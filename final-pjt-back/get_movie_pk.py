import json

with open('final-pjt-back/movies/fixtures/new_movie_data.json', 'r', encoding='UTF-8') as f:
    movie_data = json.load(f)



movie_pk_list = []
for movie in movie_data:
    movie_pk_list.append(movie['pk'])

print(sorted(movie_pk_list))

