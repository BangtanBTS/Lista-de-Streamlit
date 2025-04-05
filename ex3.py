import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Exercício 3: Simulador de Investimento")

valor_inicial = st.number_input("Valor Inicial", min_value=0.0, value=100.0, step=10.0)
taxa = st.slider("Taxa de Juros Anual (%)", min_value=0.0, max_value=20.0, value=14.25, step=0.01)
periodo = st.selectbox("Período (anos)", options=list(range(1, 50)), index=4)

anos = list(range(0, periodo + 1))
montantes = [valor_inicial * ((1 + taxa / 100) ** ano) for ano in anos]
st.subheader("Simulação do Investimento")
st.write("Valor Final após", periodo, "anos: R$", round(montantes[-1], 2))
df_simulacao = pd.DataFrame({"Ano": anos, "Montante": montantes})
fig = px.line(df_simulacao, x="Ano", y="Montante", markers=True,
              title="Crescimento do Investimento ao Longo do Tempo")
st.plotly_chart(fig)
