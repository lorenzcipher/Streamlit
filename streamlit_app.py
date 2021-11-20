import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#import plotly_express as px







#tableau de bord 

st.sidebar.header("Paramètres")
st.title("CGI KONE Sky(scraper) is the limit")
st.header("Description")
st.write('''You and your team are invited to CGI & KONE sky(scraper)-is-the-limit challenge, where you will build unimaginable creative solution to make maintenance services even smarter. This challenge is from serious elevator maintenance service business. Keep reading if you are interested to learn more about a global real-life challenge.Our goal is that a technician is never sent to the field without an actual upcoming maintenance need. Your task is to recognize which service action recommendations are relevant. You are allowed to use any programming language or tool and get creative. In the end only the result matters.

This challenge can be approached in two ways:

1. Treat this as a pure machine learning challenge and build a Best Performing and/or Most Explainable model. This is for you and for your team if:

you have solved machine learning issues in your sleep
you float in the data lake
you speak Python, R or any other programming language
you enjoy to get your hands dirty
2. Or get creative with Out of the Box Thinking. Impress us with a solution we have not even imagined before.''')

image = Image.open('as.jpg')





#ouvrir un fichier csv
data = pd.read_csv('train.csv')
data.replace('0113eba6-6928-461a-b994-35a0b2eb9f4e','*')




st.write(data)
    

 




