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

# --- Adviezen en situaties (hersteld en uitgebreid) ---
adviezen = {
    "Driftbui": {"advies": "<b>Feit:</b> Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.<br><br><b>Tip:</b> Blijf zelf rustig, geef ruimte en praat er later over."},
    "Niet luisteren": {"advies": "<b>Feit:</b> ‘Niet luisteren’ = vaak overprikkeling of testgedrag.<br><br><b>Tip:</b> Geef korte instructies en check of je kind je hoort."},
    "Agressief gedrag": {"advies": "<b>Feit:</b> Kan voortkomen uit onmacht of prikkelgevoeligheid.<br><br><b>Tip:</b> Benoem wat je wél wil zien en houd grenzen rustig maar stevig."},
    "Concentratieproblemen": {"advies": "<b>Feit:</b> Kinderen zijn vaak overprikkeld of niet uitgedaagd.<br><br><b>Tip:</b> Bied afwisseling en duidelijke structuur."},
    "Slaapproblemen": {"advies": "<b>Feit:</b> Slaappatronen ontwikkelen zich tot 6 jaar.<br><br><b>Tip:</b> Vaste bedtijden en schermvrij minstens 30 min voor bedtijd."},
    "Angst": {"advies": "<b>Feit:</b> Angst is normaal, zeker bij veranderingen.<br><br><b>Tip:</b> Erken de angst en oefen samen in kleine stapjes."},
    "Pesten": {"advies": "<b>Feit:</b> Pesten kan voortkomen uit onzekerheid of groepsdruk.<br><br><b>Tip:</b> Neem het serieus, praat met school en blijf in gesprek."},
    "Overprikkeld na school": {"advies": "<b>Feit:</b> Schooldagen zijn intens. Kinderen moeten ontladen.<br><br><b>Tip:</b> Geef je kind tijd om thuis tot rust te komen – even geen vragen, geen prikkels."},
    "100x 'Waarom?' vragen": {"advies": "<b>Feit:</b> Dit is taalontwikkeling én aandacht zoeken.<br><br><b>Tip:</b> Geef een keer serieus antwoord, daarna stel zelf een 'waarom'-vraag terug 😄."},
    "Wil niet naar school": {"advies": "<b>Feit:</b> Kan te maken hebben met spanning of sociale angst.<br><br><b>Tip:</b> Blijf kalm, maak dingen voorspelbaar en schakel school in als het aanhoudt."},
    "Eet heel weinig": {"advies": "<b>Feit:</b> Peuters en kleuters eten vaak schommelend.<br><br><b>Tip:</b> Bied kleine porties zonder druk. Gezelligheid aan tafel = meer eetlust."},
    "Is altijd druk": {"advies": "<b>Feit:</b> Sommige kinderen hebben meer beweegbehoefte.<br><br><b>Tip:</b> Bouw beweegmomenten in en leer rustmomenten aan via spel."},
    "Snoep stelen": {"advies": "<b>Feit:</b> Jonge kinderen hebben nog geen besef van eigendom zoals volwassenen.<br><br><b>Tip:</b> Leg rustig uit wat 'eigen' is en geef ruimte om opnieuw te kiezen."},
    "Liegen": {"advies": "<b>Feit:</b> Kinderen fantaseren of vermijden straf.<br><br><b>Tip:</b> Reageer niet te streng. Help eerlijkheid oefenen door mild te reageren."},
    "Gooien met speelgoed": {"advies": "<b>Feit:</b> Vaak een signaal van frustratie of onmacht.<br><br><b>Tip:</b> Stop het spel even, benoem gevoelens en laat zien wat wel kan."},
    "Niet willen delen": {"advies": "<b>Feit:</b> Bezit is belangrijk voor jonge kinderen.<br><br><b>Tip:</b> Oefen samen delen in rustige situaties, zonder druk."},
    "Kleding weigeren": {"advies": "<b>Feit:</b> Dit gaat vaak over controle willen houden.<br><br><b>Tip:</b> Geef keuzes: 'Wil je de blauwe of de rode trui?'"},
    "Regels negeren": {"advies": "<b>Feit:</b> Herhaling en duidelijkheid zijn essentieel.<br><br><b>Tip:</b> Wees consequent, benoem positief gedrag en herhaal je verwachting."},
    "Krijgt alles voor elkaar": {"advies": "<b>Feit:</b> Slimme kinderen leren snel wat werkt.<br><br><b>Tip:</b> Zeg gerust nee en houd vast aan afspraken – ook als het drama oplevert."},
    "Niet stil kunnen zitten": {"advies": "<b>Feit:</b> Beweging helpt bij concentratie.<br><br><b>Tip:</b> Las beweegpauzes in en bied fidget-materiaal aan bij stilzitmomenten."},
    "Heeft geen vriendjes": {"advies": "<b>Feit:</b> Sociale ontwikkeling loopt bij ieder kind anders.<br><br><b>Tip:</b> Oefen sociale vaardigheden spelenderwijs. Nodig kinderen uit voor korte speelafspraken."},
    "Wil niet slapen zonder ouder": {"advies": "<b>Feit:</b> Hechting = veiligheid. Alleen slapen vraagt vertrouwen.<br><br><b>Tip:</b> Bouw het langzaam af met voorspelbare stapjes en veel aanmoediging."},
    "Altijd een weerwoord": {"advies": "<b>Feit:</b> Kind zoekt autonomie of verbinding.<br><br><b>Tip:</b> Luister eerst echt, geef keuzeruimte en stel daarna je grens."},
    "Doet niets in de klas": {"advies": "<b>Feit:</b> Dit kan spanning of onderstimulatie zijn.<br><br><b>Tip:</b> Overleg met de leerkracht en kijk samen naar wat helpt."},
    "Altijd moe na school": {"advies": "<b>Feit:</b> School vraagt veel mentale energie.<br><br><b>Tip:</b> Plan geen afspraken na school en gun je kind ontprikkeltijd."},
    "Bang in het donker": {"advies": "<b>Feit:</b> Verbeelding en realiteit lopen vaak door elkaar.<br><br><b>Tip:</b> Gebruik rituelen, nachtlampje en geruststelling – zonder het gevoel weg te wuiven."},
    "Verveelt zich snel": {"advies": "<b>Feit:</b> Verveling is de start van creativiteit.<br><br><b>Tip:</b> Laat het even sudderen voor je redt. Geef een open eind opdracht zoals ‘bouw iets met 5 dingen’."},
    "Test steeds grenzen": {"advies": "<b>Feit:</b> Grenzen testen = veilig voelen.<br><br><b>Tip:</b> Reageer voorspelbaar, blijf kalm en benoem wat je verwacht."},
    "Kijkt de hele dag YouTube": {"advies": "<b>Feit:</b> Onbegeleid gebruik geeft veel prikkels en beïnvloeding.<br><br><b>Tip:</b> Kijk samen, stel tijdsgrenzen en bied aantrekkelijk alternatief."},
    "Neemt speelgoed van anderen af": {"advies": "<b>Feit:</b> Impulsbeheersing is nog in ontwikkeling.<br><br><b>Tip:</b> Grijp rustig in, benoem het juiste gedrag en oefen samen met ‘wacht op je beurt’."}
}

