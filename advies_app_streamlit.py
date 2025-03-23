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
adviezen = {
    "Driftbui": {"advies": "🧠 <b>Feit:</b> Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.<br><br>💡 <b>Tip:</b> Geef ruimte voor ontlading, blijf zelf rustig en reflecteer achteraf.<br><br>😉 <b>Knipoog:</b> Soms heb jij ook zin om op de vloer te liggen, toch?<br><br>📚 <b>Bron:</b> TNO / Ouders Centraal"},
    "Slaapproblemen": {"advies": "🧠 <b>Feit:</b> Slaappatronen ontwikkelen zich tot 6 jaar.<br><br>💡 <b>Tip:</b> Zorg voor een vast ritueel, dim lichten en schermen uit voor bedtijd.<br><br>😉 <b>Knipoog:</b> Nachtelijke wandelingen zijn overrated.<br><br>📚 <b>Bron:</b> NCJ / Slaaplaboratorium"},
    "Niet luisteren": {"advies": "🧠 <b>Feit:</b> ‘Niet luisteren’ is vaak overprikkeling of testgedrag.<br><br>💡 <b>Tip:</b> Spreek kort en op ooghoogte. Geef 2 duidelijke keuzes.<br><br>😉 <b>Knipoog:</b> Jij bent de Spotify van aanwijzingen – herhaalmodus aan.<br><br>📚 <b>Bron:</b> Positief Opvoeden / NJi"},
    "Pesten": {"advies": "🧠 <b>Feit:</b> Pesten kan voortkomen uit onmacht of groepsdynamiek.<br><br>💡 <b>Tip:</b> Praat met je kind, benoem gevoelens en betrek school of opvang waar nodig.<br><br>😉 <b>Knipoog:</b> Vriendelijkheid = de enige besmettelijkheid die we steunen.<br><br>📚 <b>Bron:</b> Stichting Stop Pesten Nu / NJi"},
    "Angst": {"advies": "🧠 <b>Feit:</b> Angst hoort bij ontwikkeling – tot op zekere hoogte.<br><br>💡 <b>Tip:</b> Normaliseer, adem samen en steun met rustige toon.<br><br>😉 <b>Knipoog:</b> Spinnen zijn misschien enger voor jou dan voor hen.<br><br>📚 <b>Bron:</b> Kindertherapie Nederland / Opvoedinformatie.nl"},
    "Agressief gedrag": {"advies": "🧠 <b>Feit:</b> Kan voortkomen uit onmacht of prikkelgevoeligheid.<br><br>💡 <b>Tip:</b> Blijf kalm, stop het gedrag, benoem emoties en geef een alternatief.<br><br>😉 <b>Knipoog:</b> Hulk komt ook weer tot rust na een knuffel.<br><br>📚 <b>Bron:</b> NJi / Ouderschap Blijft"},
    "Concentratieproblemen": {"advies": "🧠 <b>Feit:</b> Kinderen zijn vaak overprikkeld of niet uitgedaagd.<br><br>💡 <b>Tip:</b> Zorg voor een rustige werkplek, korte taakjes en beweging tussendoor.<br><br>😉 <b>Knipoog:</b> Focus? Alleen als het over ijsjes gaat.<br><br>📚 <b>Bron:</b> Hersenstichting / Leerlingbegeleiding"},
    "Snoep willen als ontbijt": {"advies": "🧠 <b>Feit:</b> Suiker werkt als beloning in de hersenen.<br><br>💡 <b>Tip:</b> Vervang door fruit met een leuke naam ('heldenhap')<br><br>😉 <b>Knipoog:</b> Pindakaas telt als proteïne, toch?<br><br>📚 <b>Bron:</b> Voedingscentrum / Gezonde School"},
    "Overprikkeld na school": {"advies": "🧠 <b>Feit:</b> Schooldagen zijn intens. Kinderen moeten ontladen.<br><br>💡 <b>Tip:</b> Bouw rustmomenten in na schooltijd. Laat ze vrij spelen.<br><br>😉 <b>Knipoog:</b> Geef ze chips of stilte – of beide.<br><br>📚 <b>Bron:</b> Ouders van Nu / Balans"},
    "Wil niet naar school": {"advies": "🧠 <b>Feit:</b> Kan te maken hebben met spanning of sociale angst.<br><br>💡 <b>Tip:</b> Blijf praten, bouw het op in stapjes en betrek school.<br><br>😉 <b>Knipoog:</b> Ochtendfiles bestaan ook binnenshuis.<br><br>📚 <b>Bron:</b> Leerkracht24 / NJi"}
}

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
    "Te laat komen": {"advies": "🧠 <b>Feit:</b> Tijdsbesef ontwikkelt zich pas rond 7 jaar.<br><br>💡 <b>Tip:</b> Gebruik visuele timers of pictogrammen in de ochtendroutine.<br><br>😉 <b>Knipoog:</b> Kinderen leven op hun eigen tijdzone.<br><br>📚 <b>Bron:</b> Pedagogisch Tijdschrift / NJi"},
    "Sloffen in plaats van schoenen": {"advies": "🧠 <b>Feit:</b> Comfort wint vaak van etiquette bij kinderen.<br><br>💡 <b>Tip:</b> Laat ze zelf schoenen kiezen (met grip) bij de voordeur.<br><br>😉 <b>Knipoog:</b> Sloffen zijn ook maar rebels schoeisel.<br><br>📚 <b>Bron:</b> Opvoedinformatie Nederland"},
    "Vingervlug op alles drukken": {"advies": "🧠 <b>Feit:</b> Jonge kinderen leren door aanraking.<br><br>💡 <b>Tip:</b> Bied dingen aan waarop gedrukt mág worden.<br><br>😉 <b>Knipoog:</b> Elk knopje roept ‘druk op mij!’ – logisch toch?<br><br>📚 <b>Bron:</b> Breinontwikkeling bij jonge kinderen – Hersenstichting"},
    "Schelden of nare woorden gebruiken": {"advies": "🧠 <b>Feit:</b> Kinderen kopiëren taalgebruik uit hun omgeving.<br><br>💡 <b>Tip:</b> Benoem alternatief taalgebruik, herhaal vriendelijk.<br><br>😉 <b>Knipoog:</b> Papegaai gespeeld, zonder kooi.<br><br>📚 <b>Bron:</b> Taalontwikkeling.nl / Ouders Centraal"},
    "Alles is oneerlijk": {"advies": "🧠 <b>Feit:</b> Rechtvaardigheidsgevoel piekt tussen 4-8 jaar.<br><br>💡 <b>Tip:</b> Benoem gevoelens, en leg uit waarom iets zo gaat.<br><br>😉 <b>Knipoog:</b> ‘Eerlijk’ = als zij winnen.<br><br>📚 <b>Bron:</b> GroeiGids / Positief Opvoeden"},
    "Alles vergeten op school": {"advies": "🧠 <b>Feit:</b> Geheugen & executieve functies zijn volop in ontwikkeling.<br><br>💡 <b>Tip:</b> Checklijst maken of tas samen inpakken helpt!<br><br>😉 <b>Knipoog:</b> Gymtas? Broodtrommel? Alleen hun glimlach is mee.<br><br>📚 <b>Bron:</b> Onderwijsontwikkeling Nederland"},
    "Niet willen douchen": {"advies": "🧠 <b>Feit:</b> Sensorisch ongemak of geen tijdsbesef.<br><br>💡 <b>Tip:</b> Maak er een vast moment van, liefst speels (watergevecht, liedje).<br><br>😉 <b>Knipoog:</b> In bad gaan? Alleen als piraat op missie.<br><br>📚 <b>Bron:</b> Ouderschap Blijft / Sensorische prikkelverwerking"},
    "Smoesjes bij huiswerk": {"advies": "🧠 <b>Feit:</b> Concentratie wisselt en motivatie mist vaak bij verplichte taken.<br><br>💡 <b>Tip:</b> Maak kleine taakjes, plan pauzes en geef complimenten.<br><br>😉 <b>Knipoog:</b> Het huiswerk is ineens 'per ongeluk' verdwenen.<br><br>📚 <b>Bron:</b> Ouders Online / Leerlingbegeleiding"},
    "Wiebelen aan tafel": {"advies": "🧠 <b>Feit:</b> Niet iedereen kan lang stilzitten (zeker na school).<br><br>💡 <b>Tip:</b> Laat even bewegen voor etenstijd, en hou het kort.<br><br>😉 <b>Knipoog:</b> Stoel = trampoline in hun hoofd.<br><br>📚 <b>Bron:</b> Gedragsspecialisten / Ouders Centraal"},
    "Elke dag verkleed willen zijn": {"advies": "🧠 <b>Feit:</b> Fantasie versterkt zelfexpressie en creatief denken.<br><br>💡 <b>Tip:</b> Geef ruimte, leg grenzen uit bij specifieke gelegenheden.<br><br>😉 <b>Knipoog:</b> Superheld naar school? Waarom niet.<br><br>📚 <b>Bron:</b> Kinderpsychologie Magazine / Speelgoed Nederland"}
})

# --- Gedrag selecteren en advies tonen ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📌 Kies een gedrag of situatie:")

keuze = st.selectbox("Gedrag of situatie", list(adviezen.keys()))

if st.button("Toon advies"):
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)
