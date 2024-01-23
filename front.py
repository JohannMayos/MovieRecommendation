import streamlit as st
import requests
import pandas as pd
import random
import numpy as np
from back import recommend_by_genres

# Título da aplicação
st.title("Avaliação de Filmes")

# Introdução e instruções
st.write("Bem-vindo à nossa aplicação, nela você indicará quais gêneros de filme mais gosta e indicaremos os melhores dessa categoria para você")


st.header("Gêneros de Filmes")

genres_dict = {
    "Ação": False,
    "Aventura": False,
    "Fantasia": False,
    "Ficção Científica": False,
    "Crime": False,
    "Drama": False,
    "Thriller": False,
    "Animação": False,
    "Família": False,
    "Romance": False,
    "Horror": False,
    "Mistério": False,
    "História": False,
    "Guerra": False,
    "Comédia": False,
    "Velho Oeste": False,
    "Música": False
}

for genre in genres_dict:
    genres_dict[genre] = st.checkbox(genre)


selected_genres = [genre for genre, state in genres_dict.items() if state]



if st.button("Obter Recomendações"):

  st.write(recommend_by_genres(selected_genres))

