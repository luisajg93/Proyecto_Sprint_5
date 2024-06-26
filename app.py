# importar las librerías
import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.title('Creación de gráficos con data de anuncios vehiculares') # título de la app

st.write('Esta aplicación permite visualizar gráficos con información de anuncios de autos')

# espacio después de la descripción
st.markdown("<br>", unsafe_allow_html=True)  # Línea vacía usando HTML

st.header('Modelos de autos anunciados')
        
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma de los módelos de autos anunciados')
    
    # crear un histograma
    fig = px.histogram(car_data, x="model")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)  # Línea vacía usando HTML

st.header('Precios de autos anunciados')

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión de los precios de autos anunciados')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)  # Línea vacía usando HTML

st.header('Lista de variables para graficar')

# selecciona la columna del dataframe para crear el histograma
column = st.selectbox('Selecciona una variable de interés de la lista desplegable', car_data.columns)

st.write("") # línea vacía para espaciar

# mensaje para selección de casilla
st.write('Selecciona el tipo de gráfico a visualizar')

# checkbox para crear el histograma
if st.checkbox('Histograma'): # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Histograma para {column}')

    # crear un histograma
    fig = px.histogram(car_data, x=column)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# checkbox para crear gráfico de dispersión
if st.checkbox('Gráfico de dispersión'): # al hacer clic en el botón
    # escribir un mensaje
    st.write(f'Gráfico de dispersión para {column}')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x=column)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)