from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.user_profile), # 내 프로필
    path('feed/', views.get_feed), # 내 피드(팔로우한 유저들의 인생 영화)

    path('<int:user_pk>/to_watch/', views.to_watch_list),
    path('<int:user_pk>/watched/', views.watched_list),
    path('<int:user_pk>/best/', views.best_list),
    
    path('<int:user_pk>/<int:movie_pk>/to_watch/', views.to_watch),
    path('<int:user_pk>/<int:movie_pk>/watched/', views.watched),

    path('<int:user_pk>/<int:movie_pk>/add_best/', views.add_best),

    path('<int:best_movie_pk>/delete_best/', views.delete_best),

    path('follow/<int:user_pk>/', views.follow), # 다른 유저 팔로우/언팔로우

    path('search_user/<str:query>/', views.search_user), # 유저 검색

    path('get_my_recommendations/', views.get_my_recommendations),

    path('testtest/', views.testtest),
]