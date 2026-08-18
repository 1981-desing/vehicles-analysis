import pandas as pd
import plotly_express as px
import streamlit as st
import nbformat as nbf

veiculos_us = pd.read_csv('vehicles_us.csv')
st.header('venda de veiculos')
hist_button = st.button('mostrar histograma')
if hist_button:
    st.write('criando um histograma')
    fig = px.histogram(veiculos_us, x='odometer')
    st.plotly_chart(fig)

st.write('análise de dados')
scatter_button = st.button('mostrar scatter_plotly')
if scatter_button:
    fig = px.scatter(veiculos_us, x='odometer', y='price')
    st.plotly_chart(fig)
