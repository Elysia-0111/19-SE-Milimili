from django.db import models
from django import forms
from django.conf import settings


class VideoUploadForm(forms.Form):
    video = forms.FileField(label='选择视频')

    class Meta:
        db_table = 'VideoUploadForm'


class User(models.Model):
    username = models.CharField('用户名', max_length=30)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField()
    nickname = models.CharField('昵称', max_length=30, default='')
    sex = models.CharField('性别', max_length=12, default='')
    signature = models.CharField('个人签名', max_length=256, default='')
    birthday = models.CharField('生日', max_length=32, default='')
    location = models.CharField('所在地', max_length=32, default="中国大陆")
    video_num = models.IntegerField(verbose_name='视频数', default=0)
    like_num = models.IntegerField(verbose_name='收获的点赞数', default=0)
    collect_num = models.IntegerField(verbose_name='收获的收藏数', default=0)
    favorite_num = models.IntegerField(verbose_name='收藏夹数', default=0)
    fan_num = models.IntegerField(verbose_name='粉丝数', default=0)
    follow_num = models.IntegerField(verbose_name='关注数', default=0)
    avatar_url = models.CharField('用户头像路径', max_length=128, default='')
    avatar = models.FileField('用户头像', upload_to='')
    isActive = models.BooleanField('是否有效', default=False)
    isSuperAdmin = models.BooleanField('是否为超级管理员', default=False)

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    complain_time = models.DecimalField('投诉时间', max_digits=12, decimal_places=2, default=0.0)

    def to_simple_dic(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar_url": self.avatar_url,
            'fan_num': self.fan_num,
            'video_num': self.video_num,
            'created_time': self.created_time,
        }

    def to_dic(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            'nickname': self.nickname,
            'sex': self.sex,
            'signature': self.signature,
            'birthday': self.birthday,
            'location': self.location,
            "video_num": self.video_num,
            "like_num": self.like_num,
            "collect_num": self.collect_num,
            'favorite_num': self.favorite_num,
            "fan_num": self.fan_num,
            "follow_num": self.follow_num,
            "avatar_url": self.avatar_url,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "isSuperAdmin": self.isSuperAdmin,
        }

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'  # 改变当前模型类对应的表名
        verbose_name = '网站用户'
        verbose_name_plural = "网站用户列表"

    # 发布视频
    def add_video(self):
        self.video_num += 1
        self.save(update_fields=['video_num'])

    # 删除视频
    def del_video(self):
        if self.video_num > 0:
            self.video_num -= 1
            self.save(update_fields=['video_num'])

    # 视频获得点赞
    def add_like(self):
        self.like_num += 1
        self.save(update_fields=['like_num'])

    # 视频取消点赞
    def del_like(self):
        if self.like_num > 0:
            self.like_num -= 1
            self.save(update_fields=['like_num'])

    # 收获粉丝
    def add_fan(self):
        self.fan_num += 1
        self.save(update_fields=['fan_num'])

    # 减少粉丝
    def del_fan(self):
        if self.fan_num > 0:
            self.fan_num -= 1
            self.save(update_fields=['fan_num'])

    # 添加关注
    def add_follow(self):
        self.follow_num += 1
        self.save(update_fields=['follow_num'])

    # 取消关注
    def del_follow(self):
        if self.follow_num > 0:
            self.follow_num -= 1
            self.save(update_fields=['follow_num'])

    # 添加收藏夹
    def add_favorite(self):
        self.favorite_num += 1
        self.save(update_fields=['favorite_num'])

    # 删除收藏夹
    def del_favorite(self):
        if self.favorite_num > 0:
            self.favorite_num -= 1
            self.save(update_fields=['favorite_num'])


class UserToFan(models.Model):
    user_id = models.IntegerField(verbose_name='主体', default=0)
    fan_id = models.IntegerField(verbose_name='粉丝', default=0)

    class Meta:
        db_table = 'UserToFan'


# 查看个人关注
class UserToFollow(models.Model):
    user_id = models.IntegerField(verbose_name='主体', default=0)
    follow_id = models.IntegerField(verbose_name='关注的up主', default=0)

    class Meta:
        db_table = 'UserToFollow'


class Tag(models.Model):
    tag = models.CharField(verbose_name='标签集合', max_length=64)
    count = models.IntegerField(verbose_name='选用此标签的视频数量', default=0)

    class Meta:
        db_table = 'Tag'


class Zone(models.Model):
    zone = models.CharField(verbose_name='分区', max_length=64)

    class Meta:
        db_table = 'Zone'


class Video_like_list(models.Model):
    user_id = models.IntegerField(verbose_name='用户id', default=0)
    video_id = models.IntegerField(verbose_name='点赞的视频id', default=0)

    class Meta:
        db_table = 'Video_like_list'


