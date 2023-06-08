from django.urls import include, path
from users import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('change_password/', views.change_password),
    path('upload_avatar/', views.upload_avatar),
    path('change_file/', views.change_file),
    path('follow/', views.follow),
    path('unfollow/', views.unfollow),
    path('follow-list/', views.follow_list),
    path('fan-list/', views.fan_list),
    path('video-list/', views.video_list),
    path('all-list/', views.all_list),
    path('up-follow-list/', views.up_follow_list),
    path('up-fan-list/', views.up_fan_list),
    path('up-video-list/', views.up_video_list),
    path('up-all-list/', views.up_all_list),
    path('get_userid/', views.get_userid),
    path('get_user/', views.simple_list),
    path('havefollow/', views.havefollow),
    path('getfollow/', views.getfollow),
    path('getfan/', views.getfan),
    path('show/', views.show)
]
