import streamlit as st
import requests
import pandas as pd
import random
import numpy as np
from back import recommend_by_genres

# Título da aplicação
st.title("Movie Recommendation")

# Introdução e instruções
st.write("Welcome to our Application! Choose the movie genres which you like the most, in the end we´re going to recommend you some movies based in your tastes!")


st.header("Movie Genres")

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


if st.button("Get Your Movies!"):

  st.write(recommend_by_genres(selected_genres))