class UserToHistory(models.Model):
    user_id = models.IntegerField(verbose_name='用户id', default=0)
    video_id = models.IntegerField(verbose_name='看过的视频id', default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-created_time']
        db_table = 'UserToHistory'

    def to_dic(self):
        return {
            'video': Video.objects.get(id=self.video_id).to_simple_dic()
        }


class Video(models.Model):
    title = models.CharField('标题', max_length=256)
    description = models.TextField('视频简介')
    video = models.FileField('视频', upload_to='', default='')
    avatar = models.FileField('封面', upload_to='', default='')
    avatar_path = models.CharField('封面路径', max_length=256, default='')
    video_path = models.CharField('视频路径', max_length=256, default='')

    like_num = models.IntegerField(verbose_name='点赞数', )
    view_num = models.IntegerField('浏览量', default=0)
    collect_num = models.IntegerField(verbose_name='收藏数', default=0)

    zone = models.CharField('专区', max_length=32, default='')
    tag1 = models.CharField('标签1', max_length=32, default='')
    tag2 = models.CharField('标签2', max_length=32, default='')
    tag3 = models.CharField('标签3', max_length=32, default='')
    tag4 = models.CharField('标签4', max_length=32, default='')
    tag5 = models.CharField('标签5', max_length=32, default='')
    user = models.ForeignKey(User, verbose_name='所属用户', on_delete=models.CASCADE)
    upload_date = models.DateTimeField('上传时间', auto_now_add=True)

    isAudit = models.IntegerField('状态', default=0)  # 0 - 待审核   1 - 审核通过    2 - 未通过   3 - 被管理员手动改为审核

    def to_dic(self):
        tag_list = []
        if self.tag1 != '':
            tag_list.append(self.tag1)
        if self.tag2 != '':
            tag_list.append(self.tag2)
        if self.tag3 != '':
            tag_list.append(self.tag3)
        if self.tag4 != '':
            tag_list.append(self.tag4)
        if self.tag5 != '':
            tag_list.append(self.tag5)
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'video_path': self.video_path,
            'avatar_path': self.avatar_path,
            'like_num': self.like_num,
            'view_num': self.view_num,
            'collect_num': self.collect_num,
            'zone': self.zone,
            'tag_list': tag_list,
            'user': self.user.to_simple_dic(),
            'upload_date': self.upload_date,
            'isAudit': self.isAudit,
        }

    def __str__(self):
        return '视频' + self.title

    class Meta:
        ordering = ['-upload_date']  # 按视频创建日期降序
        db_table = 'video'  # 改变当前模型类对应的表名
        verbose_name = '视频'
        verbose_name_plural = '视频列表'

    # 视频获得点赞
    def add_like(self):
        self.like_num += 1
        self.save(update_fields=['like_num'])

    # 视频取消点赞
    def del_like(self):
        if self.like_num > 0:
            self.like_num -= 1
            self.save(update_fields=['like_num'])

    def add_view(self):
        self.view_num += 1
        self.save(update_fields=['view_num'])


class VideoComplain(models.Model):
    title = models.CharField('标题', max_length=64)
    description = models.TextField('描述')
    user_id = models.IntegerField(verbose_name='投诉人员编号', default=0)
    video = models.ForeignKey(Video, verbose_name='所属视频', on_delete=models.CASCADE, default=None)
    verify_result = models.IntegerField(verbose_name='投诉结果', default=0)  # 0 - 正处于投诉状态，  1 - 投诉不成功   2 - 投诉成功

    def to_dic(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'verify_result': self.verify_result,
            'video': self.video.to_simple_dic(),
        }

    class Meta:
        db_table = 'VideoComplain'



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Like'


class Comment(models.Model):
    username = models.CharField('用户名', max_length=30)
    video = models.ForeignKey(Video, verbose_name='所属视频', on_delete=models.CASCADE)
    content = models.TextField('评论内容')
    comment_time = models.DateTimeField(auto_now_add=True)
    like_num = models.IntegerField(verbose_name='点赞数', default=0)
    is_like = models.IntegerField(verbose_name='是否已点赞', default=0)
    reply_id = models.IntegerField("回复编号", default=0)
    reply_username = models.CharField('回复用户名', max_length=64, default="null")
    reply_userid = models.IntegerField('回复评论用户id', default=0)
    user_id = models.IntegerField("所属用户号", default=0)
    root_id = models.IntegerField("根评论id", default=0)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-comment_time']
        verbose_name = '评论'
        verbose_name_plural = '评论列表'
        db_table = "comment"  # 数据库表名

    def to_dic(self):
        return {
            'id': self.id,
            'username': self.user,
            'user_id': self.user_id,
            'avatar_url': User.objects.get(id=self.user_id).avatar_url,
            'content': self.content,
            'like_num': self.like_num,
            'is_like': self.is_like,
            'comment_time': self.comment_time,
            'video_id': self.video.id,
            'reply_id': self.reply_id,
            'reply_username': self.reply_username,
            'reply_userid': self.reply_userid,
            "root_id": self.root_id,
        }

    # 评论获得点赞
    def add_like(self):
        self.like_num += 1
        self.save(update_fields=['like_num'])

    # 评论取消点赞
    def del_like(self):
        if self.like_num > 0:
            self.like_num -= 1
            self.save(update_fields=['like_num'])


class UserToComment_like(models.Model):
    user_id = models.IntegerField(verbose_name='主体', default=0)
    comment_id = models.IntegerField(verbose_name='点赞的评论', default=0)
    root_id = models.IntegerField(verbose_name='点赞的根评论', default=0)

    class Meta:
        db_table = 'UserToComment_like'


class Notification(models.Model):
    TYPE_CHOICES = (
        ('comment', 'New Comment'),
        ('like', 'New Like'),
        ('follow', 'New Follower'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    content = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}'s {self.type} notification"

    class Meta:
        db_table = 'Notification'


# 投诉
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Complaint'
