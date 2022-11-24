from rest_framework import serializers
from .models import Review

from movies.serializers import MovieSerializer

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


class ReviewSerializer(DynamicFieldsModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    avatar = serializers.ImageField(source='author.avatar', read_only=True)
    movie = MovieSerializer(fields = ['title', 'poster_path', 'backdrop_path'])

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('author', 'movie')


class ReviewCreateSerializer(DynamicFieldsModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('author', 'movie')