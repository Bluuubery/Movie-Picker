from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 내 프로필, 피드, 개인 추천 영화
    path('profile/', views.user_profile),
    path('feed/', views.get_feed), # 팔로우한 유저들의 인생 영화
    path('get_my_recommendations/', views.get_my_recommendations), 

    # 상태 메세지 수정
    path('update_message/', views.update_message),
    path('update_avatar/', views.update_avatar),

    # to watch, watch, best 목록
    path('<int:user_pk>/to_watch/', views.to_watch_list),
    path('<int:user_pk>/watched/', views.watched_list),
    path('<int:user_pk>/best/', views.best_list),
    
    # to_watch, watch 추가 및 삭제
    path('<int:user_pk>/<int:movie_pk>/to_watch/', views.to_watch),
    path('<int:user_pk>/<int:movie_pk>/watched/', views.watched),

    # best 추가, 삭제
    path('<int:user_pk>/<int:movie_pk>/add_best/', views.add_best),
    path('<int:best_movie_pk>/delete_best/', views.delete_best),

    # 팔로우/언팔로우, 유저 검색, 다른 사람 프로필
    path('follow/<int:user_pk>/', views.follow), 
    path('search_user/<str:query>/', views.search_user),
    path('get_profile/<int:user_pk>/', views.get_profile), # 이름, 상메, 프사, 팔로잉, 팔로우

    
    # path('testtest/', views.testtest), # 테스트용 url입니다.
]