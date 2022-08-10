from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self) -> str:
        return str(
            self.user.username,
            self.room.name,
            self.picture
        )