import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
import seaborn as sns
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregar o dataset e separar apenas as colunas de interesse
movies = pd.read_csv('dataset.csv')
movies = movies[['genres', 'original_title', 'vote_average']]

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

# Obter valores TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])
print(tfidf_matrix.shape)

print("Gênetros: ", tfidf.get_feature_names_out())

print("Matriz esparsa de ID-IDF:")
print(pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out(), index=movies.original_title).sample(10, axis=0))

# Calcular similaridade entre vetores - Similaridade do Cosseno
cosine_sim = cosine_similarity(tfidf_matrix)

cosine_sim_df = pd.DataFrame(cosine_sim, index=movies['original_title'], columns=movies['original_title'])
print("Shape: ", cosine_sim_df.shape)
print(cosine_sim_df.sample(5, axis=1).round(2))

# Função para retornar os filmes mais similares a uma lista de gêneros
# informada pelo usuário
def recommend(i, M, items, k=10):
    # Obter uma lista de índices de filmes mais similares ao perfil alvo
    ix = M.loc[:,i].to_numpy().argpartition(range(-1, -k, -1))
    # Obter uma lista com os filmes mais similares
    closest = M.columns[ix[-1:-(k+2):-1]]
    # Deletar o filme alvo
    closest = closest.drop(i, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

recommendations = recommend('Jurassic Park', cosine_sim_df, movies[['original_title', 'genres']])

print("\nRecomendações:")
print(recommendations)