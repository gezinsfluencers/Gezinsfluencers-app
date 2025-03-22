# Gezinsfluencers Advies App - compleet met zoekfunctie, onderbouwing, knipoog en webshop-link
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
</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<div class='title'>🎈 Gezinsfluencers Advies App</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Klik op een situatie en krijg advies met een knipoog én een stevige onderbouwing 😉</p>", unsafe_allow_html=True)

# Adviezen importeren uit extern bestand of uitbreiden hieronder
adviezen = {
    "Driftbui": {"advies": "📚 **Feit:** Kinderen tussen 2 en 6 hebben moeite met zelfregulatie.\n💡 **Tip:** Blijf rustig, benoem emoties.\n😄 **Knipoog:** Jij bent de kapitein, ook als het schip vuur spuwt.\n🔗 _Bron: NJI (2022)_"},
    "Niet luisteren": {"advies": "📚 **Feit:** 'Niet luisteren' = overprikkeling/testgedrag.\n💡 **Tip:** Korte zinnen, oogcontact, positieve feedback.\n😄 **Knipoog:** Fluisteren werkt soms verrassend goed.\n🔗 _Bron: Triple P_"},
    "Agressief gedrag": {"advies": "📚 **Feit:** Kan voortkomen uit onmacht of prikkelgevoeligheid.\n💡 **Tip:** Stel grenzen met rust. Help met woorden geven aan boosheid.\n😄 **Knipoog:** Misschien een kussenbokssessie voor jullie allebei?\n🔗 _Bron: Tischa Neve_"},
    "Concentratieproblemen": {"advies": "📚 **Feit:** Kinderen zijn vaak overprikkeld of niet uitgedaagd.\n💡 **Tip:** Bied structuur, korte taken en beweging tussendoor.\n😄 **Knipoog:** Korte pauze = dansen op de woonkamerbank.\n🔗 _Bron: Kinderbrein.nl_"},
    "Slaapproblemen": {"advies": "📚 **Feit:** Slaappatronen ontwikkelen zich tot 6 jaar.\n💡 **Tip:** Vaste routines, geen schermen voor het slapen.\n😄 **Knipoog:** En daarna? Jij. Dekentje. Netflix.\n🔗 _Bron: Slaapslim.nl_"},
    "Angst": {"advies": "📚 **Feit:** Angst is normaal, vooral bij nieuwe situaties.\n💡 **Tip:** Neem het serieus. Rust en herhaling helpen.\n😄 **Knipoog:** En een zelfgemaakte anti-monsterspray natuurlijk.\n🔗 _Bron: NJI_"},
    "Pesten": {"advies": "📚 **Feit:** Heeft vaak impact op zelfbeeld en vertrouwen.\n💡 **Tip:** Praat open. Werk samen met school.\n😄 **Knipoog:** En jij? Jij bent hun superheld op sokken.\n🔗 _Bron: Stichting Omgaan met Pesten_"},
    "Snoep stelen": {"advies": "📚 **Feit:** Jonge kinderen snappen eigendom nog niet goed.\n💡 **Tip:** Leg rustig uit wat van wie is, laat herstellen.\n😄 **Knipoog:** FBI-material. Let maar op.\n🔗 _Bron: Opvoedinformatie.nl_"},
    "Alles is 'saai'": {"advies": "📚 **Feit:** Verveling stimuleert creativiteit.\n💡 **Tip:** Bied niks aan. Laat ze zélf iets bedenken.\n😄 **Knipoog:** Geef ze een wasmand. Succes gegarandeerd.\n🔗 _Bron: Ouders van Nu_"},
    "100x 'Waarom?' vragen": {"advies": "📚 **Feit:** Dit is taalontwikkeling én aandacht zoeken.\n💡 **Tip:** Stel de vraag terug. Of zet een timer: nog 3 vragen!\n😄 **Knipoog:** Waarom? Omdat jij het kan.\n🔗 _Bron: Het Kindontwikkelboek_"},
    "Wil niet naar school": {"advies": "📚 **Feit:** Kan te maken hebben met spanning of sociale angst.\n💡 **Tip:** Maak school voorspelbaar. Start rustig. Check met leerkracht.\n😄 **Knipoog:** Herinner ze aan de pauzehap.\n🔗 _Bron: NJI_"},
    "Overprikkeld na school": {"advies": "📚 **Feit:** Schooldagen zijn intens. Kinderen moeten ontladen.\n💡 **Tip:** Rust, geen vragen, even niks.\n😄 **Knipoog:** Laat ze gewoon uitrazen zoals jij na een lange werkdag.\n🔗 _Bron: Hooggevoelig.nl_"},
    "Verveelt zich met 800 speelgoedjes": {"advies": "📚 **Feit:** Keuzestress en gewoonte maken speelgoed 'onzichtbaar'.\n💡 **Tip:** Roteer speelgoed. Minder is meer.\n😄 **Knipoog:** Of geef ze een wc-rol en zeg: 'Bedenk iets'.\n🔗 _Bron: Simpel opvoeden_"},
    "Zegt 'ik ben dom'": {"advies": "📚 **Feit:** Kinderen spiegelen taal die ze horen.\n💡 **Tip:** Focus op inzet, niet resultaat. Complimenteer slim.\n😄 **Knipoog:** ‘Dan ben ik de keizer van dom – ik stak ooit een tosti in de dvd-speler’.\n🔗 _Bron: Carol Dweck_"},
    "Kledingcrisis in de ochtend": {"advies": "📚 **Feit:** Keuzes geven = autonomie ontwikkelen.\n💡 **Tip:** Laat 's avonds kiezen uit 2 outfits.\n😄 **Knipoog:** Of gewoon crocs met glitterjurk. YOLO.\n🔗 _Bron: Positief Opvoeden_"},
    "Discussie over schermtijd": {"advies": "📚 **Feit:** Te veel schermen = impact op slaap en gedrag.\n💡 **Tip:** Maak samen regels. Stel schermvrije zones.\n😄 **Knipoog:** En ja, jij ook. Oeps.\n🔗 _Bron: Mediaopvoeding.nl_"},
    "Kind denkt dat hij de baas is": {"advies": "📚 **Feit:** Kinderen testen grenzen, dat is normaal.\n💡 **Tip:** Wees duidelijk en voorspelbaar. Gebruik humor.\n😄 **Knipoog:** Jij bent de manager van team chaos.\n🔗 _Bron: Tischa Neve_"},
    "Jaloers op broer of zus": {"advies": "📚 **Feit:** Jaloezie komt voort uit aandacht en vergelijking.\n💡 **Tip:** Geef ieder kind exclusieve tijd. Benoem uniek gedrag.\n😄 **Knipoog:** Wie jaloers is mag de afwas doen.\n🔗 _Bron: Opvoedinformatie Nederland_"},
    "Wil altijd winnen": {"advies": "📚 **Feit:** Competitiedrang hoort bij de ontwikkeling van eigenwaarde.\n💡 **Tip:** Leer omgaan met verlies via spelletjes.\n😄 **Knipoog:** Zeg gewoon: 'Jij wint, ik ruim op'. Win-win.\n🔗 _Bron: Pedagogisch Kader Spel_"},
    "Moeite met afscheid nemen": {"advies": "📚 **Feit:** Hechting beïnvloedt afscheid nemen.\n💡 **Tip:** Gebruik rituelen, wees voorspelbaar.\n😄 **Knipoog:** Knuffel, zwaai, sprint. Niet omkijken.\n🔗 _Bron: Babywijzer.nl_"},
    "Durft niet alleen te spelen": {"advies": "📚 **Feit:** Zelfstandig spelen vraagt oefening.\n💡 **Tip:** Begin met samen starten, daarna stukje terugtrekken.\n😄 **Knipoog:** Jij bent geen animatieteam.\n🔗 _Bron: Simpelopvoeden.nl_"}
}

# Zoekbalk
st.subheader("Zoek een gedrag of situatie")
zoekterm = st.text_input("Typ bijvoorbeeld: boos, school, slapen, dom, luisteren...")
gevonden = [k for k in adviezen.keys() if zoekterm.lower() in k.lower()] if zoekterm else list(adviezen.keys())
keuze = st.selectbox("Kies uit de lijst", gevonden)

# Advies tonen
if st.button("🎁 Geef mij advies"):
    st.markdown(adviezen[keuze]["advies"])

# Willekeurige tip
if st.button("🎲 Verras me!"):
    random_key = random.choice(list(adviezen.keys()))
    st.markdown(adviezen[random_key]["advies"])

# Webshop-link
st.markdown("""
<div class='webshop-link'>
    🛍️ Bekijk ook onze <a href='https://www.gezinsfluencers.nl/cadeau-tips/leuke-producten/' target='_blank'>leuke producten voor ouders</a>!
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 Gezinsfluencers | Advies met een knipoog én inhoud</div>", unsafe_allow_html=True)