# Selectie uit lijst eerst
situatie_lijst = list(adviezen.keys())
keuze = st.selectbox("👇 Kies een gedrag of situatie", situatie_lijst)

# Advies tonen vanuit lijstselectie
if st.button("🎁 Geef mij advies"):
    st.markdown("""
    <audio autoplay loop style='display:none;'>
      <source src='https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/happy-music-upbeat-fun-uplifting-travel-background-intro-theme-297310.mp3' type='audio/mpeg'>
    </audio>
    """, unsafe_allow_html=True)
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)

# Willekeurige tip
if st.button("🎲 Verras me!"):
    st.markdown("""
    <audio autoplay loop style='display:none;'>
      <source src='https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/happy-music-upbeat-fun-uplifting-travel-background-intro-theme-297310.mp3' type='audio/mpeg'>
    </audio>
    """, unsafe_allow_html=True)
    random_key = random.choice(situatie_lijst)
    st.markdown(f"<div class='advies-box'><b>{random_key}</b><br><br>{adviezen[random_key]['advies']}</div>", unsafe_allow_html=True)

# Extra rubriek: Oudertips & Gebeurtenissen
with st.expander("📋 Oudertips & Situaties"):
    tips = {
        "🕰️ Wat is de beste bedtijd voor kinderen?": """Tussen 18:30 – 20:30 uur, afhankelijk van leeftijd.
Maar wees eerlijk: het echte gevecht begint pas bij tandenpoetsen.
<b>Pro tip:</b> Ritme is belangrijker dan het exacte tijdstip.""",
        "☀️ Hoe overleef je de zomertijd met kids?": """Hard reset: gewoon gelijk naar het nieuwe ritme.
Of: elke dag 15 minuten verschuiven.
Kinderen klagen sowieso. Jij wint op doorzettingsvermogen.""",
        "🎒 Wat moet er in een weekendtas voor een kind?": """4 outfits (voor 2 dagen)
Snacks (voor 3 weken)
Knuffel, reserveknuffel, en back-up-deken
En natuurlijk... vergeten tandenborstel. Altijd.""",
        "🥦 Wat als mijn kind geen groente eet?": """Verstop het in pannenkoeken
Geef het een toffe naam ('superheldensaus')
Of… accepteer het. Soms is ketchup ook een groente.""",
        "🎮 Hoeveel schermtijd is normaal?": """Zolang jij soms rust krijgt, is het 'normaal'.
Officieel: max. 1 uur per dag (peuters).
Realistisch: dat was alleen haalbaar toen de wifi uitviel.""",
        "🍽️ Wat eten we vanavond? (met weinig tijd)": """Pasta + pesto + iets van groenten
Soep + tosti = feestmaal
Of ontbijt als avondeten = altijd goed bij kinderen
<b>Tip:</b> Als je er een naam aan geeft ('avonturenpasta'), eten ze het eerder.""",
        "🧳 Wat moet ik regelen als mijn kind naar school/opvang gaat?": """Label álles (inclusief hun sokken, want echt)
Reservekleding
Duidelijke afspraken over ophalen
En mentale voorbereiding op ALLE themaweken""",
        "🎉 Wat is een goede kindertraktatie zonder gedoe?": """Rozijntjes met een wiebel-oogje
Rijstwafel met smiley
Mini marshmallows in een zakje = feestje
Ouders blij = missie geslaagd."""
    }
    for tip, antwoord in tips.items():
        st.markdown(f"<div class='advies-box'><b>{tip}</b><br><br>{antwoord}</div>", unsafe_allow_html=True)
