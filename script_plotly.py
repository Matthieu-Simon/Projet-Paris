import pandas as pd
import plotly.express as px

# Charger les données depuis un fichier CSV
data = pd.read_csv("sanisettes_paris.csv", sep=';')

# Calculer le nombre de toilettes par arrondissement
toilettes_par_arrondissement = data["ARRONDISSEMENT"].value_counts().reset_index()
toilettes_par_arrondissement.columns = ['Arrondissement', 'Nombre de toilettes']

# Créer le graphique camembert interactif avec Plotly Express
fig = px.pie(toilettes_par_arrondissement, values='Nombre de toilettes', names='Arrondissement', title='Répartition du nombre de toilettes par arrondissement à Paris')
fig.show()