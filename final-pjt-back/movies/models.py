from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # tmdb에서 genre를 id로 제공해주기 때문에 별도의 중개 필드 작성
    genres = models.ManyToManyField(Genre, related_name='movies')

# 월드컵의 결과로 bestmovie라는 article이 생성되는 느낌으로 이해하면 됩니다.
class BestMovie(models.Model):
    # 월드컵 진행한 유저
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='best_movies')
    # 월드컵 우승한 영화(모든 월드컵)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 해당 월드컵 진행 날짜
    created_at = models.DateTimeField(auto_now_add=True)
    # 모든 영화 월드컵에서 우승했는지 여부(맞을 경우 true)
    best_of_best = models.BooleanField(default=False)