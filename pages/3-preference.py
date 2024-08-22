import streamlit as st
import pandas as pd

df =pd.read_csv("Cinephile1.csv")

genre_list = df["genres"].unique().tolist()
selected_genres = st.multiselect("Select Genres", genre_list)

def filter_by_genre(df, Genres):
    return df[df["genres"].isin(Genres)]

filtered_df = filter_by_genre(df, selected_genres)
st.table(filtered_df)
