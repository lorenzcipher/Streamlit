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

pays = ['Tous les pays','Germany', 'Brazil','France','Hungray','UK','Argentina','Peru','Poland']
ranking_pays = st.sidebar.selectbox('Ranking par pays ', pays)
# let's ask the user which column should be used as Index
if ranking_pays in pays:   
    choix_pays = ranking_pays

    
    
st.write(annee)




