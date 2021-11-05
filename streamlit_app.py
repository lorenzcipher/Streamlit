import streamlit as st
import pandas as pd
from streamlit.logger import get_logger
import numpy as np 
import os



logger = get_logger(__name__)


st.sidebar.header("Paramètres")
st.title("La Coupe Du Monde De Football")
st.header("Description")
st.write("Il s’agit de représenter pour la coupe du monde de football (2014, ..., 1954) le meilleur buteur et son pays d’origine ayant le record des buts inscrits par le même joueur en indiquant le nombre de buts inscrits et les éditions dans laquelle il les a inscrit. Les données sont dans le fichier csv suivant.Donnez la représentation visuelle adéquate.")
Annee = st.sidebar.slider("Année", 1954, 2014, 1954, 4)
raking_pays = st.selectbox('Ranking par pays ', ('Tous les pays','Germany', 'Brazil','France','Hungray','UK','Argentina','Peru','Poland'))
