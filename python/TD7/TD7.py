import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# exercie1
# Q 1



covid = pd.read_csv('D:/prog/programming-tds/python/TD7/covid-hospit-2023-03-31-18h01.csv')


print("\ Dernières lignes du tableau:")
print(covid.tail())


print(" Premieres lignes du tableau:")
print(covid.head())


print(" Types de données de chaque colonne:")
print(covid.dtypes)


# Q 2

covid['Jour'].dtype
covid['Jour'] = pd.to_datetime(covid['Jour'])
covid['Jour'].dtype

# Q 3
covid_agg = covid.drop(['dep', 'sexe'], axis=1).copy()
agg_par_Jour = covid_agg.groupby('Jour').sum()

print(agg_par_Jour.tail())
print(agg_par_Jour.columns.tolist())


# Q 3

plt.figure(figsize=(14, 7))
agg_par_Jour.plot(title="Evolution des hospitalisations par Jour", logy=True)
plt.xlabel("Date")
plt.ylabel("Nombre (échelle log)")
plt.legend(loc='best', fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('covid_evolution_log.png', dpi=150, bbox_inches='tight')
print("Graphique sauvegarde : 'covid_evolution_log.png'")
plt.show()

# Q 5
VOTRE_SEXE = 1  # 1 = homme, 2 = femme

sexe_label = "Homme" if VOTRE_SEXE == 1 else "Femme"
print(f"\n👤 Analyse pour: {sexe_label} (sexe={VOTRE_SEXE})")


covid_filtre = covid[covid['sexe'] == VOTRE_SEXE].copy()
covid_sexe_agg = covid_filtre.drop(['dep', 'sexe'], axis=1)
covid_sexe = covid_sexe_agg.groupby('Jour').sum()

print(covid_sexe.tail())

plt.figure(figsize=(14, 7))
covid_sexe.plot(title=f"Evolution des hospitalisations - {sexe_label}", logy=True)
plt.xlabel("Date")
plt.ylabel("Nombre (échelle log)")
plt.legend(loc='best', fontsize=8)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'covid_evolution_{sexe_label.lower()}.png', dpi=150, bbox_inches='tight')
print(f"Graphique sauvegarde:'covid_evolution_{sexe_label.lower()}.png'")
plt.show()

# exercie 2

# Question 1
temp = pd.read_csv('temperature.csv')

# Question 2
print(temp.describe())

# Question 3
temp_filtre = temp[temp['Month'].isin([3, 6, 9, 12])]
# makayn col dyal region kayn gha d city
temp_filtre = temp_filtre[temp_filtre['City'] != 'Auckland'] 


print(temp_filtre.head())

# Question 4
mois_cols = ['March', 'June', 'September', 'December']
data_numpy = temp_filtre[mois_cols].values

moyennes = np.mean(data_numpy, axis=0)
print("Moyennes:", moyennes)

matrice_corr = np.corrcoef(data_numpy.T)
print("Matrice de corrélation:")
print(matrice_corr)


