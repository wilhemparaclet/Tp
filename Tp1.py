#importer les librairies

import os
import streamlit as st 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

#Affiche le titre de l'API
st.title("Data App")

# Récupération des fichiers dans le dossier actuel
def file_selector(folder_path='/Tp/File'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Choisir un fichier', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('Vous avez choisi `%s`' % filename)

df = pd.read_csv(filename)
st.write(df)

#Afficher les colonnes de la dataset
st.title("Afficher les colonnes de la dataset")
st.write(df.columns.tolist())

#Afficher la shape de la dataset
st.title("Afficher la shape du dataset")
st.write(df.shape)

#Afficher les types de la dataset
st.title("Afficher les types de la dataset")
st.write(df.dtypes)

#Afficher les statistiques descriptives du dataset
st.title("Afficher les statistiques descriptives du dataset")
st.write(df.describe())

#Afficher les colonnes de la dataset
st.title("Afficher plusieurs type de graphique dans une partie visualisation avec notamment :")

st.write(sns.heatmap(df.corr(),annot=True))
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
showPyplotGlobalUse = False

#Afficher les colonnes de la dataset
st.subheader("Customizable Plot")
all_columns_names = df.columns.tolist()

#Visualisation personnalisable
st.title("Visualisation personnalisable")

type_of_plot = st.selectbox("Selectionner le type de graphique",["area","bar","line","hist","box","kde"])
selected_columns_names = st.multiselect("Selectioner une colonne ",all_columns_names)

if st.button("Affiche le graphique"):
    st.success("Le graphique {} pour {}".format(type_of_plot,selected_columns_names))

if type_of_plot == 'area':
    cust_data = df[selected_columns_names]
    st.area_chart(cust_data)

elif type_of_plot == 'bar':
    cust_data = df[selected_columns_names]
    st.bar_chart(cust_data)

elif type_of_plot == 'line':
    cust_data = df[selected_columns_names]
    st.line_chart(cust_data)

elif type_of_plot:
    cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
    st.write(cust_plot)
    st.pyplot()

if st.button("Merci"):
        st.balloons()
