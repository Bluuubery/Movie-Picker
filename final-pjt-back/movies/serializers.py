from rest_framework import serializers
from .models import Movie, BestMovie, Genre, Country


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


class GenreSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class CountrySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class MovieSerializer(DynamicFieldsModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    countries = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        # read_only_fields = ('genres',)

# class BestMovieSerializer(DynamicFieldsModelSerializer):

#     username = serializers.CharField(source = 'user.username', read_only=True)
#     movie = MovieSerializer(many=True, read_only=True)

#     class Meta:
#         model = BestMovie
#         fields = '__all__'
#         read_only_fields = ('user', )