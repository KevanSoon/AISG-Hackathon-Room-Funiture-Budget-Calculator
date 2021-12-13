from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User
import os

ROOM_TYPE = (
    ('LR', 'Living Room'),
    ('KC', 'Kitchen'),
    ('R', 'Room'),

)

THEMES = (
    ('French','French'),
    ('Japanese','Japanese')
)


class Room(models.Model):
    room_type = models.CharField(max_length=200,choices= ROOM_TYPE, default='LR')
    theme = models.CharField(max_length=200,choices=THEMES, default='Japanese')
    image = models.ImageField(upload_to='room/images',blank=True)  
    funiture_count = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Funiture(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=100)
    object_count = models.IntegerField(blank=True,null=True)
    object_price = models.FloatField(default=0)





# class Image(models.Model):
#     image = models.ImageField(blank=True,null=True)   


 