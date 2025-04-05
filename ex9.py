import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exercício 9: Painel Multi-página com Cache")

subpage = st.sidebar.radio("Selecione a página", 
                           ["Upload e Visualização", "Análise Estatística", "Gráficos Interativos"])
if subpage == "Upload e Visualização":
   st.subheader("Upload e Visualização de Dados")
   uploaded_file = st.file_uploader("Carregue um arquivo CSV", type="csv")
   if uploaded_file is not None:
      try:
         df = pd.read_csv(uploaded_file)
         st.session_state["df"] = df 
         st.dataframe(df)
      except Exception as e:
         st.error("Erro ao carregar o arquivo")
elif subpage == "Análise Estatística":
   st.subheader("Análise Estatística dos Dados")
   if "df" in st.session_state:
      df = st.session_state["df"]
      st.dataframe(df.describe())
   else:
      st.info("Carregue os dados na página de Upload e Visualização.")
elif subpage == "Gráficos Interativos":
   st.subheader("Gráficos Interativos")
   if "df" in st.session_state:
      df = st.session_state["df"]
      numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
      if numeric_cols:
         coluna = st.selectbox("Selecione uma coluna numérica para o gráfico", numeric_cols)
         fig = px.histogram(df, x=coluna, title=f"Histograma de {coluna}")
         st.plotly_chart(fig)
      else:
         st.warning("Não há colunas numéricas para plotar.")
   else:
      st.info("Carregue os dados na página de Upload e Visualização.")
