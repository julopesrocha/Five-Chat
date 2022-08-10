from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Message, Room

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    lookup_field = 'slug'
    extra_kwargs = {
        'url': {'lookup_field': 'slug'}
    }
    

    def room(request, slug):
        room = Room.objects.get(slug=slug)
        messages = Message.objects.filter(room=room)[0:25]

        return render(request, {'room':room, 'messages':messages})
