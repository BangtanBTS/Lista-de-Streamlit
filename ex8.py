import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

def main():
   st.title("Exercício 8: Previsão do Preço do Imóvel (Regressão Linear)")
   
   st.write("Este app utiliza um modelo de Regressão Linear para prever o preço de um imóvel com base no tamanho (m²) e na idade do imóvel.")
   
   # Dados de treinamento
   np.random.seed(42)
   tamanho = np.random.uniform(50, 200, 100)  # tamanho entre 50 e 200 m²
   idade = np.random.uniform(0, 50, 100)       # idade entre 0 e 50 anos
   ruido = np.random.normal(0, 10000, 100)
   # Fórmula criado pela minha cabeça: preço = 2000 * tamanho - 500 * idade + ruído
   preco = 2000 * tamanho - 500 * idade + ruido

   df = pd.DataFrame({
      "tamanho": tamanho,
      "idade": idade,
      "preco": preco
   })
   
   if st.checkbox("Mostrar dados de treinamento"):
      st.write(df)
   
   # Treinamento do Modelo
   X = df[["tamanho", "idade"]]
   y = df["preco"]
   model = LinearRegression()
   model.fit(X, y)
   
   # Entrada do Usuário
   st.subheader("Insira os valores para previsão:")
   tamanho_input = st.number_input("Tamanho do imóvel (m²):", min_value=30.0, max_value=300.0, value=100.0, step=1.0)
   idade_input = st.number_input("Idade do imóvel (anos):", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
   
   # Previsão
   entrada = np.array([[tamanho_input, idade_input]])
   previsao = model.predict(entrada)
   preco_previsto = previsao[0]
   st.write(f"Preço previsto: R$ {preco_previsto:,.2f}")
   
   # Gráfico
   st.subheader("Dispersão 2D com Dados de Treino")
   fig = px.scatter(
      df, 
      x="tamanho", 
      y="preco", 
      color="idade", 
      title="Distribuição do Preço em Função do Tamanho (Colorido por Idade)"
   )
   # Ponto previsto em vermelho
   fig.add_scatter(
      x=[tamanho_input], 
      y=[preco_previsto], 
      mode='markers',
      marker=dict(color='red', size=12),
      name='Imóvel Previsto'
   )
   st.plotly_chart(fig)

if __name__ == '__main__':
   main()
