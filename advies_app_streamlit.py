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

# Voeg muziek toe die speelt bij een klik op advies
st.markdown("""
<audio id="muziek" src="https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/happy-music-upbeat-fun-uplifting-travel-background-intro-theme-297310.mp3"></audio>
<script>
    function speelMuziek() {
        var audio = window.parent.document.getElementById("muziek");
        if (audio) { audio.play(); }
    }
</script>
""", unsafe_allow_html=True)

# Adviezen herstellen met inhoud
adviezen = {
    "Driftbui": {"advies": "🧠 <b>Feit:</b> Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.<br><br>💡 <b>Tip:</b> Geef rust, erken het gevoel, en stel grenzen.<br><br>😉 <b>Knipoog:</b> Jij blijft de kapitein, ook als het schip stormt.<br><br>📚 <b>Bron:</b> Tischa Neve, kinderpsycholoog"},
    "Niet luisteren": {"advies": "📖 <b>Feit:</b> ‘Niet luisteren’ is vaak overprikkeling of testgedrag.<br><br>💡 <b>Tip:</b> Geef korte opdrachten en laat kind herhalen.<br><br>😉 <b>Knipoog:</b> Hoor jij je baas altijd direct bij het eerste verzoek?<br><br>📚 <b>Bron:</b> How2talk2kids"},
    "Agressief gedrag": {"advies": "🧠 <b>Feit:</b> Kan voortkomen uit onmacht of prikkelgevoeligheid.<br><br>💡 <b>Tip:</b> Benoem wat wél mag, blijf zelf rustig.<br><br>😉 <b>Knipoog:</b> Jouw rust is besmettelijker dan je denkt.<br><br>📚 <b>Bron:</b> Nederlands Jeugdinstituut (NJi)"},
    "Concentratieproblemen": {"advies": "📚 <b>Feit:</b> Kinderen zijn vaak overprikkeld of niet uitgedaagd.<br><br>💡 <b>Tip:</b> Bied structuur, korte taken en beweging tussendoor.<br><br>😉 <b>Knipoog:</b> Niemand focust 6 uur achter elkaar. Zelfs wij niet.<br><br>📚 <b>Bron:</b> Klassenkracht / ADHD-centrum"},
    "Slaapproblemen": {"advies": "🌙 <b>Feit:</b> Slaappatronen ontwikkelen zich tot 6 jaar.<br><br>💡 <b>Tip:</b> Creëer vaste rituelen, schermvrij uur voor bedtijd.<br><br>😉 <b>Knipoog:</b> Zelfs nachtdieren leren slapen met ritme.<br><br>📚 <b>Bron:</b> Centrum voor Slaapgeneeskunde SEIN"},
    "Angst": {"advies": "🧸 <b>Feit:</b> Angst is normaal in fases (donker, monsters, school).<br><br>💡 <b>Tip:</b> Erken de angst, help woorden geven, speel het na.<br><br>😉 <b>Knipoog:</b> Je kind is dapperder dan je denkt – zeker met jou ernaast.<br><br>📚 <b>Bron:</b> Kindertelefoon / KJP Nederland"},
    "Pesten": {"advies": "🧠 <b>Feit:</b> Gepest worden heeft veel impact, maar ook pesters missen vaak sociale vaardigheden.<br><br>💡 <b>Tip:</b> Praat dagelijks over school, neem signalen serieus.<br><br>😉 <b>Knipoog:</b> Een veilig thuis maakt het verschil.<br><br>📚 <b>Bron:</b> Stichting Stop Pesten Nu"},
    "Overprikkeld na school": {"advies": "🧠 <b>Feit:</b> Schooldagen zijn intens. Kinderen moeten ontladen.<br><br>💡 <b>Tip:</b> Geef rust na schooltijd, laat ze ontladen voordat je verwachtingen stelt.<br><br>😉 <b>Knipoog:</b> Thuis komen = opladen, niet presteren.<br><br>📚 <b>Bron:</b> Hersenstichting / Ouders Centraal"},
    "Te laat komen": {"advies": "🧠 <b>Feit:</b> Tijdsbesef ontwikkelt zich pas rond 7 jaar.<br><br>💡 <b>Tip:</b> Gebruik visuele timers of pictogrammen in de ochtendroutine.<br><br>😉 <b>Knipoog:</b> Verwacht geen Zwitsers horloge van een kleuter.<br><br>📚 <b>Bron:</b> Opvoedinformatie Nederland"},
    "Spulletjes stelen": {"advies": "🧠 <b>Feit:</b> Jonge kinderen snappen eigendom nog niet altijd.<br><br>💡 <b>Tip:</b> Leg rustig uit wat van jou en ander is en herstel samen.<br><br>😉 <b>Knipoog:</b> Misschien wilde hij gewoon delen… op zijn manier.<br><br>📚 <b>Bron:</b> Ouders van Nu / Kenniscentrum Kinderrechten"}
}

