# drf
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# 숏컷
from django.shortcuts import get_object_or_404, get_list_or_404

# 모델/시리얼라이저
from .serializers import *
from .models import *
from accounts.serializers import *

from django.contrib.auth import get_user_model

from django.db.models import Q

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(
        data=serializer.data,
        headers={
            'Access-Control-Allow-Origin': '*'}
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list_small(request):
    user = request.user
    movies = get_list_or_404(Movie.objects.order_by('?').filter(Q(vote_count__gt=5000) & Q(vote_avg__gt=7.0)).exclude(watched_user = user)[:20])
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_movie(request, query):
    movies = get_list_or_404(Movie.objects.filter(Q(title__icontains=query) | Q(original_title__icontains=query)).order_by('-vote_count'))[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def picked_users(request, movie_pk):
    best_movies = get_list_or_404(BestMovie.objects.filter(movie=movie_pk).order_by('created_at'))
    serializer = BestMovieSerializer(best_movies, many=True, fields=['user', 'created_at'])

    picked_users = {data['user']['id']: data for data in serializer.data}.values()

    return Response(picked_users)
