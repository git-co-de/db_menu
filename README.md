Ursprüngliche Idee des Projekts von Jonas Köllermeier https://github.com/jkoeller93
Beitrag von git-co-de betrifft den Bereich Beverages. 

# DB_Train_Menu
Information about Onboard Dining Menu (Food &amp; Beverages) of German Railway Operator Deutsche Bahn

Datei "food_all_cleaned.csv"
- Enthält alle Speisen von allen abgerufenen Zeiten
- Alle csv Dateien wurden zusammengeführt
- Namen der Produkte bearbeitet
- Ähnliche Namen wurden zu einem Namen zusammengeführt

Datei "main.py"
- Von dieser Seite werden die anderen Seiten gesteuert
- Diese Datei aufrufen über streamlit run main.py
- Inhalte der anderen Seite werden hier importiert
- enthält das Layout von Streamlit

Datei "Home.py"
- Enthält den Code für die Seite "Home"
- Allgemeine Informationen zur Speisekarte wie Statistiken etc.

Datei "food.py"
- Enthält den Code für die Seite "food"
- Informationen und Analysen nur für die Speisen

Datei "beverages.py"
- Enthält den Code für die Seite "beverages"
- Informationen und Analyse nur für die Getränke (aktuell noch keine Daten hinterlegt)
