import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Creación de gráficos con información de anuncios vehiculares')
        
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma de los módelos de autos anunciados')
    
    # crear un histograma
    fig1 = px.histogram(car_data, x="model")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión de los tipos de autos anunciados')
    
    # crear un histograma
    fig2 = px.histogram(car_data, x="type")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)