
import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
from scipy.optimize import minimize
import scipy.optimize as sco
from scipy.stats import skew, kurtosis

# Funciones de la aplicación
def cargar_datos(tickers, inicio, fin):
    datos = {}
    for ticker in tickers:
        df = yf.download(ticker, start=inicio, end=fin)
        df['Retornos'] = df['Close'].pct_change()
        datos[ticker] = df
    return datos.tail(5)


# --- Configuración de Streamlit ---
st.title("Proyecto de Optimización de Portafolios")

# Crear tabs
tabs = st.tabs(["Selección de activos financieros", "Estadísticas de los ETF's", "Portafolios Óptimos", "Backtesting", "Modelo de Black-Litterman"])




