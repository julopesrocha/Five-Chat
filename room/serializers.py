from rest_framework import serializers
from .models import Room,Message

class RoomSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Room
        fields = ['id', 'name', 'slug']
    
class MessageSerializer(serializers.ModelSerializer):
    #output
    room_name = serializers.CharField(source='room.name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    
    room = serializers.CharField(write_only=True)
    user = serializers.CharField(write_only=True)
    content = serializers.CharField(write_only=True)

    class Meta:
        model = Message
        fields = ['room_name', 'room', 'user_name', 'user', 'content']
        ordering = ('created_at')