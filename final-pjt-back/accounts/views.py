from django.shortcuts import render
from django.contrib.auth import get_user_model


# drf
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# 권한 설정
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# 숏컷
from django.shortcuts import get_object_or_404, get_list_or_404

# 모델/시리얼라이저
from .serializers import *
from .models import *
from movies.models import *
from movies.serializers import *

# 기타 라이브러리
import random


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    # user = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user
    print(request.user.id)
    serializer = ProfileSerializer(user, fields=['id', 'username', 'avatar', 'message', 'watched_movies', 'to_watch_movies', 'best_movies', 'followings', 'followers', ])
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_message(request):
    serializer = UserSerializer(request.user, data=request.data, fields=['id', 'message'])
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def to_watch_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = ProfileSerializer(user, fields=['to_watch_movies'])
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def watched_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = ProfileSerializer(user, fields=['watched_movies'])
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def best_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    best_movies = get_list_or_404(BestMovie, user=user)
    serializer = BestMovieSerializer(best_movies, many=True, fields=['id', 'movie', 'created_at', 'best_of_best'])
    return Response(serializer.data)



@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def to_watch(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        user.to_watch_movies.add(movie)
    
    elif request.method == 'DELETE':
        user.to_watch_movies.remove(movie)

    serializer = ProfileSerializer(user, fields=['to_watch_movies'])
    return Response(serializer.data)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def watched(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        user.watched_movies.add(movie)
    
    elif request.method == 'DELETE':
        user.watched_movies.remove(movie)

    serializer = ProfileSerializer(user, fields=['watched_movies'])
    return Response(serializer.data)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_best(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = BestMovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_best(request, best_movie_pk):
    best_movie = get_object_or_404(BestMovie, pk=best_movie_pk)
    best_movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    me = request.user
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if me != person:
        if me.followings.filter(pk=person.pk).exists():
            me.followings.remove(person)
            following = False
        else:
            me.followings.add(person)
            following = True
        return Response(following)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_feed(request):
    user = request.user
    # 팔로잉
    followings = get_list_or_404(get_user_model().objects.filter(followers=user))
    # 팔로잉의 best_movie
    feed_articles = get_list_or_404(BestMovie.objects.filter(user__in=followings).order_by('-created_at')[:100])
    serializer = BestMovieSerializer(feed_articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_user(request, query):
    users = get_list_or_404(get_user_model().objects.filter(username__icontains=query))
    serializer = ProfileSerializer(users, many=True, fields=['id', 'username', 'message', 'avatar', 'best_movies'])
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_recommendations(request):
    user = request.user
    bestmovies = get_list_or_404(BestMovie, user=user)

    recommended_pk_list = []
    for bestmovie in bestmovies:
        bestmovie_data = BestMovieSerializer(bestmovie, fields=['movie'])
        for movie_pk in bestmovie_data.data['movie']['recommended']:
            recommended_pk_list.append(movie_pk)
    
    random_recommendation_pk_list = random.sample(recommended_pk_list, 20)
    random_recommendations = get_list_or_404(Movie.objects.filter(pk__in=random_recommendation_pk_list))
    serializer = MovieSerializer(random_recommendations, many=True)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def testtest(request):
    pass


