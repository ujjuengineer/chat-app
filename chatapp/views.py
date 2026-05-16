from django.shortcuts import render

import chatapp
from .models import ChatMessage, ChatRoom

# Create your views here.
def index(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'rooms':rooms})

def chatroom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)
    return render(request, 'chatapp/room.html', {'chatroom':chatroom, 'messages':messages})