# --- Oudertips & Gebeurtenissen ---
with st.expander("📋 Oudertips & Situaties"):
    tips = {
        "🕰️ Wat is de beste bedtijd voor kinderen?": "Tussen 18:30 – 20:30 uur, afhankelijk van leeftijd. Aanbevolen bedtijd per leeftijd: 0-1 jaar tussen 18:00-19:00, 1-3 jaar tussen 18:30-19:30, 4-6 jaar tussen 19:00-20:00, 7-9 jaar tussen 19:30-20:30, 10-12 jaar tussen 20:00-21:00, 13-16 jaar tussen 21:00-22:00, en vanaf 16 jaar rond 22:00 (maar succes daarmee 😅).<br><br>💡 <b>Tip:</b> Ritme is belangrijker dan het exacte tijdstip.<br><br>😉 <b>Knipoog:</b> Het echte gevecht begint pas bij tandenpoetsen.<br><br>📚 <b>Bron:</b> Nederlands Centrum Jeugdgezondheid (NCJ)",
        "☀️ Hoe overleef je de zomertijd met kids?": "Hard reset: gewoon gelijk naar het nieuwe ritme.<br><br>😉 <b>Knipoog:</b> Kinderen klagen sowieso. Jij wint op doorzettingsvermogen.<br><br>📚 <b>Bron:</b> Positief Opvoeden – Triple P",
        "🎒 Wat moet er in een weekendtas voor een kind?": "4 outfits (voor 2 dagen)<br>Snacks (voor 3 weken)<br>Knuffel, reserveknuffel, en back-up-deken<br>En natuurlijk... vergeten tandenborstel. Altijd. Mee voor een weekendje weg met je kind: 2-3 setjes kleding, ondergoed en sokken, pyjama, tandenborstel + tandpasta, knuffel, speentje indien nodig, extra set kleding (voor ongelukjes), snacks, drinkbeker, eventueel lievelingsboek of speelgoed, en natuurlijk: een tas vol geduld 😅<br><br>📚 <b>Bron:</b> Ouders van Nu",
        "🥦 Wat als mijn kind geen groente eet?": "Verstop het in pannenkoeken<br>Geef het een toffe naam (‘superheldensaus’)<br>Of… accepteer het. Soms is ketchup ook een groente.<br><br>📚 <b>Bron:</b> Voedingscentrum",
        "🎮 Hoeveel schermtijd is normaal?": "Voor jonge kinderen (2-5 jaar) wordt maximaal 1 uur schermtijd per dag aangeraden, bij voorkeur samen met een ouder; voor kinderen van 6-12 jaar is 1 tot 2 uur per dag passend, met duidelijke afspraken over inhoud, pauzes en balans met offline activiteiten — het belangrijkste blijft: schermtijd bewust inzetten, niet als standaard vervanger voor verveling of contact..<br><br>📚 <b>Bron:</b> Nederlands Jeugdinstituut (NJi)<br><br>😉 <b>Knipoog:</b> Max. 1 uur per dag? Alleen haalbaar toen de wifi uitviel.",
        "🍽️ Wat eten we vanavond? (met weinig tijd)": "Pasta + pesto + iets van groenten<br>Soep + tosti = feestmaal<br>Of ontbijt als avondeten = altijd goed bij kinderen<br><br>💡 <b>Tip:</b> Geef het een naam (‘avonturenpasta’) en ze eten het eerder.<br><br>📚 <b>Bron:</b> Gezinsbond",
        "🧳 Wat moet ik regelen als mijn kind naar school/opvang gaat?": "Label álles (inclusief hun sokken)<br>Reservekleding<br>Duidelijke afspraken over ophalen<br>Mentale voorbereiding op ALLE themaweken<br><br>📚 <b>Bron:</b> Ouders Centraal / NJi",
        "🎉 Wat is een goede kindertraktatie zonder gedoe?": "Rozijntjes met een wiebel-oogje<br>Rijstwafel met smiley<br>Mini marshmallows in een zakje = feestje<br><br>😉 <b>Knipoog:</b> Ouders blij = missie geslaagd.<br><br>📚 <b>Bron:</b> Gezonde School / Voedingscentrum"
    }
    gekozen_tip = st.selectbox("Kies een oudertip of situatie", list(tips.keys()))
    if st.button("📌 Toon oudertip"):
        st.markdown(f"<div class='advies-box'><b>{gekozen_tip}</b><br><br>{tips[gekozen_tip]}</div>", unsafe_allow_html=True)

# Extra webshop link
st.markdown("""
<div class='webshop-link'>
    🛍️ <a href='https://www.gezinsfluencers.nl/cadeau-tips/leuke-producten/' target='_blank'>Bekijk ook onze webshop voor leuke producten</a>
</div>
""", unsafe_allow_html=True)

# --- Gedrag selecteren en advies tonen ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📌 Kies een gedrag of situatie:")

keuze = st.selectbox("Gedrag of situatie", list(adviezen.keys()))

if st.button("Toon advies"):
    st.markdown("<script>speelMuziek()</script>", unsafe_allow_html=True)
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)
