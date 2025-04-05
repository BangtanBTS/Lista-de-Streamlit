import streamlit as st
import pandas as pd

st.title("Exercício 4: Mapa Interativo com Dados Geográficos")

# Dados de exemplo
data = {
   "Nome": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"],
   "Latitude": [-23.5505, -22.9068, -19.9167, -25.4284, -30.0346],
   "Longitude": [-46.6333, -43.1729, -43.9345, -49.2733, -51.2177],
   "Categoria": ["Cidade Grande", "Cidade Grande", "Cidade Média", "Cidade Média", "Cidade Grande"]
}
df = pd.DataFrame(data)

categoria_selecionada = st.selectbox("Selecione a categoria", options=df["Categoria"].unique())
df_filtrado = df[df["Categoria"] == categoria_selecionada]

df_mapa = df_filtrado.rename(columns={"Latitude": "latitude", "Longitude": "longitude"})
st.map(df_mapa[["latitude", "longitude"]])

st.write("Mostrando pontos para a categoria:", categoria_selecionada)
