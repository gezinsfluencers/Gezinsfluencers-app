# Gezinsfluencers Advies App - uitgebreid met zoekfunctie, feiten en humor
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
</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<div class='title'>🎈 Gezinsfluencers Advies App</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Klik op een situatie en krijg advies met een knipoog én een stevige onderbouwing 😉</p>", unsafe_allow_html=True)

# Gedragingen + situaties
adviezen = {
    "Driftbui": {
        "advies": "📚 **Feit:** Kinderen tussen 2 en 6 hebben moeite met zelfregulatie. Een driftbui is vaak een ontlading van overprikkeling.\n💡 **Tip:** Blijf zelf rustig. Benoem het gevoel ('Je bent boos omdat...'). Reageer pas ná de bui.\n😄 **Knipoog:** Jij bent de kapitein, ook als je schip vuur spuwt.\n🔗 _Bron: Nederlands Jeugdinstituut (2022)_"
    },
    "Niet luisteren": {
        "advies": "📚 **Feit:** Kinderen filteren prikkels anders. 'Niet luisteren' is soms overbelasting of testgedrag.\n💡 **Tip:** Maak oogcontact, geef één opdracht tegelijk, gebruik positieve feedback.\n😄 **Knipoog:** Probeer eens fluisteren – gek genoeg gaan ze dan wél luisteren.\n🔗 _Bron: Triple P, Positief Opvoeden_"
    },
    "Schreeuwt als iets niet lukt": {
        "advies": "📚 **Feit:** Frustratietolerantie ontwikkelt zich langzaam. Kinderen uiten onmacht met geluid.\n💡 **Tip:** Benoem het gevoel en model oplossingsgedrag: 'Laten we het samen opnieuw proberen'.\n😄 **Knipoog:** Jij hebt vast ook wel eens op 'Send' gedrukt voor je mail af was.\n🔗 _Bron: Tischa Neve, opvoedkundige_"
    },
    "Wil niet naar school": {
        "advies": "📚 **Feit:** Schoolangst komt vaak door onzekerheid of sociale druk.\n💡 **Tip:** Praat rustig, gebruik visuele dagplannen en houd contact met school.\n😄 **Knipoog:** Herinner ze liefdevol aan de pauzehap en gymdag.\n🔗 _Bron: NJI - Onderwijs & Welzijn_"
    },
    "Onverklaarbaar hyper om 22:00 uur": {
        "advies": "📚 **Feit:** Kinderen worden vaak hyper als ze oververmoeid raken.\n💡 **Tip:** Creëer een rustgevende slaaproutine met vaste afsluiting, zoals voorlezen.\n😄 **Knipoog:** Spring mee. Of fluister 'slaapfeest' en sluit de deur langzaam.\n🔗 _Bron: Slaapslim.nl_"
    },
    "Overprikkeld na school": {
        "advies": "📚 **Feit:** Na school kunnen kinderen 'ontladen'. De rugzak zit vol met indrukken.\n💡 **Tip:** Laat ze even ontprikkelen zonder vragen. Denk aan muziek, knuffelen of bouwen.\n😄 **Knipoog:** Ook jij snauwt als je honger hebt en iemand vraagt waar de schaar is.\n🔗 _Bron: Het hooggevoelige kind - Elaine Aron_"
    },
    "Zegt 'ik ben dom'": {
        "advies": "📚 **Feit:** Negatief zelfbeeld kan al jong ontstaan door (onbedoelde) feedback of vergelijking.\n💡 **Tip:** Benoem inzet, niet alleen resultaat. Stimuleer zelfvertrouwen via complimenten op gedrag.\n😄 **Knipoog:** Zeg: 'Dan ben ik de keizerin van dom – want ik heb ooit pindakaas in de vriezer gelegd.'\n🔗 _Bron: Carol Dweck – Growth Mindset_"
    }
    # ... hier kun je eenvoudig meer toevoegen in hetzelfde format
}

# Zoekbalk
st.subheader("Zoek een gedrag of situatie")
zoekterm = st.text_input("Typ bijvoorbeeld: boos, school, slapen, dom, luisteren...")

# Filter resultaten
gevonden = [k for k in adviezen.keys() if zoekterm.lower() in k.lower()] if zoekterm else list(adviezen.keys())
keuze = st.selectbox("Kies uit de lijst", gevonden)

# Advies tonen
if st.button("🎁 Geef mij advies"):
    st.markdown(adviezen[keuze]["advies"])

# Willekeurige tip
if st.button("🎲 Verras me!"):
    random_key = random.choice(list(adviezen.keys()))
    st.markdown(adviezen[random_key]["advies"])

# Footer
st.markdown("<div class='footer'>© 2025 Gezinsfluencers | Advies met een knipoog én inhoud</div>", unsafe_allow_html=True)
