from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from .models import Room

class RoomTestCase(TestCase):
    def setUp(self):
        self.room_1 = baker.make(Room)
        self.room_2 = baker.make(Room)
        self.room_3 = baker.make(Room)

    def test_list_rooms(self):
        """
        List all rooms, expected HTTP status code : 200 (OK)   
        """

        response = self.client.get('/room/')
        rooms = Room.objects.all()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), rooms.count())
    

    def test_list_error(self):
        """List unexistent room by slug, expected HTTP status code: 404 not found
        """
        response = self.client.get('/room/coder/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data.get('detail'), 'Not found.')