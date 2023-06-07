import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.db.models import expressions

# from . import global_variables
# from .global_variables import userid
from sendings.views import create_code
from utils.Bucket import Bucket
from video.settings import *
from .models import *
from videos import views
import re
from django.conf import settings

userid = 0


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('repassword')

        if len(username) == 0 or len(password) == 0 or len(password2) == 0:
            result = {'result': 0, 'message': r'用户名与密码不允许为空!'}
            return JsonResponse(result)

        if password != password2:
            response = JsonResponse({'result': 0, 'message': ' 两次密码不一致'})

        if User.objects.filter(username=username).exists():
            result = {'result': 0, 'message': r'用户已存在!'}
            return JsonResponse(result)

        response = JsonResponse({'result': 1, 'message': '注册成功'})
        user = User.objects.create(name=username, password=password)
        return response
    else:
        return JsonResponse({'result': 0, 'message': '请求方法错误'}, status=405)


# userid = 0
def login(request):
    if request.method == 'POST':
        # 获取表单信息
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if len(username) == 0 or len(password) == 0:
            result = {'result': 0, 'message': r'用户名与密码不允许为空!'}
            return JsonResponse(result)

        if not User.objects.filter(username=username, isActive=True).exists():
            result = {'result': 0, 'message': r'用户不存在!'}
            return JsonResponse(result)

        user = User.objects.get(username=username, isActive=True)

        if user.password != password:
            result = {'result': 0, 'message': r'用户名或者密码有误!'}
            return JsonResponse(result)
        global userid
        userid = user.id
        result = {'result': 1, 'message': r"登录成功！", 'user': user.to_dic()}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def find_password(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        if not User.objects.filter(username=username).exists():
            result = {'result': 0, 'message': r'用户名不存在!'}
            return JsonResponse(result)
        user = User.objects.get(username=username)
        # 获取密码
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if len(password1) == 0 or len(password2) == 0:
            result = {'result': 0, 'message': r'用户名与密码不允许为空!'}
            return JsonResponse(result)

        if password1 != password2:
            result = {'result': 0, 'message': r'两次密码不一致!'}
            return JsonResponse(result)

        email = user.email
        result = {'result': 1, 'message': r'修改成功!'}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def upload_avatar(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        # 获取用户上传的头像并检验是否符合要求
        avatar = request.FILES.get("avatar", None)
        if not avatar:
            result = {'result': 0, 'message': r"请上传图片！"}
            return JsonResponse(result)
        if avatar.size > 1024 * 1024:
            result = {'result': 0, 'message': r"图片不能超过1M！"}
            return JsonResponse(result)
        # 获取文件尾缀并修改名称
        suffix = '.' + avatar.name.split(".")[-1]
        avatar.name = str(user_id) + suffix
        # 保存到本地
        user.avatar = avatar
        user.save()
        # 常见对象存储的对象
        bucket = Bucket()
        # 先生成一个随机 Key 保存在桶中进行审核
        key = create_code()
        upload_result = bucket.upload_file("avatar", key + suffix, avatar.name)
        # 上传审核
        if upload_result == -1:
            result = {'result': 0, 'message': r"上传失败！"}
            os.remove(os.path.join(BASE_DIR, "media/" + avatar.name))
            return JsonResponse(result)

        # 审核
        audit_dic = bucket.image_audit("avatar", key + suffix)
        if audit_dic.get("result") != 0:
            result = {'result': 0, 'message': r"审核失败！", "user": user.to_dic()}
            # 删除审核对象
            bucket.delete_object("avatar", key + suffix)
            # 删除本地对象
            os.remove(os.path.join(BASE_DIR, "media/" + avatar.name))
            return JsonResponse(result)

        # 删除审核对象
        bucket.delete_object("avatar", key + suffix)

        # 判断用户是不是默认头像   如果不是，要删除以前的
        if re.match("media/avatar/a" + r'\d\.png', user.avatar_url) is None:
            try:
                bucket.delete_object("avatar", str(user_id) + ".png")
            except:
                pass
            try:
                bucket.delete_object("avatar", str(user_id) + ".jpg")
            except:
                pass
            try:
                bucket.delete_object("avatar", str(user_id) + ".jpeg")
            except:
                pass

        # 上传是否成功
        upload_result = bucket.upload_file("avatar", str(user_id) + suffix, avatar.name)
        if upload_result == -1:
            os.remove(os.path.join(BASE_DIR, "media/" + avatar.name))
            result = {'result': 0, 'message': r"上传失败！"}
            return JsonResponse(result)

        # 上传是否可以获取路径
        url = bucket.query_object("avatar", str(user_id) + suffix)
        if not url:
            os.remove(os.path.join(BASE_DIR, "media/" + avatar.name))
            result = {'result': 0, 'message': r"上传失败！"}
            return JsonResponse(result)
        # 获取对象存储的桶地址
        user.avatar_url = url
        user.save()
        # 删除本地文件
        os.remove(os.path.join(BASE_DIR, "media/" + avatar.name))

        result = {'result': 1, 'message': r"上传成功！", "user": user.to_dic()}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 获取个人关注列表的id
def get_follow_list_simple(user_id):
    return [x.follow_id for x in UserToFollow.objects.filter(user_id=user_id)]


# 获取个人关注列表的详情(具体信息)
def get_follow_list_detail(user_id):
    return [User.objects.get(id=x).to_dic() for x in get_follow_list_simple(user_id)]


# 获取个人粉丝列表的id
def get_fan_list_simple(user_id):
    return [x.fan_id for x in UserToFan.objects.filter(user_id=user_id)]


# 获取个人粉丝列表的详情(具体信息)
def get_fan_list_detail(user_id):
    return [User.objects.get(id=x).to_dic() for x in get_fan_list_simple(user_id)]


# 关注一个用户
def follow(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        # 获取关注用户的实体和id
        follow_id = int(request.POST.get('follow_id', ''))
        try:
            follow_user = User.objects.get(id=follow_id)
        except Exception as e:
            result = {'result': 0, 'message': r"关注的用户不存在!"}
            return JsonResponse(result)

        # 是否已关注
        if follow_id in get_follow_list_simple(user_id):
            result = {'result': 0, 'message': r"已关注该用户!"}
            return JsonResponse(result)

        # 添加双向记录
        UserToFollow.objects.create(user_id=user_id, follow_id=follow_id)
        UserToFan.objects.create(user_id=follow_id, fan_id=user_id)

        # 关注数+1 , 粉丝数+1
        user.add_follow()
        follow_user.add_fan()

        result = {'result': 1, 'message': r"关注成功！", "user": user.to_dic()}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 取消关注
def unfollow(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        # 获取取消关注用户的实体和id
        follow_id = int(request.POST.get('follow_id', ''))
        try:
            follow_user = User.objects.get(id=follow_id)
        except Exception as e:
            result = {'result': 0, 'message': r"取消关注的用户不存在!"}
            return JsonResponse(result)

        # 是否已关注
        if follow_id not in get_follow_list_simple(user_id):
            result = {'result': 0, 'message': r"从未关注过该用户!"}
            return JsonResponse(result)

        # 删除双向记录
        UserToFollow.objects.get(user_id=user_id, follow_id=follow_id).delete()
        UserToFan.objects.get(user_id=follow_id, fan_id=user_id).delete()

        # 关注数-1 , 粉丝数-1
        user.del_follow()
        follow_user.del_fan()

        result = {'result': 1, 'message': r"取消成功！", "user": user.to_dic()}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 展示关注列表
def follow_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取关注列表成功！", "user": user.to_dic(),
                  "follow_list": get_follow_list_detail(user_id)}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 展示粉丝列表
def fan_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取粉丝列表成功！", "user": user.to_dic(),
                  "fan_list": get_fan_list_detail(user_id), }
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 获取自己正常的视频列表
def video_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)
        result = {'result': 1, 'message': r"获取视频列表成功！", "user": user.to_dic(),
                  "video_list": [x.to_dic() for x in Video.objects.filter(user_id=user_id, isAudit=1)],
                  "video_num": len(Video.objects.filter(user_id=user_id, isAudit=1))}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def all_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取详情列表成功！", "user": user.to_dic(),
                  "follow_list": get_follow_list_detail(user_id),
                  "fan_list": get_fan_list_detail(user_id),
                  "video_list": [x.to_dic() for x in Video.objects.filter(user_id=user_id)],
                  "video_num": len(Video.objects.filter(user_id=user_id)),
                  }
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def simple_list(request):
    if request.method == 'POST':

        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)
        result = {'result': 1, 'message': r"获取简略列表成功！",
                  "user": user.to_simple_dic()}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 展示up主粉丝列表
