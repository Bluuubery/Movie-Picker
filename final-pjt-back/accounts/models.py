from django.db import models
from movies.models import *
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    message = models.CharField(max_length=100, null=True)

    avatar = models.ImageField(null=True, default="default_avatar_2.svg")

    watched_movies = models.ManyToManyField(Movie, related_name='watched_user')
    to_watch_movies = models.ManyToManyField(Movie, related_name='to_watch_user')
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    