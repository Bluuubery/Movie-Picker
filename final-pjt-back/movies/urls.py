from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('movie_list_small/', views.movie_list_small),
    path('<int:movie_pk>/', views.movie_detail),
    path('search_movie/<str:query>/', views.search_movie)
]
