import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

st.title("Exercício 6: Análise de Texto com Processamento em Tempo Real")

texto = st.text_area("Insira o texto aqui", height=200)
if texto:
# Contagem de palavras e caracteres
   palavras = texto.split()
   cont_palavras = len(palavras)
   cont_caracteres = len(texto)
   st.write("Número de palavras:", cont_palavras)
   st.write("Número de caracteres:", cont_caracteres)
    
# 5 Palavras mais frequentes
   contagem = Counter(palavras)
   mais_comuns = contagem.most_common(5)
   st.write("5 palavras mais frequentes:")
   for palavra, frequencia in mais_comuns:
      st.write(f"{palavra}: {frequencia}")
    
# Gerar nuvem de palavras
   wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto)
   plt.figure(figsize=(10, 5))
   plt.imshow(wordcloud, interpolation="bilinear")
   plt.axis("off")
   st.pyplot(plt)
