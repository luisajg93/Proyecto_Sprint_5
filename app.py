import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('Creación de gráficos con data de anuncios vehiculares')

st.header('Modelos de autos anunciados')
        
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma de los módelos de autos anunciados')
    
    # crear un histograma
    fig1 = px.histogram(car_data, x="model")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)

st.header('Precios de autos anunciados')

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión de los precios de autos anunciados')
    
    # crear un histograma
    fig2 = px.scatter(car_data, x="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

st.header('Selecciona la información para crear un gráfico')

# selecciona la columna del dataframe para crear el histograma
column = st.selectbox('Selecciona la variable de interés para el histograma', car_data.columns)

# mensaje para selección de casilla
st.write('Selecciona el tipo de gráfico a visualizar')

# checkbox para crear el histograma
if st.checkbox('Histograma'): # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Histograma para {column}')

    # crear un histograma
    fig3 = px.histogram(car_data, x=column)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)

# checkbox para crear gráfico de dispersión
if st.checkbox('Gráfico de dispersión'): # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Gráfico de dispersión para {column}')

    # crear un gráfico de dispersión
    fig3 = px.scatter(car_data, x=column)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)