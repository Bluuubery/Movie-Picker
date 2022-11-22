from rest_framework import serializers
# from django.contrib.auth import get_user_model

from .models import User
from movies.models import *
from movies.serializers import MovieSerializer

# 원하는 필드만 출력할 수 있도록 하는 시리얼라이저 클래스입니다.
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)



# class MovieSerializer(DynamicFieldsModelSerializer):
    
#     class Meta:
#         model = Movie
#         fields = '__all__'


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# dj-rest-auth의 USER_DETAILS_SERIALIZER를 대체하기 위한 custom serializer(프로필 수정 용도)
class CustomUserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'avatar')



class BestMovieSerializer(DynamicFieldsModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True, fields=['id', 'username', 'avatar'])

    class Meta:
        model = BestMovie
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class ProfileSerializer(DynamicFieldsModelSerializer):
    best_movies = BestMovieSerializer(many=True, fields=['id', 'movie', 'created_at', 'best_of_best'])
    watched_movies = MovieSerializer(many=True)
    to_watch_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


# 유저 검색용 시리얼라이저       

class UserSearchBestMovieSerializer(DynamicFieldsModelSerializer):
    movie = MovieSerializer(read_only=True, fields=['id', 'title'])

    class Meta:
        model = BestMovie
        fields = '__all__'



class ProfileSearchSerializer(DynamicFieldsModelSerializer):
    best_movies = BestMovieSerializer(many=True, fields=['id', 'movie', 'created_at', 'best_of_best'])
    watched_movies = MovieSerializer(many=True)
    to_watch_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'