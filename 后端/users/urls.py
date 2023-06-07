from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('find_password/', views.find_password),
    path('upload_avatar/', views.upload_avatar),

    path('follow/', views.follow),
    path('unfollow/', views.unfollow),
    path('follow-list/', views.follow_list),
    path('fan-list/', views.fan_list),
    path('video-list/', views.video_list),
    path('all-list/', views.all_list),
    path('simple-list/', views.simple_list),
    path('up-follow-list/', views.up_follow_list),
    path('up-fan-list/', views.up_fan_list),
    path('up-video-list/', views.up_video_list),
    path('up-all-list/', views.up_all_list),
]
