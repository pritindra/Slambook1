from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Slam(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    nickname = models.CharField(max_length=100)
    petname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    birthday = models.DateField()
    zodiac = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)

    ambition = models.CharField(max_length=100)
    films = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    songs = models.CharField(max_length=100)
    books = models.CharField(max_length=100)
    reality_show = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)

    friends = models.CharField(max_length=100)
    crush = models.CharField(max_length=100)
    fantasy = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    feature = models.CharField(max_length=100)
    lifeline = models.CharField(max_length=100)
    fear = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    movie_role = models.CharField(max_length=100)
    lines_for = models.CharField(max_length=500)

    date = models.DateField()


