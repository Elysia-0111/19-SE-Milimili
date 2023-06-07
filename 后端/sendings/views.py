from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Notification
import random
from random import Random

@login_required(login_url='/login/')
def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-time')
    return render(request, 'notifications.html', {'notifications': notifications})


def create_code(random_length=6):
    str_code = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str_code += chars[random.randint(0, length)]
    return str_code
