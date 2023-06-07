
from videos import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
urlpatterns = [
    path('', views.home, name='home'),
    path('api/upload_video/', views.upload_video, name='upload_video'),
    # path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('api/complain-video', views.complain_video),
    path('api/del-video', views.del_video),
    path('api/trending/', views.trending, name='trending'),
    path('api/search/', views.search, name='search'),
    path('api/like-list', views.like_list),
    path('api/add-comment', views.add_comment),
    path('api/del-comment', views.del_comment),
    path('api/reply-comment', views.reply_comment),
    path('api/like-comment', views.like_comment),
    path('api/detail/<str:video_id>', views.video_page),
    path('api/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static('media/avatar/', document_root=settings.MEDIA_ROOT)
