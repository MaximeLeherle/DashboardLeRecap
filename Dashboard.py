import streamlit as st
import pandas as pd

# Lecture du fichier CSV
stat_df = pd.read_csv("datav3.csv", sep=";")

# Création d'une fonction qui récupère le nom ou les noms des joueurs ayant le score maximal
def get_winners(row):
    scores = row[2:].fillna(0)
    print(type(scores))
    max_score = max(scores)
    print(max_score)
    winners = [col for col in row.index if row[col] == max_score]
    print("This is the winner :", winners)
    return "/".join(winners)

# Application de la fonction sur chaque ligne du DataFrame pour créer la colonne "Victoire"
stat_df["Victoire"] = stat_df.apply(get_winners, axis=1)

# Affichage du titre
st.title("Bilan du quizz de JiJi 2023")

# Affichage du DataFrame
st.write(stat_df)