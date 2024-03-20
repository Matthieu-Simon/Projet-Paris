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
def df_nbr_arr(MyDataFrame):
    df_nb_ar= MyDataFrame["ARRONDISSEMENT"].value_counts()
    return df_nb_ar
df['ACCES_PMR'] = df['ACCES_PMR'].apply(modifier_valeur)
df['RELAIS_BEBE'] = df['RELAIS_BEBE'].apply(modifier_valeur)
df['ARRONDISSEMENT']=df['ARRONDISSEMENT'].apply(split_arr)
df['HORAIRE']=df['HORAIRE'].apply(modifier_horaire)
 
print(df)
print(df.shape)
 
df_arr=pandas.DataFrame(df['ARRONDISSEMENT'].sort_values())
df_arr['ARRONDISSEMENT']=df_arr['ARRONDISSEMENT'].apply(arr_tostring)
ax=sns.histplot(data=df_arr, x="ARRONDISSEMENT")
ax.bar_label 
print(df_arr)

for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 10), 
                   textcoords = 'offset points')
print(len(ax.patches)) 
for p in ax.patches: 
    print(p.get_height())  
plt.xlabel("Arrondissement ") 
plt.ylabel("Nombre de toilettes")
plt.title("Nombre de toilette par Arrondissement")
#plt.show()
 
 
