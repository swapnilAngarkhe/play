from django.db import models

# Create your models here.

#Room, will be created by the host
class Room(models.Model):
    code=models.CharField(max_length=5, default="", unique=True)
    #setting only one host per room, ie: one host canot have multiple rooms.
    host=models.CharField(max_length=50, unique=True)