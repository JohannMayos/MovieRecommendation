import streamlit as st
import requests
import pandas as pd
import random
import numpy as np

# Configuração da sessão para armazenar variáveis
if 'avaliacoes_anteriores' not in st.session_state:
    st.session_state.avaliacoes_anteriores = []
    st.session_state.numero_avaliacoes = 0
    st.session_state.inputs_nome_jogo = {}
    st.session_state.rec_list = []

# Título da aplicação
st.title("Avaliação de Filmes")

# Introdução e instruções
st.write("Bem-vindo à nossa aplicação, nela você indicará quais gêneros de filme mais gosta e indicaremos os melhores dessa categoria para você")


st.header("Gêneros de Filmes")

checkbox_action = st.checkbox("Ação")
checkbox_adventure = st.checkbox("Aventura")
checkbox_fantasy = st.checkbox("Fantasia")
checkbox_Scifi = st.checkbox("Ficção Científica")
checkbox_crime = st.checkbox("Crime")
checkbox_drama = st.checkbox("Drama")
checkbox_thriller = st.checkbox("Thriller")
checkbox_anim = st.checkbox("Animação")
checkbox_family = st.checkbox("Família")
checkbox_romance = st.checkbox("Romance")
checkbox_horror = st.checkbox("Horror")
checkbox_mistery = st.checkbox("Mistério")
checkbox_history = st.checkbox("História")
checkbox_war = st.checkbox("Guerra")
checkbox_comedy = st.checkbox("Comédia")
checkbox_western = st.checkbox("Velho Oeste")
checkbox_music = st.checkbox("Música")


if st.button("Obter Recomendações"):

  st.write("Recomendações")

