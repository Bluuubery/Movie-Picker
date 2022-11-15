import requests
import json
from movie_picker.local_settings import TMDB_API_KEY

API_KEY = TMDB_API_KEY


def get_movie_data():
    movie_data = []

    for idx in range(1, 501):
        print(idx)
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-kr&page={idx}"
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            if movie.get('release_date', '') and movie.get('overview', '') and movie.get('poster_path', ''):
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids']
                }

                data = {
                    'pk': movie['id'],
                    'model': 'movies.movie',
                    'fields': fields
                }

                movie_data.append(data)

    with open('movie_data.json', 'w', encoding="utf-8") as make_file:
        json.dump(movie_data, make_file, ensure_ascii=False, indent="\t")


def get_genre_data():
    genre_data = []

    request_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-kr'
    genres = requests.get(request_url).json()
    for genre in genres['genres']:
        fields = {
            'name': genre['name']
        }
        data = {
            'pk': genre['id'],
            'model': 'movies.genre',
            'fields': fields
        }
        genre_data.append(data)

    with open('genre_data.json', 'w', encoding="utf-8") as make_file:
        json.dump(genre_data, make_file, ensure_ascii=False, indent="\t")

get_movie_data()
print('got movie_data')
# get_genre_data()
print('got genre_data')
