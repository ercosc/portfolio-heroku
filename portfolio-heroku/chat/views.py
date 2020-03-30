from django.shortcuts import render
from django.views.generic import CreateView
from .models import User


def IndexCreate(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    print(request.POST)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
    })
