import streamlit as st
import pandas as pd

st.title("Exercício 2: Filtro Dinâmico em Tabela")

# Dados de exemplo
data = {
   "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "São Paulo", "Rio de Janeiro"],
   "Categoria": ["A", "B", "A", "C", "B", "C", "A"],
   "Valor": [100, 150, 200, 250, 300, 120, 500]
}
df = pd.DataFrame(data)
st.subheader("Tabela de Dados")
st.dataframe(df)

st.subheader("Filtros")
cidades = st.multiselect("Selecione as cidades", options=df["Cidade"].unique(), default=df["Cidade"].unique())
categorias = st.multiselect("Selecione as categorias", options=df["Categoria"].unique(), default=df["Categoria"].unique())
valor_min, valor_max = st.slider("Selecione o intervalo de valores", 
                                 min_value=int(df["Valor"].min()), 
                                 max_value=int(df["Valor"].max()), 
                                 value=(int(df["Valor"].min()), int(df["Valor"].max())))
df_filtrado = df[(df["Cidade"].isin(cidades)) & 
                 (df["Categoria"].isin(categorias)) & 
                 (df["Valor"] >= valor_min) & (df["Valor"] <= valor_max)]
st.subheader("Dados Filtrados")
st.dataframe(df_filtrado)
