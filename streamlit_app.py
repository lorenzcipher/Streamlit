import streamlit as st
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 









st.sidebar.header("Paramètres")
st.sidebar.info("Veuilez Selectionnez l'année et le pays que vous voulez savoir le meilleur buteur des coordonnées selectionné")
st.title("La Coupe Du Monde De Football")
st.header("Description")
st.write("Il s’agit de représenter pour la coupe du monde de football (2014, ..., 1954) le meilleur buteur et son pays d’origine ayant le record des buts inscrits par le même joueur en indiquant le nombre de buts inscrits et les éditions dans laquelle il les a inscrit. Les données sont dans le fichier csv suivant.Donnez la représentation visuelle adéquate.")

df = pd.read_csv("data.csv", sep=",", encoding="utf-8")

pays = list(df["Country"])

ranking_pays = st.sidebar.selectbox('Ranking par pays ', pays)

tmp = df[df.Country == ranking_pays]


totale = list(tmp["Total"])
del tmp["Total"]
st.write(tmp)







    
    




