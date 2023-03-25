## Import part

# streamlist for dashboard app
import streamlit as st


# pandas for manage dataframe
import pandas as pd


# intertools and collection to manipulate list
import itertools
from collections import Counter



## Compute Data Part

# Read the data
full_data_df = pd.read_csv("data/datav3.csv", sep=";")


# Function to compte the week winner
def get_winners(row):
    scores = row[2:].fillna(0)
    max_score = scores.max()
    winners = [col for col in row.index if row[col] == max_score]
    return "/".join(winners)

full_data_df["Victoire"] = full_data_df.apply(get_winners, axis=1)


# Get all player names
players = list(full_data_df.columns[2:-1])


# Compute a dict to have number of victry by player
def get_number_of_victory(df):
    last_col = [elem.split("/") for elem in df.iloc[:, -1].tolist()]
    return dict(Counter(list(itertools.chain(*last_col))))

victory_dict = get_number_of_victory(full_data_df)


# Compute the statistical dataframe
def create_statistical_datafrale(df, players):

    data_player = {}

    # Loop on all players
    for player in players:

        max_score = df[player].max()
        min_score = df[player].min()
        total_score = df[player].sum()
        total_victoires = victory_dict[player] if player in victory_dict else 0
        nb_participations = len(df[df[player].notna()])
        victoire_per_100 = (total_victoires / nb_participations) * 100
        mean_score = df[player].mean()

        # store data for the current player
        data_player[player] = {
            'Score max': max_score,
            'Score min': min_score,
            'Total score': total_score,
            'Total victoires': total_victoires,
            'Nombre de participations': nb_participations,
            '% de victoire': victoire_per_100,
            'Score moyen': mean_score,
        }

    # return it with the good format
    return pd.DataFrame(data_player).T.round(2)

df_player = create_statistical_datafrale(full_data_df, players)



## Create the app

# Affichage du titre
st.title("Bilan du quizz de JiJi 2023")


# Affichage des DataFrames
st.write(full_data_df)
st.write(df_player)