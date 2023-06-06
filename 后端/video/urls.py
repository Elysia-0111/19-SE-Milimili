from django.urls import path
from 后端.videos import videos
from 后端.users import users
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', videos.views.home, name='home'),
    path('upload_video/', videos.views.upload_video, name='upload_video'),
    # path('video/<int:video_id>/', videos.views.video_detail, name='video_detail'),
    path('complain-video', videos.views.complain_video),
    path('del-video', videos.views.del_video),
    path('trending/', videos.views.trending, name='trending'),
    path('search/', videos.views.search, name='search'),
    path('like-list', videos.views.like_list),
    path('add-comment', videos.views.add_comment),
    path('del-comment', videos.views.del_comment),
    path('reply-comment', videos.views.reply_comment),
    path('like-comment', videos.views.like_comment),
    path('detail/<str:video_id>', videos.views.video_page),
    path('api/register/', videos.views.register),
]

if settings.DEBUG:
    urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static('media/avatar/', document_root=settings.MEDIA_ROOT)
