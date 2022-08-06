from django.urls import path, include
from rest_framework import routers
from .views import RoomViewSet

router = routers.DefaultRouter()
router.register('room', RoomViewSet, basename='room')

urlpatterns = [
    # path('room/{slug}', RoomViewSet.as_view({'get':'retrieve'}), name='room_name'),
    path('', include(router.urls)),
]

