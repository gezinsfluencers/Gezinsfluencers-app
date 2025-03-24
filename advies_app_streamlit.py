# Gezinsfluencers Advies App - verbeterde zoekfunctie, grotere tekst en visuele structuur
import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Gezinsfluencers Advies App", layout="centered")

# Stijl
st.markdown("""
<style>
    .stApp {
        background-color: #eae4db;
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
        margin-bottom: 30px;
        background-color: #F7C5D5;
        border-left: 5px solid #C2185B;
        padding: 20px;
        font-size: 18px;
        margin-top: 20px;
    }
label {
    font-size: 22px;
    font-weight: bold;
}

button[kind="primary"] {
    font-size: 20px;
    padding: 12px 24px;
}

div[data-baseweb="select"] {
    font-size: 20px;
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
<audio id="muziek" preload="auto">
  <source src="https://raw.githubusercontent.com/gezinsfluencers/Gezinsfluencers-app/main/happy-music-upbeat-fun-uplifting-travel-background-intro-theme-297310.mp3" type="audio/mpeg">
</audio>
<script>
  const audio = document.getElementById("muziek");
  function speelMuziek() {
    if (audio && typeof audio.play === 'function') {
      audio.currentTime = 0;
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.catch((error) => {
          console.log("Audio play blocked by browser:", error);
        });
      }
    }
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
    "Spulletjes stelen": {"advies": "🧠 <b>Feit:</b> Jonge kinderen snappen eigendom nog niet altijd.<br><br>💡 <b>Tip:</b> Leg rustig uit wat van jou en ander is en herstel samen.<br><br>😉 <b>Knipoog:</b> Misschien wilde hij gewoon delen… op zijn manier.<br><br>📚 <b>Bron:</b> Ouders van Nu / Kenniscentrum Kinderrechten"},

    "Schelden": {"advies": "🧠 <b>Feit:</b> Schelden is vaak een uitlaatklep voor frustratie die ze nog niet kunnen reguleren.<br><br>💡 <b>Tip:</b> Herhaal dat woorden pijn kunnen doen, en bied alternatieven zoals 'pauzewoorden'.<br><br>😉 <b>Knipoog:</b> Kleine mond, grote meningen. Gelukkig geen microfoon erbij.<br><br>📚 <b>Bron:</b> Opvoedinformatie Nederland"},

    "Niet delen": {"advies": "🧠 <b>Feit:</b> Delen is pas echt goed te verwachten vanaf ongeveer 4 jaar.<br><br>💡 <b>Tip:</b> Speel samen en benoem positief gedrag als het wél gebeurt.<br><br>😉 <b>Knipoog:</b> ‘Samen spelen, samen delen’... maar die regel gold niet voor zijn favoriete dino.<br><br>📚 <b>Bron:</b> NJi / Pedagogisch Kader Kinderopvang"},

    "Eten weigeren": {"advies": "🧠 <b>Feit:</b> Smaakpapillen van kinderen zijn gevoeliger dan die van volwassenen.<br><br>💡 <b>Tip:</b> Laat kinderen meehelpen met koken en bied iets vaker aan zonder dwang.<br><br>😉 <b>Knipoog:</b> Als het geen pannenkoek of pasta is, noemen ze het 'vies'.<br><br>📚 <b>Bron:</b> Voedingscentrum"},

    "Heel druk gedrag": {"advies": "🧠 <b>Feit:</b> Veel bewegen hoort bij de ontwikkeling, maar kan soms duiden op behoefte aan prikkelverwerking.<br><br>💡 <b>Tip:</b> Bied beweegmomenten aan én rustmomenten, structuur helpt.<br><br>😉 <b>Knipoog:</b> Springen op de bank = kinderversie van espresso.<br><br>📚 <b>Bron:</b> Balans Digitaal / Hersenstichting"}
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
        st.components.v1.html("""
        <script>
          var audio = window.parent.document.getElementById("muziek");
          if (audio) {
            audio.currentTime = 0;
            audio.play().catch(e => console.log("Autoplay blocked:", e));
          }
        </script>
        """, height=0)
        st.markdown(f"<div class='advies-box'><b>{gekozen_tip}</b><br><br>{tips[gekozen_tip]}</div>", unsafe_allow_html=True)

# Extra webshop link
st.markdown("""
<div class='webshop-link'>
    🛍️ <a href='https://www.gezinsfluencers.nl/cadeau-tips/leuke-producten/' target='_blank'>Bekijk ook onze webshop voor leuke producten</a>
</div>
""", unsafe_allow_html=True)
# --- Weeradvies & kledingtip ---
import requests

def haal_weer_data(api_key, stad="Amsterdam"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={stad}&appid={api_key}&units=metric&lang=nl"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

def genereer_kledingadvies(temp):
    if temp >= 25:
        return "☀️ Korte broek en t-shirt – zonnebrand niet vergeten!"
    elif temp >= 18:
        return "🌤️ Luchtige kleding met eventueel een vest."
    elif temp >= 12:
        return "🍃 Lange broek en trui. Jas mee voor de zekerheid."
    elif temp >= 5:
        return "🌥️ Warme jas, sjaal en dichte schoenen."
    else:
        return "❄️ Dikke jas, muts en handschoenen – brrr!"

# API key van OpenWeather
api_key = "3c9f7bdff73f7d336480c44e3bbae6b7"
weer_data = haal_weer_data(api_key)

if weer_data:
    temperatuur = weer_data["main"]["temp"]
    omschrijving = weer_data["weather"][0]["description"]
    advies = genereer_kledingadvies(temperatuur)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("👕 Kledingadvies voor vandaag")
    st.components.v1.html("""
        <script>
          var audio = window.parent.document.getElementById("muziek");
          if (audio) {
            audio.currentTime = 0;
            audio.play().catch(e => console.log("Autoplay blocked:", e));
          }
        </script>
    """, height=0)
    st.markdown(f"<div class='advies-box'>📍 In {weer_data['name']} is het momenteel <b>{temperatuur}°C</b> met <i>{omschrijving}</i>.<br><br>👚 <b>Kledingtip:</b> {advies}</div>", unsafe_allow_html=True)
else:
    st.error("Kon het weerbericht niet ophalen. Check je internet of API-key.") 
    st.write("")  # lege regel


keuze = st.selectbox("Gedrag of situatie", list(adviezen.keys()))

if st.button("Toon advies"):
    st.components.v1.html("""
    <script>
      var audio = window.parent.document.getElementById("muziek");
      if (audio) {
        audio.currentTime = 0;
        audio.play().catch(e => console.log("Autoplay blocked:", e));
      }
    </script>
    """, height=0)
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)
