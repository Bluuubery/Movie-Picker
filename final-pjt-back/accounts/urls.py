from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:user_pk>/', views.user_profile),

    path('<int:user_pk>/to_watch/', views.to_watch_list),
    path('<int:user_pk>/watched/', views.watched_list),
    path('<int:user_pk>/best/', views.best_list),
    
    path('<int:user_pk>/<int:movie_pk>/to_watch/', views.to_watch),
    path('<int:user_pk>/<int:movie_pk>/watched/', views.watched),

    path('<int:user_pk>/<int:movie_pk>/add_best/', views.add_best),

    path('<int:best_movie_pk>/delete_best/', views.delete_best),


    path('testtest/', views.testtest),
]