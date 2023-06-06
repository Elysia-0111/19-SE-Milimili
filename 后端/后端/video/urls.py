from django.urls import path
from videos import views
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.home, name='home'),
    # path('upload_video/', views.upload_video, name='upload_video'),
    # path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    # path('complain-video', views.complain_video),
    # path('del-video', views.del_video),
    # path('trending/', views.trending, name='trending'),
    # path('search/', views.search, name='search'),
    # path('like-list', views.like_list),
    # path('add-comment', views.add_comment),
    # path('del-comment', views.del_comment),
    # path('reply-comment', views.reply_comment),
    # path('like-comment', views.like_comment),
    # path('detail/<str:video_id>', views.video_page),
    path('api/register/', views.register)
]

if settings.DEBUG:
    urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static('media/avatar/', document_root=settings.MEDIA_ROOT)
