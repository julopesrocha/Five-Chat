from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField()
    slug = serializers.SlugField()

    class Meta:
        model = Room
        fields = ['id', 'name', 'slug']