from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from users.models import Complaint, Video, Comment


@login_required(login_url='/login/')
def complaints(request):
    if not request.user.is_superuser:
        return redirect('home')
    complaints = Complaint.objects.all().order_by('-time')
    return render(request, 'complaints.html', {'complaints': complaints})


@login_required(login_url='/login/')
def review_complaint(request, complaint_id):
    if not request.user.is_superuser:
        return redirect('home')
    complaint = get_object_or_404(Complaint, id=complaint_id)
    if request.method == 'POST':
        if complaint.video:
            complaint.video.delete()
        if complaint.comment:
            complaint.comment.delete()
        complaint.delete()
        return redirect('complaints')
    return render(request, 'review_complaint.html', {'complaint': complaint})


@login_required(login_url='/login/')
def delete_video(request, video_id):
    if not request.user.is_superuser:
        return redirect('home')
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('home')
    return render(request, 'delete_video.html', {'video': video})


@login_required(login_url='/login/')
def delete_comment(request, comment_id):
    if not request.user.is_superuser:
        return redirect('home')
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'delete_comment.html', {'comment': comment})
