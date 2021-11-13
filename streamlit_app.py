import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image







#tableau de bord 

st.sidebar.header("Paramètres")
st.title("Titanic Visualisation")
st.header("Description")
st.write("Les passagers sur le bateau Titanic sont à représenter par 3 classes (hommes, femmes,enfants). Sur chaque compartiment (Affaire, busines, troisième classe, membresd’équipage). On veut représenter les survivants et les noyés par classe (H, F, E) et parcompartiment. Donnez la représentation visuelle adéquate.")

image = Image.open('titanic.jpg')
st.image(image, caption='Titanic')

st.sidebar.info('''Boite à clées :
                       * survivant (1:oui 0:Non)
                       *Pclass (Passenger Class): 1,2,3
                       *Sex: Male, Female
                       *Embarked (Port of Embarkation): C = Cherbourg, Q = Queenstown, S = Southampto
                       ''')

option = st.sidebar.selectbox('Selectionnez : ',('Relation entre passengers survivants et booking class', 'Relation entre passengers survivants et leurs sex', "Relation between passengers survivant et port d'embarkation"))


#ouvrir un fichier csv
data = pd.read_csv('titanic-data.csv')




#supprimer les lignes avec des informations manquante (vide)
data = data.dropna(axis=0)

#fonction avec deux paramétres pour créer une dataframe et faire la relation entre les deux paramétres 
def make_pivot (param1, param2):
    df_slice = df[[param1, param2, 'PassengerId']]
    slice_pivot = df_slice.pivot_table(index=[param1], columns=[param2],aggfunc=np.size, fill_value=0)
    
    p_chart = slice_pivot.plot.bar()
    for p in p_chart.patches:
        p_chart.annotate(str(p.get_height()), (p.get_x() * 1.05, p.get_height() * 1.01))
    
    return slice_pivot
    return p_chart



    




