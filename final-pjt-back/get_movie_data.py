import requests
import json
from movie_picker.local_settings import TMDB_API_KEY

API_KEY = TMDB_API_KEY

# country_list = ['GB', 'US', 'FR', 'CN', 'KR', 'JP', 'IN', 'HK', 'TW', 'NO', 'PE', 'ES', 'DE', 'IT', 'RU', 'AU']

country_dict = {
    'KR': 1,
    'US': 2,
    'GB': 3,
    'FR': 4,
    'CN': 5,
    'JP': 6,
    'IN': 7,
    'HK': 8,
    'TW': 9,
    'NO': 10,
    'PE': 11,
    'ES': 12,
    'DE': 13,
    'IT': 14,
    'RU': 15,
    'AU': 16,
}


def get_movie_data():
    movie_data = []

    for idx in range(1, 501):

        print(idx)

        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={idx}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:

            if movie.get('release_date', '') and movie.get('overview', '') and movie.get('poster_path', ''):

                movie_id = movie['id']
                detail_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR'
                movie_detail = requests.get(detail_url).json()
                
                # genres = []
                # for genre in movie_detail['genres']:
                #     genres.append(genre['name'])

                countries = []
                for country in movie_detail['production_countries']:
                    if country['iso_3166_1'] in country_dict.keys():
                        countries.append(country_dict[country['iso_3166_1']])
                    elif 17 not in countries:
                        countries.append(17)

                
                fields = {
                    # 'movie_id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_count': movie['vote_count'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'countries': countries
                }

                data = {
                    'pk': movie['id'],
                    'model': 'movies.movie',
                    'fields': fields
                }

                movie_data.append(data)

    with open('new_movie_data.json', 'w', encoding="utf-8") as make_file:
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
# print('got genre_data')
