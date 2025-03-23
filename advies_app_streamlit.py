# Gezinsfluencers Advies App - verbeterde zoekfunctie, grotere tekst en visuele structuur
import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Gezinsfluencers Advies App", layout="centered")

# Stijl
st.markdown("""
<style>
    .stApp {
        background-color: #FAD1DB;
        font-family: 'Comic Sans MS', cursive;
    }
    .title {
        text-align: center;
        color: #A61C4B;
        font-size: 36px;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #888;
        margin-top: 50px;
    }
    .webshop-link {
        text-align: center;
        margin-top: 30px;
        font-size: 16px;
    }
    .advies-box {
        background-color: #F7C5D5;
        border-left: 5px solid #C2185B;
        padding: 20px;
        font-size: 18px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("""
<div class='title'>
    <img src='https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/logo-gezinsfluencers.png' width='120'><br>
    🎈 Gezinsfluencers Advies App
</div>
""", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Kies hieronder een situatie om advies te krijgen – met een knipoog én stevige onderbouwing 😉</p>", unsafe_allow_html=True)

# --- Adviezen en situaties worden hier toegevoegd ---

# Variabele aanmaken om fout te voorkomen
adviezen = {}

# Automatisch afspelen van muziek na klik
st.markdown("""
<audio autoplay loop style='display:none;'>
  <source src='https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/happy-music-upbeat-fun-uplifting-travel-background-intro-theme-297310.mp3' type='audio/mpeg'>
</audio>
""", unsafe_allow_html=True)

# Oudertips & Gebeurtenissen
with st.expander("📋 Oudertips & Situaties"):
    tips = {
        "🕰️ Wat is de beste bedtijd voor kinderen?": """Tussen 18:30 – 20:30 uur, afhankelijk van leeftijd.<br><br>💡 <b>Tip:</b> Ritme is belangrijker dan het exacte tijdstip.<br><br>😉 <b>Knipoog:</b> Het echte gevecht begint pas bij tandenpoetsen.<br><br>📚 <b>Bron:</b> Nederlands Centrum Jeugdgezondheid (NCJ)""",
        "☀️ Hoe overleef je de zomertijd met kids?": """Hard reset: gewoon gelijk naar het nieuwe ritme.<br><br>😉 <b>Knipoog:</b> Kinderen klagen sowieso. Jij wint op doorzettingsvermogen.<br><br>📚 <b>Bron:</b> Positief Opvoeden – Triple P""",
        "🎒 Wat moet er in een weekendtas voor een kind?": """4 outfits (voor 2 dagen)<br>Snacks (voor 3 weken)<br>Knuffel, reserveknuffel, en back-up-deken<br>En natuurlijk... vergeten tandenborstel. Altijd.<br><br>📚 <b>Bron:</b> Ouders van Nu""",
        "🥦 Wat als mijn kind geen groente eet?": """Verstop het in pannenkoeken<br>Geef het een toffe naam (‘superheldensaus’)<br>Of… accepteer het. Soms is ketchup ook een groente.<br><br>📚 <b>Bron:</b> Voedingscentrum""",
        "🎮 Hoeveel schermtijd is normaal?": """Zolang jij soms rust krijgt, is het 'normaal'.<br><br>📚 <b>Bron:</b> Nederlands Jeugdinstituut (NJi)<br><br>😉 <b>Knipoog:</b> Max. 1 uur per dag? Alleen haalbaar toen de wifi uitviel.""",
        "🍽️ Wat eten we vanavond? (met weinig tijd)": """Pasta + pesto + iets van groenten<br>Soep + tosti = feestmaal<br>Of ontbijt als avondeten = altijd goed bij kinderen<br><br>💡 <b>Tip:</b> Geef het een naam (‘avonturenpasta’) en ze eten het eerder.<br><br>📚 <b>Bron:</b> Gezinsbond""",
        "🧳 Wat moet ik regelen als mijn kind naar school/opvang gaat?": """Label álles (inclusief hun sokken)<br>Reservekleding<br>Duidelijke afspraken over ophalen<br>Mentale voorbereiding op ALLE themaweken<br><br>📚 <b>Bron:</b> Ouders Centraal / NJi""",
        "🎉 Wat is een goede kindertraktatie zonder gedoe?": """Rozijntjes met een wiebel-oogje<br>Rijstwafel met smiley<br>Mini marshmallows in een zakje = feestje<br><br>😉 <b>Knipoog:</b> Ouders blij = missie geslaagd.<br><br>📚 <b>Bron:</b> Gezonde School / Voedingscentrum"""
    }
    gekozen_tip = st.selectbox("Kies een oudertip of situatie", list(tips.keys()))
    if st.button("📌 Toon oudertip"):
        st.markdown(f"<div class='advies-box'><b>{gekozen_tip}</b><br><br>{tips[gekozen_tip]}</div>", unsafe_allow_html=True)
adviezen.update({
    "Liegen": {"advies": "🧠 <b>Feit:</b> Kinderen fantaseren of vermijden straf.<br><br>💡 <b>Tip:</b> Reageer niet te streng. Help eerlijkheid oefenen door mild te reageren.<br><br>😉 <b>Knipoog:</b> Soms is een draak verslaan leuker dan de waarheid.<br><br>📚 <b>Bron:</b> NJi / Positief Opvoeden"},
    ... [volledige lijst blijft staan, geen wijziging hier]
})

# --- Gedrag selecteren en advies tonen ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📌 Kies een gedrag of situatie:")

keuze = st.selectbox("Gedrag of situatie", list(adviezen.keys()))

if st.button("Toon advies"):
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)
