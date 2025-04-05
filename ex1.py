import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exercício 1: Dashboard de Análise de Dados com Upload de CSV")

uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")
if uploaded_file is not None:
   try:
      df = pd.read_csv(uploaded_file)
      st.subheader("Pré-visualização dos dados")
      st.dataframe(df.head())
      numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
      if numeric_cols:
         coluna = st.selectbox("Selecione uma coluna numérica", numeric_cols)
         if coluna:
            media = df[coluna].mean()
            mediana = df[coluna].median()
            desvio = df[coluna].std()
            st.write("Média:", media)
            st.write("Mediana:", mediana)
            st.write("Desvio Padrão:", desvio)
            st.subheader("Histograma da coluna " + coluna)
            fig = px.histogram(df, x=coluna)
            st.plotly_chart(fig)
      else:
         st.warning("Não há colunas numéricas no dataset.")
   except Exception as e:
      st.error("Erro ao ler o arquivo CSV.")
