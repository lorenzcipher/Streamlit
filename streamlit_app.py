import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#import plotly_express as px







#tableau de bord 

st.sidebar.header("Paramètres")
st.title("Titanic Visualisation")
st.header("Description")
st.write("Les passagers sur le bateau Titanic sont à représenter par 3 classes (hommes, femmes,enfants). Sur chaque compartiment (Affaire, busines, troisième classe, membresd’équipage). On veut représenter les survivants et les noyés par classe (H, F, E) et parcompartiment. Donnez la représentation visuelle adéquate.")

image = Image.open('titanic.jpg')
st.image(image, caption='Titanic')

st.sidebar.write('''Boite à clées :
-Survivant (1:oui 0:Non) 
-Pclass (Passenger Class): 1,2,3 
-Sex: Male, Female\n-Embarked (Port of Embarkation): C = Cherbourg, Q = Queenstown, S = Southampto''')

options = st.sidebar.multiselect(
     'Choisi Deux paramétres à comparais ',
     ["Survived", 'Pclass', 'Sex', 'Embarked'])



#ouvrir un fichier csv
data = pd.read_csv('titanic-data.csv')




#supprimer les lignes avec des informations manquante (vide)
data = data.dropna(axis=0)

#fonction avec deux paramétres pour créer une dataframe et faire la relation entre les deux paramétres 
def make_pivot (param1, param2):
    df_slice = data[[param1, param2, 'PassengerId']]
    slice_pivot = df_slice.pivot_table(index=[param1], columns=[param2],aggfunc=np.size, fill_value=0)
    
     #fig1 = px.bar(slice_pivot, x=str(options[0]), y=str(options[1]), color='PassengerId', height=400)
     #p_chart = st.write(fig1)   
    #p_chart = st.bar_chart(slice_pivot)
    #for p in p_chart.patches:
    #    p_chart.annotate(str(p.get_height()), (p.get_x() * 1.05, p.get_height() * 1.01))
    
    return slice_pivot
    #return p_chart

if not options or len(options)<2:
     st.warning('Selectionne les deux parametres à comparer')
else:
     st.write(make_pivot(options[0],options[1]))
    

 




