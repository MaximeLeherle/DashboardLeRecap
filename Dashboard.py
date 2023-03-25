import streamlit as st
import pandas as pd
import itertools
from collections import Counter

# Lecture du fichier CSV
df = pd.read_csv("data/datav3.csv", sep=";")

# Création d'une fonction qui récupère le nom ou les noms des joueurs ayant le score maximal
def get_winners(row):
    scores = row[2:].fillna(0)
    max_score = scores.max()
    winners = [col for col in row.index if row[col] == max_score]
    return "/".join(winners)

# Application de la fonction sur chaque ligne du DataFrame pour créer la colonne "Victoire"
df["Victoire"] = df.apply(get_winners, axis=1)

# On récupère la liste des noms de colonnes à partir du dataframe de départ
players = list(df.columns[2:-1])
last_col = df.iloc[:, -1].tolist()
last_col = [elem.split("/") for elem in last_col]
last_col = list(itertools.chain(*last_col))
last_col_dict = dict(Counter(last_col))

print(last_col_dict)

# On initialise un dictionnaire vide pour stocker les données des joueurs
data_player = {}

# Pour chaque joueur, on calcule les différentes propriétés demandées
for player in players:

    max_score = df[player].max()
    min_score = df[player].min()
    total_score = df[player].sum()
    total_victoires = last_col_dict[player] if player in last_col_dict else 0
    nb_participations = len(df[df[player].notna()])
    victoire_per_100 = (total_victoires / nb_participations) * 100
    mean_score = df[player].mean()

    # On stocke les données dans le dictionnaire data_player
    data_player[player] = {
        'Score max': max_score,
        'Score min': min_score,
        'Total score': total_score,
        'Total victoires': total_victoires,
        'Nombre de participations': nb_participations,
        '% de victoire': victoire_per_100,
        'Score moyen': mean_score,
    }

# On crée un nouveau dataframe à partir du dictionnaire de données data_player
df_player = pd.DataFrame(data_player).T.round(2)

# Affichage du titre
st.title("Bilan du quizz de JiJi 2023")

# Affichage du DataFrame
st.write(df)

st.write(df_player)
