# Gezinsfluencers Advies App - verbeterde zoekfunctie, grotere tekst en visuele structuur
import streamlit as st
import random

# Pagina-instellingen
st.set_page_config(page_title="Gezinsfluencers Advies App", layout="centered")

# Stijl
st.markdown("""
<style>
    .stApp {
        background-color: #FFF8F0;
        font-family: 'Comic Sans MS', cursive;
    }
    .title {
        text-align: center;
        color: #4E342E;
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
        background-color: #FFFAF0;
        border-left: 5px solid #FFCC80;
        padding: 20px;
        font-size: 18px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<div class='title'>🎈 Gezinsfluencers Advies App</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Kies hieronder een situatie om advies te krijgen – met een knipoog én stevige onderbouwing 😉</p>", unsafe_allow_html=True)

# --- Adviezen en situaties (hersteld en uitgebreid) ---
adviezen = {
    "Driftbui": {"advies": """📚 **Feit:** Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.
💡 **Tip:** Blijf rustig, benoem emoties.
😄 **Knipoog:** Jij bent de kapitein, ook als het schip vuur spuwt.
🔗 _Bron: NJI (2022)_"""},
    "Niet luisteren": {"advies": """📚 **Feit:** 'Niet luisteren' = overprikkeling/testgedrag.
💡 **Tip:** Korte zinnen, oogcontact, positieve feedback.
😄 **Knipoog:** Fluisteren werkt soms verrassend goed.
🔗 _Bron: Triple P_"""},
    "Agressief gedrag": {"advies": "📚 **Feit:** Kan voortkomen uit onmacht of prikkelgevoeligheid.
💡 **Tip:** Stel grenzen met rust. Help met woorden geven aan boosheid.
😄 **Knipoog:** Misschien een kussenbokssessie voor jullie allebei?
🔗 _Bron: Tischa Neve_"},
    "Concentratieproblemen": {"advies": "📚 **Feit:** Kinderen zijn vaak overprikkeld of niet uitgedaagd.
💡 **Tip:** Bied structuur, korte taken en beweging tussendoor.
😄 **Knipoog:** Korte pauze = dansen op de woonkamerbank.
🔗 _Bron: Kinderbrein.nl_"},
    "Slaapproblemen": {"advies": "📚 **Feit:** Slaappatronen ontwikkelen zich tot 6 jaar.
💡 **Tip:** Vaste routines, geen schermen voor het slapen.
😄 **Knipoog:** En daarna? Jij. Dekentje. Netflix.
🔗 _Bron: Slaapslim.nl_"},
    "Angst": {"advies": "📚 **Feit:** Angst is normaal, vooral bij nieuwe situaties.
💡 **Tip:** Neem het serieus. Rust en herhaling helpen.
😄 **Knipoog:** En een zelfgemaakte anti-monsterspray natuurlijk.
🔗 _Bron: NJI_"},
    "Pesten": {"advies": "📚 **Feit:** Heeft vaak impact op zelfbeeld en vertrouwen.
💡 **Tip:** Praat open. Werk samen met school.
😄 **Knipoog:** En jij? Jij bent hun superheld op sokken.
🔗 _Bron: Stichting Omgaan met Pesten_"},
    "Snoep stelen": {"advies": "📚 **Feit:** Jonge kinderen snappen eigendom nog niet goed.
💡 **Tip:** Leg rustig uit wat van wie is, laat herstellen.
😄 **Knipoog:** FBI-material. Let maar op.
🔗 _Bron: Opvoedinformatie.nl_"},
    "Alles is 'saai'": {"advies": "📚 **Feit:** Verveling stimuleert creativiteit.
💡 **Tip:** Bied niks aan. Laat ze zélf iets bedenken.
😄 **Knipoog:** Geef ze een wasmand. Succes gegarandeerd.
🔗 _Bron: Ouders van Nu_"},
    "100x 'Waarom?' vragen": {"advies": "📚 **Feit:** Dit is taalontwikkeling én aandacht zoeken.
💡 **Tip:** Stel de vraag terug. Of zet een timer: nog 3 vragen!
😄 **Knipoog:** Waarom? Omdat jij het kan.
🔗 _Bron: Het Kindontwikkelboek_"},
    "Wil niet naar school": {"advies": "📚 **Feit:** Kan te maken hebben met spanning of sociale angst.
💡 **Tip:** Maak school voorspelbaar. Start rustig. Check met leerkracht.
😄 **Knipoog:** Herinner ze aan de pauzehap.
🔗 _Bron: NJI_"},
    "Overprikkeld na school": {"advies": "📚 **Feit:** Schooldagen zijn intens. Kinderen moeten ontladen.
💡 **Tip:** Rust, geen vragen, even niks.
😄 **Knipoog:** Laat ze gewoon uitrazen zoals jij na een lange werkdag.
🔗 _Bron: Hooggevoelig.nl_"},
    "Verveelt zich met 800 speelgoedjes": {"advies": "📚 **Feit:** Keuzestress en gewoonte maken speelgoed 'onzichtbaar'.
💡 **Tip:** Roteer speelgoed. Minder is meer.
😄 **Knipoog:** Of geef ze een wc-rol en zeg: 'Bedenk iets'.
🔗 _Bron: Simpel opvoeden_"},
    "Zegt 'ik ben dom'": {"advies": "📚 **Feit:** Kinderen spiegelen taal die ze horen.
💡 **Tip:** Focus op inzet, niet resultaat. Complimenteer slim.
😄 **Knipoog:** ‘Dan ben ik de keizer van dom – ik stak ooit een tosti in de dvd-speler’.
🔗 _Bron: Carol Dweck_"},
    "Kledingcrisis in de ochtend": {"advies": "📚 **Feit:** Keuzes geven = autonomie ontwikkelen.
💡 **Tip:** Laat 's avonds kiezen uit 2 outfits.
😄 **Knipoog:** Of gewoon crocs met glitterjurk. YOLO.
🔗 _Bron: Positief Opvoeden_"},
    "Discussie over schermtijd": {"advies": "📚 **Feit:** Te veel schermen = impact op slaap en gedrag.
💡 **Tip:** Maak samen regels. Stel schermvrije zones.
😄 **Knipoog:** En ja, jij ook. Oeps.
🔗 _Bron: Mediaopvoeding.nl_"},
    "Kind denkt dat hij de baas is": {"advies": "📚 **Feit:** Kinderen testen grenzen, dat is normaal.
💡 **Tip:** Wees duidelijk en voorspelbaar. Gebruik humor.
😄 **Knipoog:** Jij bent de manager van team chaos.
🔗 _Bron: Tischa Neve_"},
    "Jaloers op broer of zus": {"advies": "📚 **Feit:** Jaloezie komt voort uit aandacht en vergelijking.
💡 **Tip:** Geef ieder kind exclusieve tijd. Benoem uniek gedrag.
😄 **Knipoog:** Wie jaloers is mag de afwas doen.
🔗 _Bron: Opvoedinformatie Nederland_"},
    "Wil altijd winnen": {"advies": "📚 **Feit:** Competitiedrang hoort bij de ontwikkeling van eigenwaarde.
💡 **Tip:** Leer omgaan met verlies via spelletjes.
😄 **Knipoog:** Zeg gewoon: 'Jij wint, ik ruim op'. Win-win.
🔗 _Bron: Pedagogisch Kader Spel_"},
    "Moeite met afscheid nemen": {"advies": "📚 **Feit:** Hechting beïnvloedt afscheid nemen.
💡 **Tip:** Gebruik rituelen, wees voorspelbaar.
😄 **Knipoog:** Knuffel, zwaai, sprint. Niet omkijken.
🔗 _Bron: Babywijzer.nl_"},
    "Durft niet alleen te spelen": {"advies": "📚 **Feit:** Zelfstandig spelen vraagt oefening.
💡 **Tip:** Begin met samen starten, daarna stukje terugtrekken.
😄 **Knipoog:** Jij bent geen animatieteam.
🔗 _Bron: Simpelopvoeden.nl_"}
}

# Selectie uit lijst eerst
situatie_lijst = list(adviezen.keys())
keuze = st.selectbox("👇 Kies een gedrag of situatie", situatie_lijst)

# Advies tonen vanuit lijstselectie
if st.button("🎁 Geef mij advies"):
    st.markdown(f"<div class='advies-box'>{adviezen[keuze]['advies']}</div>", unsafe_allow_html=True)

# Willekeurige tip
if st.button("🎲 Verras me!"):
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
st.markdown("""
<div class='webshop-link'>
    🛍️ Bekijk ook onze <a href='https://www.gezinsfluencers.nl/cadeau-tips/leuke-producten/' target='_blank'>leuke producten voor ouders</a>!
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 Gezinsfluencers | Advies met een knipoog én inhoud</div>", unsafe_allow_html=True)
