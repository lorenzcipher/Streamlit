'''
Bibliothéques pour la manipulation des dataFrame et les chart
'''
import streamlit as st
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 







#tableau de bord 

st.sidebar.header("Paramètres")
st.sidebar.info("Veuilez Selectionnez l'année et le pays que vous voulez savoir le meilleur buteur des coordonnées selectionné")
st.title("La Coupe Du Monde De Football")
st.header("Description")
st.write("Il s’agit de représenter pour la coupe du monde de football (2014, ..., 1954) le meilleur buteur et son pays d’origine ayant le record des buts inscrits par le même joueur en indiquant le nombre de buts inscrits et les éditions dans laquelle il les a inscrit. Les données sont dans le fichier csv suivant.Donnez la représentation visuelle adéquate.")




#ouvrir un fichier csv
data = pd.read_csv('titanic-data.csv')

#filtrer la dataframe
data = data.drop(['Name','SibSp','Parch','Ticket','Fare','Cabin','Embarked'],axis=1)

#supprimer les lignes avec des informations manquante (vide)
data = data.dropna(axis=0)

#groupe by class
st.write(data.groupby(['Sex','Pclass']).mean())

st.write(data[data['Age'] < 18].groupby(['Sex','Pclass']).mean())




st.write(data)
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.write(chart_data)
st.bar_chart(chart_data)    
    




