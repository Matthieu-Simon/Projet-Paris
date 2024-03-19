import requests
import os
dossier_execution = os.path.dirname(os.path.abspath(__file__)) 
def save_data_from_online():
# Lien vers le fichier CSV
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/sanisettesparis/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B"

    # Nom du fichier de sortie
    output_file = dossier_execution + "/sanisettes_paris.csv"
   
    # Effectuer la requête HTTP
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Écrire le contenu de la réponse dans un fichier CSV
        with open(output_file, 'wb') as f:
            f.write(response.content)
        #print("Téléchargement terminé. Fichier enregistré sous le nom :", output_file)
    else:
        pass
        #print("La requête a échoué. Statut code :", response.status_code)


