import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")   # Layout von Streamlit konfigurieren

# Navigationsbar oben konfigurieren
selected = option_menu(
    menu_title = None,
    options = ["Home", "food", "beverages"],
    icons = ["house", "utensils", "cup-straw"],
    menu_icon = "cast",
    orientation = "horizontal"
)

# Fallunterscheidung: Wenn Reiter ausgewählt, importiere Code des jeweiligen Reiters
if selected == "Home":
    import Home
    Home.show_home()

if selected == "food":
    import food
    food.show_food()

if selected == "beverages":
    import beverages
    beverages.show_beverages()