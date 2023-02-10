import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from datetime import datetime
import yfinance as yf
yf.pdr_override()

st.sidebar.title('Menu')

# Lista de empresas
empresas = ['PETR4.SA', 'AMER3.SA']
selecao = st.sidebar.selectbox('Selecione a empresa', empresas)

range = st.sidebar.slider('Período de meses', 0,12,1, key='Barra_selecao')
selecao_range = str(range) + 'mo'

# Colunas
col1, col2 = st.columns([0.9,0.1])

imagens = [
    'https://play-lh.googleusercontent.com/95UEdYdWxPFtXWnF-cFTTrn6dYFUl91uDVnST2hr8xy30UYS3eywf3VHWYHSQggae7c=w240-h480-rw',
    'https://seeklogo.com/images/P/Petrobras-logo-03DABEE0AC-seeklogo.com.png'
    ]

#Título
titulo = f'Análise Econômica {str(selecao)}'
col1.title(titulo)

if selecao == 'AMER3.SA':
    col2.image(imagens[0], width=70)
else:
    col2.image(imagens[1], width=70)

#Coletar dados da API do Yahoo!
dados = web.get_data_yahoo(selecao, period=selecao_range)

grafico_candlestick = go.Figure(
    data = [
        go.Candlestick(
            x=dados.index,
            open = dados.Open,
            high = dados.High,
            low = dados.Low,
            close = dados.Close
        )
    ]
)

grafico_candlestick.update_layout(
    xaxis_rangeslider_visible=False,
    title='Análise de ações',
    yaxis_title='Preço'
)

# Mostrar gráfico plotly com o streamlit
st.plotly_chart(grafico_candlestick)

if st.checkbox('Mostrar dados em tabela'):
    st.subheader('Tabela de registros')
    st.write(dados)