import streamlit as st
from streamlit.logger import get_logger 
import os
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 
from datetime import datetime



logger = get_logger(__name__)


st.sidebar.header("Paramètres")
st.title("La Coupe Du Monde De Football")
st.header("Description")
st.write("Il s’agit de représenter pour la coupe du monde de football (2014, ..., 1954) le meilleur buteur et son pays d’origine ayant le record des buts inscrits par le même joueur en indiquant le nombre de buts inscrits et les éditions dans laquelle il les a inscrit. Les données sont dans le fichier csv suivant.Donnez la représentation visuelle adéquate.")
Annee = st.sidebar.slider("Année", 1954, 2014, 1954, 4)
raking_pays = st.sidebar.selectbox('Ranking par pays ', ('Tous les pays','Germany', 'Brazil','France','Hungray','UK','Argentina','Peru','Poland'))

DATA_URL = ('covid.csv')
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    return data
df = load_data()

# show data on streamlit
st.write(df)

# Filters UI
subset_data = df
country_name_input = st.sidebar.multiselect(
'Country name',
df.groupby('Country/Region').count().reset_index()['Country/Region'].tolist())
# by country name
if len(country_name_input) > 0:
    subset_data = df[df['Country/Region'].isin(country_name_input)]
view rawmulti_select_widget.py hosted with ❤ by GitHub
