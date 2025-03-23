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
    "Gooien met speelgoed": {"advies": "🧠 <b>Feit:</b> Vaak een signaal van frustratie of onmacht.<br><br>💡 <b>Tip:</b> Stop het spel even, benoem gevoelens en laat zien wat wel kan.<br><br>😉 <b>Knipoog:</b> Alles vliegt behalve de sfeer? Tijd voor thee.<br><br>📚 <b>Bron:</b> Ouders Centraal"},
    "Niet willen delen": {"advies": "🧠 <b>Feit:</b> Bezit is belangrijk voor jonge kinderen.<br><br>💡 <b>Tip:</b> Oefen samen delen in rustige situaties, zonder druk.<br><br>😉 <b>Knipoog:</b> 'Samen spelen' is een ambitie, geen startpunt.<br><br>📚 <b>Bron:</b> Pedagogisch Kader"},
    "Kleding weigeren": {"advies": "🧠 <b>Feit:</b> Dit gaat vaak over controle willen houden.<br><br>💡 <b>Tip:</b> Geef keuzes: 'Wil je de blauwe of de rode trui?'<br><br>😉 <b>Knipoog:</b> Modieuze driftbuien zijn ook een fase.<br><br>📚 <b>Bron:</b> NCJ"},
    "Regels negeren": {"advies": "🧠 <b>Feit:</b> Herhaling en duidelijkheid zijn essentieel.<br><br>💡 <b>Tip:</b> Wees consequent, benoem positief gedrag en herhaal je verwachting.<br><br>😉 <b>Knipoog:</b> Regels zijn geen suggesties – ook niet op dinsdagen.<br><br>📚 <b>Bron:</b> Positief Opvoeden"},
    "Altijd druk": {"advies": "🧠 <b>Feit:</b> Sommige kinderen hebben meer beweegbehoefte.<br><br>💡 <b>Tip:</b> Bouw beweegmomenten in en leer rustmomenten aan via spel.<br><br>😉 <b>Knipoog:</b> Een kind met turbo = ouder met koffie.<br><br>📚 <b>Bron:</b> Hersenstichting"},
    "Neemt speelgoed van anderen af": {"advies": "🧠 <b>Feit:</b> Impulsbeheersing is nog in ontwikkeling.<br><br>💡 <b>Tip:</b> Grijp rustig in, benoem het juiste gedrag en oefen samen met ‘wacht op je beurt’.<br><br>😉 <b>Knipoog:</b> Alles is aantrekkelijker in andermans hand.<br><br>📚 <b>Bron:</b> KinderopvangTotaal"},
    "Kijkt de hele dag YouTube": {"advies": "🧠 <b>Feit:</b> Onbegeleid gebruik geeft veel prikkels en beïnvloeding.<br><br>💡 <b>Tip:</b> Kijk samen, stel tijdsgrenzen en bied aantrekkelijk alternatief.<br><br>😉 <b>Knipoog:</b> Als je het kanaal kent, heb je al half gewonnen.<br><br>📚 <b>Bron:</b> NJi / Mediawijsheid.nl"},

    "Concentratieproblemen": {"advies": "🧠 <b>Feit:</b> Kinderen zijn vaak overprikkeld of niet uitgedaagd.<br><br>💡 <b>Tip:</b> Zorg voor duidelijke structuur en voldoende pauzes.<br><br>😉 <b>Knipoog:</b> Soms helpt een danspauze meer dan een preek.<br><br>📚 <b>Bron:</b> Expertisecentrum Leerlingenzorg"},
    "Overprikkeld na school": {"advies": "🧠 <b>Feit:</b> Schooldagen zijn intens. Kinderen moeten ontladen.<br><br>💡 <b>Tip:</b> Bied een rustige overgang na schooltijd, zonder meteen vragen.<br><br>😉 <b>Knipoog:</b> Laat ze eerst ontploffen, daarna knuffelen.<br><br>📚 <b>Bron:</b> Hersenstichting"},
    "Huilt snel": {"advies": "🧠 <b>Feit:</b> Kinderen huilen om te ontladen of als signaal.<br><br>💡 <b>Tip:</b> Erken het gevoel eerst voordat je troost of stuurt.<br><br>😉 <b>Knipoog:</b> Tranen zijn gewoon mini-resetknoppen.<br><br>📚 <b>Bron:</b> Pedagogisch Kader Kinderopvang"},
    "Boos bij verlies (spelletje)": {"advies": "🧠 <b>Feit:</b> Jongere kinderen vinden verliezen écht lastig.<br><br>💡 <b>Tip:</b> Leer ze omgaan met verlies door oefening en humor.<br><br>😉 <b>Knipoog:</b> 'Jij wint als je verliest met een glimlach.'<br><br>📚 <b>Bron:</b> Opvoedadvies.nl"},
    "Eet langzaam / weigert eten": {"advies": "🧠 <b>Feit:</b> Eetgedrag kan samenhangen met autonomie en sensorische prikkels.<br><br>💡 <b>Tip:</b> Maak van eten geen strijd. Klein aanbod, grote complimenten.<br><br>😉 <b>Knipoog:</b> Elk hapje telt – ook als het een wortelsliertje is.<br><br>📚 <b>Bron:</b> Voedingscentrum"},
    "Spulletjes stelen": {"advies": "🧠 <b>Feit:</b> Kinderen onder 7 begrijpen eigendom nog niet volledig.<br><br>💡 <b>Tip:</b> Spreek rustig uit dat iets teruggegeven moet worden.<br><br>😉 <b>Knipoog:</b> Misschien vond hij het gewoon ‘te leuk om niet te houden’.<br><br>📚 <b>Bron:</b> Positief Opvoeden – Triple P"},
    "100x 'Waarom?' vragen": {"advies": "🧠 <b>Feit:</b> Dit is taalontwikkeling én aandacht zoeken.<br><br>💡 <b>Tip:</b> Geef af en toe serieus antwoord – en af en toe een grapje.<br><br>😉 <b>Knipoog:</b> Je mag ook eens 'Waarom denk jij?' teruggooien.<br><br>📚 <b>Bron:</b> NJi / Taalontwikkeling.nl"},
    "Wil niet naar school": {"advies": "🧠 <b>Feit:</b> Kan te maken hebben met spanning of sociale angst.<br><br>💡 <b>Tip:</b> Praat zonder oordeel. Begin bij kleine stapjes (schoolplein etc.).<br><br>😉 <b>Knipoog:</b> Wie wil er nou wél vroeg opstaan in een koude ochtend?<br><br>📚 <b>Bron:</b> Schoolmaatschappelijk werk / KJP"}
})
