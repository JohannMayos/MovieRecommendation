import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import seaborn as sns
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''
Gêneros disponíveis:
    ['Action', 'Adventure', 'Fantasy', 'Science Fiction', 'Crime', 'Drama', 'Thriller', 'Animation',
    'Family', 'Romance', 'Horror', 'Mystery', 'History', 'War', 'Comedy', 'Western', 'Music']
'''

def recommend_by_genres(user_profile):

    # Carregar o dataset e separar apenas as colunas de interesse
    movies = pd.read_csv('dataset.csv')
    movies = movies[['genres', 'original_title']]

    # Editar a coluna de gêneros
    genres = []

    for value in movies.genres:
        movie_genres = json.loads(value)
        movie_genres_filtered = []
        for genre in movie_genres:
            movie_genres_filtered.append(genre["name"])
        genres.append('|'.join(movie_genres_filtered))

    movies['genres'] = genres
            
    # Verificar a popularidade de cada gênero retornado
    genre_popularity = (movies.genres.str.split('|').explode().value_counts().sort_values(ascending=False))

    # Criação de uma linha para a tabela de filmes com os gêneros informados pelo usuário
    simulated_movie = {'genres': '|'.join(user_profile), 'original_title': 'FAKE MOVIE'}

    # Adição do "filme" criado na tabela de filmes, para que possa ser processado com todos
    movies = movies._append(simulated_movie, ignore_index=True)

    # Obter valores TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies['genres'])

    # Calcular similaridade entre vetores - Similaridade do Cosseno
    cosine_sim = cosine_similarity(tfidf_matrix)
    cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['original_title'], columns=movies['original_title'])

    # Realizar a busca de filmes similares ao filme criado com os gostos do usuário
    recommendations = recommend_by_movie('FAKE MOVIE', cosine_sim_df, movies[['original_title', 'genres']])

    return recommendations

def recommend_by_movie(i, M, items, k=10):
    # Obter uma lista de índices de filmes mais similares ao perfil alvo
    ix = M.loc[:,i].to_numpy().argpartition(range(-1, -k, -1))
    # Obter uma lista com os filmes mais similares
    closest = M.columns[ix[-1:-(k+2):-1]]
    # Deletar o filme alvo
    closest = closest.drop(i, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

################ Teste de uso do sistema #################

# Gêneros indicados pelo usuário
user_profile = ['Adventure', 'Science Fiction']
recommendations = recommend_by_genres(user_profile)

print("Filmes recomendados para este usuário:")
print(recommendations)