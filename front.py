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
    "Action": False,
    "Adventure": False,
    "Fantasy": False,
    "Science Fiction": False,
    "Crime": False,
    "Drama": False,
    "Thriller": False,
    "Animation": False,
    "Family": False,
    "Romance": False,
    "Horror": False,
    "Mystery": False,
    "History": False,
    "War": False,
    "Comedy": False,
    "Western": False,
    "Music": False
}

for genre in genres_dict:
    genres_dict[genre] = st.checkbox(genre)

selected_genres = [genre for genre, state in genres_dict.items() if state]


if st.button("Obter Recomendações"):

  st.write(recommend_by_genres(selected_genres))

