from django.contrib import admin
from .models import User
# from movies.models import *

# Register your models here.

# class MovieInline(admin.TabularInline):
#     model = Movie

# class UserAdmin(admin.ModelAdmin):
#     inlines = [
#         MovieInline
#     ]

admin.site.register(User)
