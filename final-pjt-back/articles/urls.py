from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<int:movie_pk>/review_movie/', views.review_movie),
    path('<int:user_pk>/review_user/', views.review_user),
    path('<int:movie_pk>/review_create/', views.review_create),
    path('<int:review_pk>/', views.review_detail)

]