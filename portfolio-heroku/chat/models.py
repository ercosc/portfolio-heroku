from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    room = models.CharField(max_length=120)

    def get_absolute_url(self):
        return reverse("chat:room", kwargs={"room_name": self.room})
