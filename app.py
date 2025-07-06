from io import StringIO
import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title('Análisis de datos de anuncios de venta de coches')
# Descripción de la aplicación
st.write('Esta aplicación permite analizar un conjunto de datos de anuncios de venta de coches en Estados Unidos. Puedes explorar los datos y visualizar un histograma y de dispersión de los odómetros de los coches.')  

car_data = pd.read_csv('dataset/vehicles_us.csv') 
# Cargar el conjunto de datos de anuncios de venta de coches

# Inicializar el estado de sesión para controlar la visibilidad
if 'show_hist' not in st.session_state:
    st.session_state.show_hist = False

if 'show_scatter' not in st.session_state:
    st.session_state.show_scatter = False

# Botón que alterna el estado de visibilidad del histograma
hist_button = st.button('Mostrar/Ocultar Histograma')

# Botón para mostrar/ocultar el histograma
if hist_button:
    st.session_state.show_hist = not st.session_state.show_hist

# Mostrar el histograma si el estado es verdadero
if st.session_state.show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)  # mostrar el histograma

# Botón que alterna el estado de visibilidad del gráfico de dispersión
scatter_button = st.button('Mostrar/Ocultar Gráfico de Dispersión')

# Botón para mostrar/ocultar el gráfico de dispersión
if scatter_button:
    st.session_state.show_scatter = not st.session_state.show_scatter

# Mostrar el gráfico de dispersión si el estado es verdadero
if st.session_state.show_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)  # mostrar el gráfico de dispersión


# Mostrar el número de filas y columnas del conjunto de datos
st.write(f'El conjunto de datos contiene {car_data.shape[0]} filas y {car_data.shape[1]} columnas.')

# Mostrar información del conjunto de datos
buffer = StringIO()
car_data.info(buf=buffer)
info_str = buffer.getvalue()

with st.expander('Información del conjunto de datos'):
    st.text(info_str)  # mostrar información del conjunto de datos

# Mostrar las primeras filas del conjunto de datos
st.write('Primeras filas del conjunto de datos:')
st.dataframe(car_data.head())  # mostrar las primeras filas del conjunto de datos

# Mostrar estadísticas descriptivas del conjunto de datos
st.write('Estadísticas descriptivas del conjunto de datos:')
st.write(car_data.describe())  # mostrar estadísticas descriptivas del conjunto de datos

