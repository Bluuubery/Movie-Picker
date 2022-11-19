# drf
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import status

# 숏컷
from django.shortcuts import get_object_or_404, get_list_or_404

# 모델/시리얼라이저
from .serializers import *
from .models import *

from django.db.models import Q

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(
        data=serializer.data,
        headers={
            'Access-Control-Allow-Origin': '*'}
        )

@api_view(['GET'])
def movie_list_small(request):
    user = request.user
    movies = get_list_or_404(Movie.objects.order_by('?').exclude(watched_user = user)[:20])
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def search_movie(request, query):
    movies = get_list_or_404(Movie.objects.filter(Q(title__icontains=query)).order_by('-vote_count'))[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

