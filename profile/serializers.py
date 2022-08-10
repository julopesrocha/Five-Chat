import profile
from signal import valid_signals
from rest_framework import serializers
from profile.models import Profile
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    
    #output
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    #input
    email = serializers.EmailField(write_only=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    picture = serializers.ImageField()

    class Meta:
        model = Profile
        fields = ['picture', 'user_email','user_username', 'email', 'username', 'password', 'confirm_password']

    def create_user(self, validated_data):
        filter_user = User.objects.filter(username=validated_data.get('username'))

        if not filter_user.exists():
            user = User.objects.create_user(validated_data.get('username'), validated_data.get('password'))
        else:
            user = filter_user[0]
        return user

    def create(self, validated_data):
        user = self.create_user(validated_data)
        validated_data.pop('username')
        validated_data.pop('password')
        validated_data.pop('confirm_password')
        validated_data['user']=user
        validated_data['picture']='https://ui-avatars.com/api/?background=random'
        profile = Profile.objects.create(**validated_data)
        return profile