def up_fan_list(request):
    if request.method == 'POST':
        # 检查表单信息
        up_user_id = request.POST.get('up_user_id', '')
        try:
            up_user = User.objects.get(id=up_user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"获取粉丝列表失败！"}
            return JsonResponse(result)
        result = {'result': 1, 'message': r"获取粉丝列表成功！", "user": up_user.to_dic(),
                  "fan_list": get_fan_list_detail(up_user_id)}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 展示up主关注列表
def up_follow_list(request):
    if request.method == 'POST':
        # 检查表单信息
        up_user_id = request.POST.get('up_user_id', '')
        try:
            up_user = User.objects.get(id=up_user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"获取关注列表失败！"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取关注列表成功！", "user": up_user.to_dic(),
                  "follow_list": get_follow_list_detail(up_user_id)}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 获取up主视频列表
def up_video_list(request):
    if request.method == 'POST':
        # 检查表单信息
        up_user_id = request.POST.get('up_user_id', '')
        try:
            up_user = User.objects.get(id=up_user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"获取关注列表失败！"}
            return JsonResponse(result)
        result = {'result': 1, 'message': r"获取视频列表成功！", "user": up_user.to_dic(),
                  "video_list": [x.to_dic() for x in
                                 Video.objects.filter(user_id=up_user_id, isAudit=1)],
                  "video_num": len(Video.objects.filter(user_id=up_user_id, isAudit=1))}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def up_all_list(request):
    if request.method == 'POST':
        # 检查表单信息
        up_user_id = int(request.POST.get('up_user_id', 0))
        try:
            up_user = User.objects.get(id=up_user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"获取详情列表失败！"}
            return JsonResponse(result)

        JWT = request.POST.get('JWT', '')
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 1, 'message': r"获取详情列表成功！", "user": up_user.to_dic(),
                      'is_follow': -1,
                      "follow_list": get_follow_list_detail(up_user_id),
                      "fan_list": get_fan_list_detail(up_user_id),
                      "video_list": [x.to_dic() for x in
                                     Video.objects.filter(user_id=up_user_id, isAudit=1)],
                      "video_num": len(Video.objects.filter(user_id=up_user_id, isAudit=1)), }
            return JsonResponse(result)
        result = {'result': 1, 'message': r"获取详情列表成功！", "user": up_user.to_dic(),
                  'is_follow': views.is_follow(user_id=user_id, target_id=up_user_id),
                  "follow_list": get_follow_list_detail(up_user_id),
                  "fan_list": get_fan_list_detail(up_user_id),
                  "video_list": [x.to_dic() for x in
                                 Video.objects.filter(user_id=up_user_id, isAudit=1)],
                  "video_num": len(Video.objects.filter(user_id=up_user_id, isAudit=1))}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)
