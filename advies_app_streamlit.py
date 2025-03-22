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
    "Driftbui": {"advies": """<b>📚 Feit:</b> Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.

<b>💡 Tip:</b> Blijf rustig, benoem emoties.

<b>😄 Knipoog:</b> Jij bent de kapitein, ook als het schip vuur spuwt.

🔗 _Bron: NJI (2022)_"""},
    "Niet luisteren": {"advies": """<b>📚 Feit:</b> 'Niet luisteren' = overprikkeling/testgedrag.
    
<b>💡 Tip:</b> Korte zinnen, oogcontact, positieve feedback.

<b>😄 Knipoog:</b> Fluisteren werkt soms verrassend goed.

🔗 _Bron: Triple P_"""},
  
    "Agressief gedrag": {"advies": """<b>📚 Feit:</b> Kan voortkomen uit onmacht of prikkelgevoeligheid.
    
<b>💡 Tip:</b> Stel grenzen met rust. Help met woorden geven aan boosheid.

<b>😄 Knipoog:</b> Misschien een kussenbokssessie voor jullie allebei?

🔗 _Bron: Tischa Neve_"""},
  
    "Concentratieproblemen": {"advies": """<b>📚 Feit:</b> Kinderen zijn vaak overprikkeld of niet uitgedaagd.
    
<b>💡 Tip:</b> Bied structuur, korte taken en beweging tussendoor.

<b>😄 Knipoog:</b> Korte pauze = dansen op de woonkamerbank.

🔗 _Bron: Kinderbrein.nl_"""},
  
    "Slaapproblemen": {"advies": """<b>📚 Feit:</b> Slaappatronen ontwikkelen zich tot 6 jaar.
    
<b>💡 Tip:</b> Vaste routines, geen schermen voor het slapen.

<b>😄 Knipoog:</b> En daarna? Jij. Dekentje. Netflix.

🔗 _Bron: Slaapslim.nl_"""},
  
    "Angst": {"advies": """📚 <b>📚 Feit:</b> Angst is normaal, vooral bij nieuwe situaties.
    
💡 <b>💡 Tip:</b> Neem het serieus. Rust en herhaling helpen.

😄 <b>😄 Knipoog:</b> En een zelfgemaakte anti-monsterspray natuurlijk.

🔗 _Bron: NJI_"""},
  
    "Pesten": {"advies": """<b>📚 Feit:</b> Heeft vaak impact op zelfbeeld en vertrouwen.
    
<b>💡 Tip:</b> Praat open. Werk samen met school.

<b>😄 Knipoog:</b> En jij? Jij bent hun superheld op sokken.

🔗 _Bron: Stichting Omgaan met Pesten_"""},
  
    "Spulletjes stelen": {"advies": """<b>📚 Feit:</b> Jonge kinderen snappen eigendom nog niet goed.
    
<b>💡 Tip:</b> Leg rustig uit wat van wie is, laat herstellen.

<b>😄 Knipoog:</b> FBI-material. Let maar op.

🔗 _Bron: Opvoedinformatie.nl_"""},
  
    "Alles is 'saai'": {"advies": """📚 <b>📚 Feit:</b> Verveling stimuleert creativiteit.
    
💡 <b>💡 Tip:</b> Bied niks aan. Laat ze zélf iets bedenken.

😄 <b>😄 Knipoog:</b> Geef ze een wasmand. Succes gegarandeerd.

🔗 _Bron: Ouders van Nu_"""},
    "100x 'Waarom?' vragen": {"advies": """📚 <b>📚 Feit:</b> Dit is taalontwikkeling én aandacht zoeken.
    
💡 <b>💡 Tip:</b> Stel de vraag terug. Of zet een timer: nog 3 vragen!

😄 <b>😄 Knipoog:</b> Waarom? Omdat jij het kan.

🔗 _Bron: Het Kindontwikkelboek_"""},
    "Wil niet naar school": {"advies": """📚 <b>📚 Feit:</b> Kan te maken hebben met spanning of sociale angst.
    
💡 <b>💡 Tip:</b> Maak school voorspelbaar. Start rustig. Check met leerkracht.

😄 <b>😄 Knipoog:</b> Herinner ze aan de pauzehap.

🔗 _Bron: NJI_"""},
    "Overprikkeld na school": {"advies": """<b>📚 Feit:</b> Schooldagen zijn intens. Kinderen moeten ontladen.
    
<b>💡 Tip:</b> Rust, geen vragen, even niks.

<b>😄 Knipoog:</b> Laat ze gewoon uitrazen zoals jij na een lange werkdag.

🔗 _Bron: Hooggevoelig.nl_"""},
  
    "Verveelt zich met 800 speelgoedjes": {"advies": """📚 <b>📚 Feit:</b> Keuzestress en gewoonte maken speelgoed 'onzichtbaar'.
    
💡 <b>💡 Tip:</b> Roteer speelgoed. Minder is meer.

😄 <b>😄 Knipoog:</b> Of geef ze een wc-rol en zeg: 'Bedenk iets'.

🔗 _Bron: Simpel opvoeden_"""},
  
    "Zegt 'ik ben dom'": {"advies": """<b>📚 Feit:</b> Kinderen spiegelen taal die ze horen.
    
<b>💡 Tip:</b> Focus op inzet, niet resultaat. Complimenteer slim.

<b>😄 Knipoog:</b> ‘Dan ben ik de keizer van dom – ik stak ooit een tosti in de dvd-speler’.

🔗 _Bron: Carol Dweck_"""},
    "Kledingcrisis in de ochtend": {"advies": """📚 <b>📚 Feit:</b> Keuzes geven = autonomie ontwikkelen.
    
💡 <b>💡 Tip:</b> Laat 's avonds kiezen uit 2 outfits.

😄 <b>😄 Knipoog:</b> Of gewoon crocs met glitterjurk. YOLO.

🔗 _Bron: Positief Opvoeden_"""},
    "Discussie over schermtijd": {"advies": """<b>📚 Feit:</b> Te veel schermen = impact op slaap en gedrag.
    
<b>💡 Tip:</b> Maak samen regels. Stel schermvrije zones.

<b>😄 Knipoog:</b> En ja, jij ook. Oeps.

🔗 _Bron: Mediaopvoeding.nl_"""},
    "Kind denkt dat hij de baas is": {"advies": """📚 <b>📚 Feit:</b> Kinderen testen grenzen, dat is normaal.
    
💡 <b>💡 Tip:</b> Wees duidelijk en voorspelbaar. Gebruik humor.

😄 <b>😄 Knipoog:</b> Jij bent de manager van team chaos.

🔗 _Bron: Tischa Neve_"""},
    "Jaloers op broer of zus": {"advies": """<b>📚 Feit:</b> Jaloezie komt voort uit aandacht en vergelijking.
    
<b>💡 Tip:</b> Geef ieder kind exclusieve tijd. Benoem uniek gedrag.

<b>😄 Knipoog:</b> Wie jaloers is mag de afwas doen.

🔗 _Bron: Opvoedinformatie Nederland_"""},
    "Wil altijd winnen": {"advies": """📚 <b>📚 Feit:</b> Competitiedrang hoort bij de ontwikkeling van eigenwaarde.
    
💡 <b>💡 Tip:</b> Leer omgaan met verlies via spelletjes.

😄 <b>😄 Knipoog:</b> Zeg gewoon: 'Jij wint, ik ruim op'. Win-win.

🔗 _Bron: Pedagogisch Kader Spel_"""},
    "Moeite met afscheid nemen": {"advies": """<b>📚 Feit:</b> Hechting beïnvloedt afscheid nemen.
    
<b>💡 Tip:</b> Gebruik rituelen, wees voorspelbaar.

<b>😄 Knipoog:</b> Knuffel, zwaai, sprint. Niet omkijken.

🔗 _Bron: Babywijzer.nl_"""},
    "Durft niet alleen te spelen": {"advies": """📚 <b>📚 Feit:</b> Zelfstandig spelen vraagt oefening.
    
💡 <b>💡 Tip:</b> Begin met samen starten, daarna stukje terugtrekken.

😄 <b>😄 Knipoog:</b> Jij bent geen animatieteam.

🔗 _Bron: Simpelopvoeden.nl_"""}
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
    st.markdown(f"<div class='advies-box'>{adviezen[random_key]['advies']}</div>", unsafe_allow_html=True)

# Zoekfunctie onderaan als extra optie
with st.expander("🔍 Of zoek op een trefwoord"):
    zoekterm = st.text_input("Typ bijvoorbeeld: boos, school, slapen, dom, luisteren...")
    if zoekterm:
        gevonden = [k for k in adviezen if zoekterm.lower() in k.lower() or zoekterm.lower() in adviezen[k]["advies"].lower()]
        if gevonden:
            keuze_zoek = st.selectbox("Gevonden situaties:", gevonden)
            if st.button("Toon advies voor zoekresultaat"):
                st.markdown(f"<div class='advies-box'>{adviezen[keuze_zoek]['advies']}</div>", unsafe_allow_html=True)
        else:
            st.warning("Geen resultaten gevonden. Probeer een ander woord.")

# Webshop-link
st.markdown("<div class='webshop-link'>Bekijk ook onze <a href='https://www.gezinsfluencers.nl/cadeau-tips/leuke-producten/' target='_blank'>leuke producten voor ouders</a>!</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 Gezinsfluencers | Advies met een knipoog én inhoud</div>", unsafe_allow_html=True)
