from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(max_length=20)
    picture = models.ImageField()

    def __str__(self) -> str:
        return str(
            self.user.username,
            self.room.name,
            self.picture
        )