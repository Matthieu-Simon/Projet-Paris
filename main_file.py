def main():
    pass
if __name__=='__main__':
    main()

#il faut charger la librairie pandas
import os
import pandas
import csv
import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy 
import os
dossier_execution = os.path.dirname(os.path.abspath(__file__)) 
import save_data_from_api as sd
import seaborn as sns

#import gaussian_kde
"%matplotlib inline"
if sd.creation_date_today()==False:
    sd.save_data_from_online()



df=pandas.read_csv(dossier_execution + "/sanisettes_paris.csv",sep=';',header=0)
df = df.drop('URL_FICHE_EQUIPEMENT', axis=1)
df = df.drop('geo_shape', axis=1)
df = df.drop('geo_point_2d', axis=1)
df=df.drop('STATUT', axis=1)

def modifier_valeur(valeur):
    if pandas.isna(valeur):
        return -1
    elif valeur == "Oui":
        return 1
    else:
        return 0
def modifier_horaire(valeur):
    if pandas.isna(valeur):
        return -1
    elif valeur == "Voir fiche équipement":
        return "Non mentionné"
    else:
        return valeur

def split_arr(valeur):
    return int(str(valeur)[-2:])
def arr_tostring(valeur):
    return str(valeur) 
df['ACCES_PMR'] = df['ACCES_PMR'].apply(modifier_valeur)
df['RELAIS_BEBE'] = df['RELAIS_BEBE'].apply(modifier_valeur)
df['ARRONDISSEMENT']=df['ARRONDISSEMENT'].apply(split_arr)
df['HORAIRE']=df['HORAIRE'].apply(modifier_horaire)

#copie de la colonne arrondissement en DataFrame
df_toilette_arrondissement = pandas.DataFrame(df['ARRONDISSEMENT'].sort_values()) # trie les arrondissements
df_toilette_arrondissement['ARRONDISSEMENT']=df_toilette_arrondissement['ARRONDISSEMENT'].apply(arr_tostring)

# compter le nombre de toilettes par arrondissement
nombre_toilette_arrondissement = df_toilette_arrondissement[df_toilette_arrondissement['ARRONDISSEMENT'] == "18"].shape[0] # attention valeur du  ==
print(nombre_toilette_arrondissement)

sns.set_theme(style="darkgrid")

gt_nb_toilette_by_arrondissement = sns.histplot(data=df_toilette_arrondissement, x="ARRONDISSEMENT", discrete=True,  shrink=.5 ) #shrink = largeur de la colonne

# affichage de la valeur max en haut de chaque colonne
gt_nb_toilette_by_arrondissement.bar_label(gt_nb_toilette_by_arrondissement.containers[0], fontsize=10)

#rotation affichage des x
plt.xticks(rotation=30)

plt.title("Toilettes par arrondissement")
plt.xlabel("Arrondissement")
plt.ylabel("Nombre de Toilettes")

plt.show()






