import streamlit as st
import pandas as pd
import requests
import pydeck as pdk

st.title("Exercício 10: Integração com API Externa")
st.write("Digite o nome do país em Inglês")
pais = st.text_input("Nome do país")
if pais:
   url = f"https://restcountries.com/v3.1/name/{pais}"
   try:
      response = requests.get(url)
      if response.status_code == 200:
         dados = response.json()
         if isinstance(dados, list) and len(dados) > 0:
            info = dados[0]
            nome_comum = info.get("name", {}).get("common", "N/A")
            capital = info.get("capital", ["N/A"])[0]
            regiao = info.get("region", "N/A")
            populacao = info.get("population", "N/A")
            st.write(f"Nome: {nome_comum}")
            st.write(f"Capital: {capital}")
            st.write(f"Continente: {regiao}")
            st.write(f"População: {populacao}")
            latlng = info.get("latlng", None)
            if latlng and len(latlng) == 2:
               # criando um DataFrame
               df_map = pd.DataFrame({"lat": [latlng[0]], "lon": [latlng[1]]})
               view_state = pdk.ViewState(
                  latitude=latlng[0],
                  longitude=latlng[1],
                  zoom=3, 
                  pitch=0
               )
               layer = pdk.Layer(
                  "ScatterplotLayer",
                  data=df_map,
                  get_position='[lon, lat]',
                  get_color='[255, 0, 0, 160]',
                  get_radius=50000,
               )
               deck = pdk.Deck(
                  map_style="mapbox://styles/mapbox/light-v9",
                  initial_view_state=view_state,
                  layers=[layer],
               )
               st.pydeck_chart(deck)
            else:
               st.error("Dados de localização não disponíveis.")
         else:
               st.error("Erro ao consultar a API.")
      else:
         st.error("Erro ao consultar a API.")
   except Exception as e:
      st.error("Erro na requisição à API.")
