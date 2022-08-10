
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import RegisterSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer
    http_method_names = ['get', 'post', 'patch', 'put']

