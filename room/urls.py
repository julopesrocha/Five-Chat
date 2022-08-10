from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet

router = routers.DefaultRouter()
router.register('room', RoomViewSet, basename='room')
# router.register('messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]

