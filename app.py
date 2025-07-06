import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('dataset/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # si el botón es presionado
  st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
  
  fig = px.histogram(car_data, x="odometer")

  st.plotly_chart(fig, use_container_width=True) # mostrar el histograma