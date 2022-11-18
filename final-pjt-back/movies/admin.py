from django.contrib import admin
from .models import Movie, BestMovie

# Register your models here.

admin.site.register(Movie)
admin.site.register(BestMovie)

# admin.site.register(Genre)