#Import
import pandas as pd
import numpy as np
import streamlit as st

# Charger le fichier CSV dans un dataframe Pandas
df = pd.read_csv("datav3.csv", delimiter=";")

# Création d'une fonction qui récupère le nom du joueur ayant le score maximal
def get_winner(row):
    scores = row[2:]
    max_score = max(scores)
    winners = [col for col in row.index if row[col] == max_score]
    return "/".join(winners)

# Application de la fonction sur chaque ligne du DataFrame pour créer la colonne "Victoire"
df["Victoire"] = df.apply(get_winner, axis=1)

# Affichage du DataFrame avec la nouvelle colonne
print(df)