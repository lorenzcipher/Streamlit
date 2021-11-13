import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image







#tableau de bord 

st.sidebar.header("Paramètres")
st.title("Titanic Visualisation")
st.header("Description")
st.write("Les passagers sur le bateau Titanic sont à représenter par 3 classes (hommes, femmes,enfants). Sur chaque compartiment (Affaire, busines, troisième classe, membresd’équipage). On veut représenter les survivants et les noyés par classe (H, F, E) et parcompartiment. Donnez la représentation visuelle adéquate.")

st.sidebar.info("Boite à selection des analyses")


#ouvrir un fichier csv
data = pd.read_csv('titanic-data.csv')



#supprimer les lignes avec des informations manquante (vide)
data = data.dropna(axis=0)






    




