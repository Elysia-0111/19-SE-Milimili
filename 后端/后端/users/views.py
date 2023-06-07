from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import User, Video, Like
from django.http import JsonResponse
# from .forms import VideoForm, CommentForm


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        response = JsonResponse({'message': '注册成功'})
        user = User.objects.create(
            name=username, email='5', password='21373225')
        return response
    return JsonResponse({'message': '请求方法错误'}, status=405)
    # form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}!')
    #         return redirect('login')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    videos = Video.objects.filter(user=user)
    return render(request, 'profile.html', {'user': user, 'users': videos})


@login_required(login_url='/login/')
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            messages.success(request, 'Your video has been uploaded')
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})


@login_required(login_url='/login/')
def follow(request, user_id):
    user = get_object_or_404(User, id=user_id)
    request.user.following.add(user)
    return redirect('home')


@login_required(login_url='/login/')
def unfollow(request, user_id):
    user = get_object_or_404(User, id=user_id)
    request.user.following.remove(user)
    return redirect('home')


@login_required(login_url='/login/')
def like(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    like, created = Like.objects.get_or_create(user=request.user, video=video)
    if not created:
        messages.warning(request, 'You have already liked this video')
    return redirect('home')


@login_required(login_url='/login/')
def unlike(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    try:
        like = Like.objects.get(user=request.user, video=video)
        like.delete()
    except Like.DoesNotExist:
        messages.warning(request, 'You have not liked this video')
    return redirect('home')


@login_required(login_url='/login/')
def comment(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.video = video
            comment.save()
            messages.success(request, 'Your comment has been posted')
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})
