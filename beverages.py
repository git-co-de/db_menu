# from functions import load_csv, clean_price, save_csv, add_date
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Funktion, die dann in "main.py" importiert wird
def show_beverages():
    st.title("Getränkeangebot der Deutschen Bahn")
    st.header("Hier findest du Informationen zum historischen und aktuellen Getränkeangebot der Deutschen Bahn")


    df = pd.read_csv("beverages_concat.csv") 

    with st.expander(f"Klicke HIER, um alle Produkte seit {df["date"].min()} zu sehen"):
        st.dataframe(df)

    st.header("Nun kannst du die Artikel nach der Kategorie und den Artikel selbst filtern")
    col_1, col_2 = st.columns(2)    # Zwei Spalten mit der gleichen Größe erstellen
    with col_1:
        col_11, col_12 = st.columns(2)
        with col_11:
            category_selected = st.selectbox("Wähle eine Kategorie aus", df["category"].sort_values(ascending=True).unique())   # Selectbox zur Auswahl der Kategorie
            filter_category = df[df["category"] == category_selected]
        with col_12:
            article_selected = st.selectbox(f"Wähle einen Artikel der Kategorie **{category_selected}** aus",   # Selectbox zur Auswahl des Artikels
                                            filter_category["name"].sort_values(ascending=True).unique())
            filter_article = df[df["name"] == article_selected]

        with st.expander(f"Klicke HIER, um alle Einträge des Artikels {article_selected} zu sehen"):
            st.dataframe(filter_article)

        category_counts = df["category"].value_counts().reset_index()
        category_counts.columns = ["Kategorie", "Anzahl"]
        # Abbildung mit Anzahl der Produkte je Kategorie erstellen
        fig = px.bar(category_counts,
            x="Kategorie",
            y="Anzahl",
            title="Anzahl der einzigartigen Artikel pro Kategorie")
        st.plotly_chart(fig)
    with col_2:
        st.subheader(f"Bild des Artikels: {article_selected}")
        image_url = filter_article.iloc[0]["image"]  # oder z.B. filter_article["image"].values[0]

        if isinstance(image_url, str) and image_url.startswith("http"):
            try:
                st.image(image_url, width=600)
            except Exception as e:
                st.warning(f"Bild konnte nicht geladen werden: {e}")
        else:
            st.info("Kein Bild vorhanden.")
    st.divider()

    st.header("Preisverlauf")

    # Abbildung mit Preisverlauf erstellen
    fig = px.line(
        filter_article,
        x="date",
        y="price",
        markers=True,
        labels={"date": "Datum", "price": "Preis"},
        title=f"Preisverlauf des Artikels {article_selected}"
    )
    fig.update_traces(
        marker=dict(symbol='square', size=8, color='blue'),  # Viereckige Marker
        line=dict(dash='dash', color='blue')  # Gestrichelte Linie (blau)
    )
    st.plotly_chart(fig)

    st.subheader("Liste mit den Zeitpunkten der Aktualisierung der Getränkekarte")

    date_selected = st.selectbox("Wähle ein Datum zum Abruf der Getränkekarte aus", df["date"].sort_values(ascending=False).unique())
    with st.expander(f"Speisekarte am {date_selected}"):
        df_date_selected = df[df["date"] == date_selected]
        st.dataframe(df_date_selected)
    st.divider()
    product_counts = df.groupby("date")["name"].count().reset_index()

    # Abbildung mit Produkten je Datum erstellen
    fig = px.bar(
        product_counts,
        barmode="group",
        x="date",
        y="name",
        title=f"Anzahl der Produkte zum jeweiligen Zeitpunkt",
        labels={"date": "Datum", "name": "Anzahl der Produkte"},
        text_auto=True
    )
    fig.update_layout(bargap=0.0005, bargroupgap=0.0005)
    st.plotly_chart(fig)

    st.divider()