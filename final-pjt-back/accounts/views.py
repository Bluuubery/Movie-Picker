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


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_profile(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = ProfileSerializer(user, fields=['id', 'username', 'watched_movies', 'to_watch_movies', 'best_movies'])
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def to_watch_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = ProfileSerializer(user, fields=['to_watch_movies'])
    return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['GET'])
def watched_list(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = ProfileSerializer(user, fields=['watched_movies'])
    return Response(serializer.data)



@permission_classes([IsAuthenticated])
@api_view(['POST', 'DELETE'])
def to_watch(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        user.to_watch_movies.add(movie)
    
    elif request.method == 'DELETE':
        user.to_watch_movies.remove(movie)

    serializer = ProfileSerializer(user, fields=['to_watch_movies'])
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['POST', 'DELETE'])
def watched(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'POST':
        user.watched_movies.add(movie)
    
    elif request.method == 'DELETE':
        user.watched_movies.remove(movie)

    serializer = ProfileSerializer(user, fields=['watched_movies'])
    return Response(serializer.data)






@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_best(request, user_pk, movie_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = BestMovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, movie=movie)
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_best(request, best_movie_pk):
    best_movie = get_object_or_404(BestMovie, pk=best_movie_pk)
    best_movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def testtest(request):
    bestmovies = get_list_or_404(BestMovie)
    bestmovie = get_object_or_404(BestMovie, pk=1)
    print(bestmovie)
    serializer = BestMovieSerializer(bestmovie)
    return Response(serializer.data)


    