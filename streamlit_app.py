'''
Bibliothéques pour la manipulation des dataFrame et les chart
'''
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import csv







#tableau de bord 

st.sidebar.header("Paramètres")
st.sidebar.info("Veuilez Selectionnez l'année et le pays que vous voulez savoir le meilleur buteur des coordonnées selectionné")
st.title("La Coupe Du Monde De Football")
st.header("Description")
st.write('''Les passagers sur le bateau Titanic sont à représenter par 3 classes (hommes, femmes,
enfants). Sur chaque compartiment (Affaire, busines, troisième classe, membres
d’équipage). On veut représenter les survivants et les noyés par classe (H, F, E) et par
compartiment. Donnez la représentation visuelle adéquate.''')



#ouvrir un fichier csv
data = pd.read_csv('titanic-data.csv')



#supprimer les lignes avec des informations manquante (vide)
data = data.dropna(axis=0)






    




