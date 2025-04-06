import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exercício 7: Sistema de Recomendação Simples")

st.write("Selecione suas preferências:")
generos = st.multiselect(
   "Escolha gêneros de filmes", 
   options=["Ação", "Comédia", "Drama", "Ficção Científica", "Romance"]
)

# Conjunto de dados 
recomendacoes = {
    "Ação": [
      {"Filme": "Mad Max: Estrada da Fúria", "Pontuação": 9},
      {"Filme": "John Wick", "Pontuação": 8.5},
      {"Filme": "Gladiador", "Pontuação": 8},
      {"Filme": "Velozes e Furiosos", "Pontuação": 10},
      {"Filme": "Missão Impossível", "Pontuação": 8.2},
      {"Filme": "007 - Operação Skyfall", "Pontuação": 8.0}
    ],
    "Comédia": [
      {"Filme": "A Grande Aposta", "Pontuação": 8},
      {"Filme": "Se Beber, Não Case", "Pontuação": 7},
      {"Filme": "Missão Madrinha de Casamento", "Pontuação": 7.5},
      {"Filme": "O Virgem de 40 Anos", "Pontuação": 8.2},
      {"Filme": "Superbad - É Hoje", "Pontuação": 7.8},
      {"Filme": "As Branquelas", "Pontuação": 9}
    ],
    "Drama": [
      {"Filme": "Forrest Gump", "Pontuação": 9},
      {"Filme": "Um Sonho de Liberdade", "Pontuação": 9.3},
      {"Filme": "Clube da Luta", "Pontuação": 8.9},
      {"Filme": "Cidadão Kane", "Pontuação": 8.7},
      {"Filme": "O Poderoso Chefão", "Pontuação": 9.2},
      {"Filme": "Beleza Americana", "Pontuação": 8.0}
    ],
    "Ficção Científica": [
      {"Filme": "Interstellar", "Pontuação": 10},
      {"Filme": "Blade Runner 2049", "Pontuação": 9},
      {"Filme": "Matrix", "Pontuação": 9.8},
      {"Filme": "A Origem", "Pontuação": 8.8},
      {"Filme": "2001: Uma Odisseia no Espaço", "Pontuação": 9.0},
      {"Filme": "Ex Machina", "Pontuação": 8.5}
    ],
    "Romance": [
      {"Filme": "Diário de uma Paixão", "Pontuação": 8.9},
      {"Filme": "Antes do Amanhecer", "Pontuação": 8},
      {"Filme": "La La Land", "Pontuação": 8.3},
      {"Filme": "Orgulho e Preconceito", "Pontuação": 10},
      {"Filme": "Me Chame Pelo Seu Nome", "Pontuação": 8.2},
      {"Filme": "Titanic", "Pontuação": 9.9}
    ]
}

lista_recomendacoes = []
scores = []
genero_list = []

for genero in generos:
   if genero in recomendacoes:
      for rec in recomendacoes[genero]:
         lista_recomendacoes.append(rec["Filme"])
         scores.append(rec["Pontuação"])
         genero_list.append(genero)

if lista_recomendacoes:
   st.subheader("Recomendações para você:")
   for filme in lista_recomendacoes: #exibir as recomendações na tela
      st.write(filme)
      df_recomendacoes = pd.DataFrame({ #cria um DataFrame
         "Gênero": genero_list,
         "Filme": lista_recomendacoes,
         "Pontuação": scores
    })
   fig = px.bar( # mostra o grafico de barras com a pontuação dos filmes
      df_recomendacoes, 
      x="Filme", 
      y="Pontuação", 
      color="Gênero", 
      title="Pontuação das Recomendações",
      text="Pontuação"
   )
   st.plotly_chart(fig)
else:
   st.info("Selecione pelo menos um gênero para receber recomendações.")
