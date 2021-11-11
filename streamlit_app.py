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

#importer data
df = pd.read_csv("data.csv", sep=",", encoding="utf-8")

#list par pays 
pays = list(set(df["Country"]))
ranking_pays = st.sidebar.selectbox('Ranking par pays ',pays)





#marque du filtrage
df_mask=df['Country']==ranking_pays

#data filter dépend le pays
filtered_df = df[df_mask]

#max des buteurs
max_total = max(df['Total'])

#supprimer les colonnes commune
del filtered_df['Country']
del filtered_df['Total']



#récupérer les années à partir des columns
Col = filtered_df.columns.values
Col = Col[1:-1]




z = pd.DataFrame(
    Col,
    columns=list(range(max_total)))

st.write(z)

'''

c = alt.Chart(z).mark_circle().encode(
   x='a', y='b', size='a', color='b', tooltip=['a', 'b'])

st.altair_chart(c, use_container_width=True)

'''





    
    




