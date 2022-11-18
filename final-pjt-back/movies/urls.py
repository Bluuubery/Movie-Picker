from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    # add해주는 그런,,,
    # path('best_movies/<int:movie_pk>/', views.best_movies),
    # path('add_watched/<int:movie_pk>/', views.add_watched),
    # path('add_to_watch/<int:movie_pk>/', views.add_to_watch),
]
