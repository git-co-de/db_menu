#from functions import load_csv, clean_price, save_csv, add_date
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Funktion, die dann in "main.py" importiert wird
def show_home():
    # DataFrame erstellen und einlesen aus csv
    df_food = pd.read_csv("food_all_cleaned.csv")
    df_bev = pd.read_csv("beverages_concat.csv")

    
    st.title("Bordgastronomie der Deutschen Bahn")
    st.write("Auf dieser Seit findest du allgemeine Informationen und Statistiken zum Speise- und Getränkeangebot der Deutschen Bahn.")
    st.write("Navigiere gerne über die Reiter oben in der Leiste, um Informationen zu den Speisen und Getränken zu erhalten.")

    st.divider()
    st.header(f"Allgemeine Statistiken zum gastronomischen Angebot seit {df_food["date"].min()}:")

    df_statistics = pd.DataFrame(
        {
            "Produkte gesamt": [df_food["name"].nunique(), df_bev["name"].nunique()],
            "Produkte aktuell": [df_food[df_food["date"] == df_food["date"].max()]["name"].nunique(),
                                 df_bev[df_bev["date"] == df_bev["date"].max()]["name"].nunique()],
            "Anzahl Kategorien": [df_food["category"].nunique(), df_bev["category"].nunique()],
            "Vegane Produkte": [df_food[df_food["vegan"] == "Vegan"]["name"].nunique(),
                                df_bev[df_bev["vegan"] == "Vegan"]["name"].nunique()],
            "Vegetarische Produkte": [df_food[df_food["vegetaric"] == "Vegetarisch"]["name"].nunique(),
                                      df_bev[df_bev["vegetaric"] == "Vegetarisch"]["name"].nunique()],
            "Bio-Produkte": [df_food[df_food["bio"] == "Bio"]["name"].nunique(), 
                             df_bev[df_bev["bio"] == "bio"]["name"].nunique()]
        },
    index = ["Speisen", "Getränke"]
    )
    st.write(df_statistics)

    st.markdown(
        '<a href="https://db-bordgastronomie.de/digitalespeisekarte" target="_blank">Klicke HIER um zur aktuellen Speisekarte zu gelangen</a>',
        unsafe_allow_html=True
    )

