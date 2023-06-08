from django.db import models
from django import forms


class VideoUploadForm(forms.Form):
    video = forms.FileField(label='选择视频')


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)


class Tag(models.Model):
    tag = models.CharField(verbose_name='标签集合', max_length=64)
    count = models.IntegerField(verbose_name='选用此标签的视频数量', default=0)


class Zone(models.Model):
    zone = models.CharField(verbose_name='分区', max_length=64)


class Video_like_list(models.Model):
    user_id = models.IntegerField(verbose_name='用户id', default=0)
    video_id = models.IntegerField(verbose_name='点赞的视频id', default=0)


class UserToHistory(models.Model):
    user_id = models.IntegerField(verbose_name='用户id', default=0)
    video_id = models.IntegerField(verbose_name='看过的视频id', default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-created_time']

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
    user = models.ForeignKey(User, verbose_name='所属用户',
                             on_delete=models.CASCADE)
    upload_date = models.DateTimeField('上传时间', auto_now_add=True)

    # 0 - 待审核   1 - 审核通过    2 - 未通过   3 - 被管理员手动改为审核
    isAudit = models.IntegerField('状态', default=0)

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
    video = models.ForeignKey(
        Video, verbose_name='所属视频', on_delete=models.CASCADE, default=None)
    # 0 - 正处于投诉状态，  1 - 投诉不成功   2 - 投诉成功
    verify_result = models.IntegerField(verbose_name='投诉结果', default=0)

    def to_dic(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'verify_result': self.verify_result,
            'video': self.video.to_simple_dic(),
        }


class UserToFollow(models.Model):
    user_id = models.IntegerField(verbose_name='主体', default=0)
    follow_id = models.IntegerField(verbose_name='关注的up主', default=0)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


# class Comment(models.Model):
#     user = models.ForeignKey(User, user_name='用户名', on_delete=models.CASCADE)
#     video = models.ForeignKey(Video, verbose_name='所属视频', on_delete=models.CASCADE)
#     content = models.TextField('评论内容')
#     comment_time = models.DateTimeField(auto_now_add=True)
#     like_num = models.IntegerField(verbose_name='点赞数', default=0)
#     is_like = models.IntegerField(verbose_name='是否已点赞', default=0)
#     reply_id = models.IntegerField("回复编号", default=0)
#     reply_username = models.CharField('回复用户名', max_length=64, default="null")
#     reply_userid = models.IntegerField('回复评论用户id', default=0)
#     user_id = models.IntegerField("所属用户号", default=0)
#     root_id = models.IntegerField("根评论id", default=0)

#     def __str__(self):
#         return self.content

#     class Meta:
#         ordering = ['-created_time']
#         verbose_name = '评论'
#         verbose_name_plural = '评论列表'
#         db_table = "comment"  # 数据库表名

#     def to_dic(self):
#         return {
#             'id': self.id,
#             'username': self.user,
#             'user_id': self.user_id,
#             'avatar_url': User.objects.get(id=self.user_id).avatar_url,
#             'content': self.content,
#             'like_num': self.like_num,
#             'is_like': self.is_like,
#             'comment_time': self.comment_time,
#             'video_id': self.video.id,
#             'reply_id': self.reply_id,
#             'reply_username': self.reply_username,
#             'reply_userid': self.reply_userid,
#             "root_id": self.root_id,
#         }

#     # 评论获得点赞
#     def add_like(self):
#         self.like_num += 1
#         self.save(update_fields=['like_num'])

#     # 评论取消点赞
#     def del_like(self):
#         if self.like_num > 0:
#             self.like_num -= 1
#             self.save(update_fields=['like_num'])


class UserToComment_like(models.Model):
    user_id = models.IntegerField(verbose_name='主体', default=0)
    comment_id = models.IntegerField(verbose_name='点赞的评论', default=0)
    root_id = models.IntegerField(verbose_name='点赞的根评论', default=0)


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


# 投诉
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, null=True, blank=True)
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
