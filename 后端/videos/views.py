from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from users.models import *
import time
from users.views import userid
from utils import Bucket
from video.settings import *
import os


def home(request):
    videos = Video.objects.all().order_by('upload_date')
    return render(request, 'home.html', {'videos': videos})


def upload_video(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        zone = request.POST.get('zone', '')
        tag1 = request.POST.get('tag1', '')
        tag2 = request.POST.get('tag2', '')
        tag3 = request.POST.get('tag3', '')
        tag4 = request.POST.get('tag4', '')
        tag5 = request.POST.get('tag5', '')
        avatar = request.FILES.get("avatar", None)
        if title == '':
            result = {'result': 0, 'message': r"视频标题不能为空!"}
            return JsonResponse(result)
        if description == '':
            result = {'result': 0, 'message': r"视频描述不能为空!"}
            return JsonResponse(result)
        if zone == '':
            result = {'result': 0, 'message': r"分区不能为空!"}
            return JsonResponse(result)
        video = Video.objects.create(title=title, description=description, zone=zone, user_id=user_id, tag1=tag1,
                                     tag2=tag2, tag3=tag3, tag4=tag4, tag5=tag5)
        video_id = video.id

        if avatar:
            if avatar.size > 2 * 1024 * 1024:
                Video.objects.get(id=video_id).delete()
                result = {'result': 0, 'message': r"图片不能超过2M！"}
                return JsonResponse(result)
            # 获取文件尾缀并修改名称
            suffix_avatar = '.' + avatar.name.split(".")[-1]
            avatar.name = str(video.id) + suffix_avatar
            # 封面保存到本地
            video.avatar = avatar

            video.avatar_path = video.avatar.url
            video.save()
            result = {'result': 1, 'message': r"上传成功！"}
            return JsonResponse(result)

        # 处理上传视频
        video_upload = request.FILES.get("video", None)
        if not video_upload:
            if video.video_path != '':
                # 删除封面
                video.avatar.delete()
                video.avatar_path = ''
                video.save()
            Video.objects.get(id=video_id).delete()
            result = {'result': 0, 'message': r"请上传视频！"}
            return JsonResponse(result)
        if video_upload.size > 1024 * 1024 * 100:
            if video.video_path != '':
                # 删除封面
                video.avatar.delete()
                video.avatar_path = ''
                video.save()
            Video.objects.get(id=video_id).delete()
            result = {'result': 0, 'message': r"视频大小不能超过100M！"}
            return JsonResponse(result)
        # 获取文件尾缀并修改名称
        suffix_video = '.' + video_upload.name.split(".")[-1]
        video_upload.name = str(video.id) + suffix_video
        # 保存到本地
        video.video = video_upload
        video.save()

        # 上传
        video.video_path = video.video.url
        video.save()

        bucket = Bucket()
        upload_result = bucket.upload_file(video_upload.name)
        if upload_result == -1:
            result = {'result': 0, 'message': r"上传失败！"}
            os.remove(os.path.join(BASE_DIR, "media/" + video_upload.name))
            return JsonResponse(result)
        else:
            for i in range(1, 6):
                tag = eval('tag' + str(i))
                if tag != '':
                    try:
                        tag_info = Tag.objects.get(tag=tag)
                        tag_info.count += 1
                        tag_info.save()
                    except Exception:
                        Tag.objects.create(tag=tag)
            result = {'result': 1, 'message': r"上传成功！"}
            return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def del_video(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        # 获取视频主体
        video_id = request.POST.get('video_id', '')
        video = Video.objects.get(id=video_id)

        # 清除点赞
        video_list = Video_like_list.objects.filter(video_id=video_id)
        del_like_num = len(video_list)
        user.like_num -= del_like_num
        video_list.delete()

        # 清楚历史记录
        UserToHistory.objects.filter(video_id=video_id).delete()
        # 清除本身
        video.delete()
        user.del_video()

        result = {'result': 1, 'message': r"删除视频成功！", "user": user.to_dic()}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# def video_detail(request, video_id):
#     video = get_object_or_404(Video, id=video_id)
#     comments = Comment.objects.filter(video=video).order_by('-comment_time')
#     liked = False
#     if request.user.is_authenticated:
#         try:
#             like = Like.objects.get(user=request.user, video=video)
#             liked = True
#         except Like.DoesNotExist:
#             pass
#     return render(request, 'video_detail.html', {'video': video, 'comments': comments, 'liked': liked})


def complain_video(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)
        now_time = time.time()
        if user.complain_time != 0.0:
            if now_time - float(user.complain_time) <= 60 * 60:
                result = {'result': 0, 'message': r"离上次投诉的时间间隔小于1小时，请不要频繁投诉!"}
                return JsonResponse(result)
        user.complain_time = now_time
        user.save()
        # 获取投诉信息
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        video_id = request.POST.get('video_id', 0)
        if len(title) == 0 or len(description) == 0:
            result = {'result': 0, 'message': r"投诉的标题和主体不能为空！"}
            return JsonResponse(result)
        VideoComplain.objects.create(title=title, description=description, user_id=user_id, video_id=video_id)
        video = Video.objects.get(id=video_id)

        result = {'result': 1, 'message': r"投诉视频成功！", "user": user.to_dic()}
        return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


# 视频列表
def trending(request):
    videos = Video.objects.all().order_by('upload_date')[:10]
    return render(request, 'trending.html', {'videos': videos})


# 查询
def search(request):
    query = request.GET.get('query')
    videos = Video.objects.filter(Q(title__icontains=query) |
                                  Q(zone__icontains=query) |
                                  Q(tag1__icontains=query) |
                                  Q(tag2__icontains=query) |
                                  Q(tag3__icontains=query) |
                                  Q(tag4__icontains=query) |
                                  Q(tag5__icontains=query))
    return render(request, 'search.html', {'videos': videos})


def get_like_videos_list(user_id):
    return [Video.objects.get(id=x).to_dic() for x in get_like_videoid_list(user_id)]


def get_like_videoid_list(user_id):
    return [x.video_id for x in Video_like_list.objects.filter(user_id=user_id)]


def get_like_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取点赞列表成功！", "user": user.to_dic(),
                  "like_list": get_like_videos_list(user_id)}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


# 点赞
def like_video(request):
    if request.method == 'POST':
        try:
            user_id = request.POST.get('user_id')
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        video_id = request.POST.get('video_id', '')

        if Video_like_list.objects.filter(user_id=user_id, video_id=video_id).exists():
            Video_like_list.objects.get(user_id=user_id, video_id=video_id).delete()
            video = Video.objects.get(id=video_id)
            video.del_like()
            upload_user = video.user
            upload_user.del_like()
            result = {'result': 1, 'message': r"取消成功！", "user": user.to_dic(),
                      "like_list": get_like_videos_list(user_id)
                      }
            return JsonResponse(result)
        else:
            Video_like_list.objects.create(user_id=user_id, video_id=video_id)
            video = Video.objects.get(id=video_id)
            video.add_like()
            upload_user = video.user
            upload_user.add_like()

            result = {'result': 1, 'message': r"点赞成功！", "user": user.to_dic(),
                      "like_list": get_like_videos_list(user_id)}
            return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


def like_list(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        result = {'result': 1, 'message': r"获取点赞列表成功！", "user": user.to_dic(),
                  "like_list": get_like_videos_list(user_id)}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
        return JsonResponse(result)


def get_comment_list(video_id):
    return [x.to_dic() for x in Video.objects.get(id=video_id).videocomment_set.all()]


def get_video_comment(video_id, user_id):
    if user_id != 0:
        user = User.objects.get(id=user_id)
        # 用户点赞的评论
        comment_like_dict = {x.comment_id: 1 for x in UserToComment_like.objects.filter(user_id=user_id)}

    # 当前视频所有所有评论
    comment_list = get_comment_list(video_id=video_id)
    # 对comment_list进行按照root_id进行二级列表划分
    comment_child_dict = {}
    comment_root_dict = {}
    for every_comment in comment_list:
        if user_id != 0:
            if every_comment.get('id') in comment_like_dict:
                every_comment['is_like'] = 1
        root_id = every_comment['root_id']
        # 如果是一级根存在
        if root_id == every_comment['id']:
            # 添加至根列表
            comment_root_dict[root_id] = every_comment
        # 如果是回复的评论且是第一个
        elif root_id not in comment_child_dict.keys():

            comment_child_dict[root_id] = [every_comment]
        else:
            comment_child_dict[root_id].append(every_comment)

    result_list = []
    for root_id in comment_root_dict.keys():
        comment_root = comment_root_dict[root_id]
        if root_id in comment_child_dict.keys():
            child_list = comment_child_dict[root_id]
        else:
            child_list = []
        result_list.append({'comment_root': comment_root, 'child_list': child_list})
    return result_list


# 添加评论
def add_comment(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        video_id = request.POST.get('video_id', '')
        video = Video.objects.get(id=video_id)
        username = user.username
        content = request.POST.get('content', '')
        if len(content) == 0:
            result = {'result': 0, 'message': r"评论不能为空！"}
            return JsonResponse(result)
        comment = Comment.objects.create(username=username, user_id=user_id, content=content, video_id=video_id)
        comment.root_id = comment.id
        comment.save()
        comment_list = get_video_comment(video_id, user_id)
        result = {'result': 1, 'message': r"评论成功！", "user": user.to_dic(),
                  "comment": comment_list,
                  "comment_num": len(video.videocomment_set.filter(video_id=video_id))}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


# 删除评论
def del_comment(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)
        comment_id = int(request.POST.get('comment_id', ''))
        comment = Comment.objects.get(id=comment_id)
        root_id = int(comment.root_id)
        video = comment.video
        video_id = video.id

        # 判断是否为一级评论，如果是，将要删除所有二级评论
        if comment_id == root_id:
            Comment.objects.filter(root_id=root_id).delete()
            UserToComment_like.objects.filter(root_id=root_id).delete()
        else:
            comment.delete()
            UserToComment_like.objects.filter(comment_id=comment_id).delete()

        comment_list = get_video_comment(video_id, user_id)
        result = {'result': 1, 'message': r"删除评论成功！", "user": user.to_dic(),
                  "comment": comment_list,
                  "comment_num": len(video.videocomment_set.filter(video_id=video_id))}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


# 回复评论
def reply_comment(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)
        video_id = request.POST.get('video_id', '')
        video = Video.objects.get(id=video_id)
        username = user.username
        content = request.POST.get('content', '')
        reply_comment_id = request.POST.get('reply_comment_id', '')
        reply_username = request.POST.get('reply_username', '')
        reply_user = User.objects.get(username=reply_username)
        reply_userid = reply_user.id
        if len(content) == 0:
            result = {'result': 0, 'message': r"评论不能为空！"}
            return JsonResponse(result)
        comment = Comment.objects.create(username=username, user_id=user_id, content=content, video_id=video_id,
                                         reply_comment_id=reply_comment_id, reply_username=reply_username,
                                         reply_userid=reply_userid)
        # 更新根节点
        comment.root_id = Comment.objects.get(id=reply_comment_id).root_id
        comment.save()
        comment_list = get_video_comment(video_id, user_id)
        result = {'result': 1, 'message': r"回复评论成功！", "user": user.to_dic(),
                  "comment": comment_list,
                  "comment_num": len(video.videocomment_set.filter(video_id=video_id))}
        return JsonResponse(result)
    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


# 点赞评论
def like_comment(request):
    if request.method == 'POST':
        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception as e:
            result = {'result': 0, 'message': r"请先登录!"}
            return JsonResponse(result)

        # 获取点赞视频编号 并添加点击记录
        comment_id = request.POST.get('comment_id', '')
        try:
            comment = Comment.objects.get(id=comment_id)
        except Exception as e:
            result = {'result': 0, 'message': r"该评论不存在!"}
            return JsonResponse(result)
        # 判断是否已经点赞过
        video = comment.video
        video_id = video.id
        if UserToComment_like.objects.filter(user_id=user_id, comment_id=comment_id).exists():
            UserToComment_like.objects.get(user_id=user_id, comment_id=comment_id).delete()
            comment.del_like()
            comment_list = get_video_comment(video_id, user_id)
            result = {'result': 1, 'message': r"取消点赞成功！", "user": user.to_dic(),
                      "comment": comment_list,
                      "comment_num": len(video.videocomment_set.filter(video_id=video_id))}
            return JsonResponse(result)
        else:
            # 添加点赞记录
            UserToComment_like.objects.create(user_id=user_id, comment_id=comment_id, root_id=comment.root_id)
            comment.add_like()
            comment_list = get_video_comment(video_id, user_id)

            result = {'result': 1, 'message': r"点赞评论成功！", "user": user.to_dic(),
                      "comment": comment_list,
                      "comment_num": len(video.videocomment_set.filter(video_id=video_id))}
            return JsonResponse(result)

    else:
        result = {'result': 0, 'message': r"发生错误！"}
        return JsonResponse(result)


def video_page(request, video_id):
    if request.method == 'POST':
        video_id = int(video_id)
        # 获取具体视频
        video_info = Video.objects.get(id=video_id)
        # 自己是否已经点赞或者收藏过该视频
        is_like = 0
        # is_collect = 0
        # 视频浏览量 + 1
        video_info.add_view()
        video_tag = {}
        for i in range(1, 6):
            if eval('video_info.tag' + str(i)) != '':
                video_tag[eval('video_info.tag' + str(i))] = 20
        # list_map = VideoData(video_id, video_tag).get_data()

        try:
            user_id = userid
            user = User.objects.get(id=user_id)
        except Exception:
            # 游客情况
            # 当前视频所有所有评论
            comment_list = get_video_comment(video_id, 0)
            result = {'result': 1, 'message': r"获取视频信息成功！", 'video_info': video_info.to_dic(),
                      'is_like': is_like,
                      'comment_list': comment_list,
                      "comment_num": len(video_info.videocomment_set.filter(video_id=video_id)),
                      }
            return JsonResponse(result)
        # 用户情况  需要添加历史记录,但是需要先需要判断是否已存在该记录
        if UserToHistory.objects.filter(user_id=user_id, video_id=video_id).exists():
            UserToHistory.objects.filter(user_id=user_id, video_id=video_id).delete()
        # 添加历史记录
        UserToHistory.objects.create(user_id=user_id, video_id=video_id)

        comment_list = get_video_comment(video_id, user_id)

        if Video_like_list.objects.filter(video_id=video_id, user_id=user_id).exists():
            is_like = 1
        result = {'result': 1, 'message': r"获取视频信息成功！",
                  'is_like': is_like,
                  'video_info': video_info.to_dic(),
                  'comment_list': comment_list,
                  "comment_num": len(video_info.videocomment_set.filter(video_id=video_id)),
                  }
    else:
        result = {'result': 0, 'message': r"请求方式错误！"}
    return JsonResponse(result)


# 判断是否属于已关注该视频的up主
def is_follow(user_id, target_id):
    try:
        UserToFollow.objects.get(user_id=user_id, follow_id=target_id)
    except Exception as e:
        return False
    return True
