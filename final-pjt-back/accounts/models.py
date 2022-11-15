from django.db import models
from movies.models import *
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    watched_movies = models.ManyToManyField(Movie, related_name='watched_user')
    to_watch_movies = models.ManyToManyField(Movie, related_name='to_watch_user')
    pass
