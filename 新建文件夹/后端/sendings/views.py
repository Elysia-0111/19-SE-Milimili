from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Notification


@login_required(login_url='/login/')
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-time')
    return render(request, 'notifications.html', {'notifications': notifications})
