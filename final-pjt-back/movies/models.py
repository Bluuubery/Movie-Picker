from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Country(models.Model):
    name = models.CharField(max_length=50)



class Movie(models.Model):

    # 한국어 제목과 원제(검색용)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=200)

    # 영화 정보
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_avg = models.FloatField()
    overview = models.TextField()

    # 외부 링크(포스터, 배경, 트레일러)
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    trailer_path = models.CharField(max_length=100)

    # 장르, 국가(M:N)
    genres = models.ManyToManyField(Genre, related_name='movies')
    countries = models.ManyToManyField(Country, related_name='movies')
    
    # 추천영화(자신과 M:N)
    recommended = models.ManyToManyField('self', symmetrical=False, related_name='recommendation')

# 월드컵의 결과로 bestmovie라는 article이 생성되는 느낌으로 이해하면 됩니다.
class BestMovie(models.Model):
    # 월드컵 진행한 유저
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='best_movies')
    # 월드컵 우승한 영화(모든 월드컵)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 해당 월드컵 진행 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 모든 영화 월드컵에서 우승했는지 여부(맞을 경우 true)
    best_of_best = models.BooleanField(default=False)

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rated_movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)