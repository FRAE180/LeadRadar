
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titel der App
st.title("Kundenanalyse für EBV Elektronik")

# Sidebar für Eingaben
st.sidebar.header("🔍 Eingabeparameter")

# Eingabefelder
firmenname = st.sidebar.text_input("Firmenname", "Dryad Networks")
region = st.sidebar.text_input("Region", "Berlin")
sprache = st.sidebar.selectbox("Sprache", ["Deutsch", "Englisch"])

# Bewertungskriterien mit Gewichtung
st.sidebar.subheader("⚖️ Bewertungskriterien (0 = unwichtig, 10 = sehr wichtig)")
gewichtung = {
    "Innovation": st.sidebar.slider("Innovation", 0, 10, 10),
    "Größe": st.sidebar.slider("Größe", 0, 10, 8),
    "Partnerschaften": st.sidebar.slider("Partnerschaften", 0, 10, 6),
    "Engineering-Fokus": st.sidebar.slider("Engineering-Fokus", 0, 10, 9),
    "Regionale Relevanz": st.sidebar.slider("Regionale Relevanz", 0, 10, 7)
}

# Button zur Analyse
if st.sidebar.button("Analyse starten"):
    st.subheader(f"📊 Analyseergebnisse für: {firmenname}")

    # Simulierte Bewertungen (könnten später durch echte Webanalyse ersetzt werden)
    bewertung = {
        "Innovation": 9,
        "Größe": 6,
        "Partnerschaften": 7,
        "Engineering-Fokus": 8,
        "Regionale Relevanz": 7
    }

    # Berechnung des Scores
    score = sum(gewichtung[k] * bewertung[k] for k in gewichtung) / sum(gewichtung.values()) * 10
    score = round(score, 2)

    # Anzeige der Bewertungstabelle
    df = pd.DataFrame({
        "Kriterium": list(gewichtung.keys()),
        "Gewichtung": list(gewichtung.values()),
        "Bewertung": [bewertung[k] for k in gewichtung]
    })
    st.table(df)

    # Balkendiagramm
    fig, ax = plt.subplots()
    ax.bar(df["Kriterium"], df["Bewertung"], color="skyblue")
    ax.set_ylabel("Bewertung (0–10)")
    ax.set_title("Einzelbewertungen")
    st.pyplot(fig)

    # Gesamtscore anzeigen
    st.metric(label="📈 Gesamtscore", value=f"{score} / 10")

    # Zusammenfassung
    st.markdown("### 📝 Zusammenfassung")
    st.markdown(f"""
    **{firmenname}** ist ein Unternehmen mit Sitz in **{region}**, das in der Sprache **{sprache}** kommuniziert.  
    Basierend auf den gewählten Kriterien ergibt sich ein Gesamtscore von **{score}/10**.

    **Empfehlung**:  
    - Bei einem Score über 7 lohnt sich ein Kontakt für EBV Elektronik.  
    - Mögliche Ansatzpunkte: Sensorik, Embedded Systems, Partnerschaften im Bereich Umwelttechnik.
    """)

    st.success("Analyse abgeschlossen!")

else:
    st.info("Bitte gib die Daten ein und klicke auf 'Analyse starten'.")
