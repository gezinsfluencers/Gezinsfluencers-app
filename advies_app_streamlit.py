# Gezinsfluencers Advies App - uitgebreide versie met stijling en extra functies
import streamlit as st
import random

# --- Pagina instellingen ---
st.set_page_config(page_title="Gezinsfluencers Advies App", layout="centered")

# --- Kleuren en stijl ---
PRIMARY_COLOR = "#4E342E"  # donkerbruin
ACCENT_COLOR = "#FFCC80"   # warm oranje
BG_COLOR = "#F5F5DC"        # beige achtergrond

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {BG_COLOR};
        font-family: 'Comic Sans MS', cursive;
    }}
    .title-style {{
        color: {PRIMARY_COLOR};
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }}
    .footer-style {{
        text-align: center;
        font-size: 14px;
        color: grey;
        margin-top: 50px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Titels ---
st.markdown("<div class='title-style'>🎈 Gezinsfluencers Advies App</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Kies een gedrag of situatie en krijg advies met een knipoog 😉</p>", unsafe_allow_html=True)

# --- Thema's en gedragingen ---
thema_dict = {
    "Gedrag": ["Driftbui", "Niet luisteren", "Agressief gedrag", "Kind denkt dat hij de baas is"],
    "School": ["Concentratieproblemen", "Wil niet naar school", "Pesten"],
    "Slapen": ["Slaapproblemen", "Onverklaarbaar hyper om 22:00 uur"],
    "Dagelijks gedoe": [
        "Kledingcrisis in de ochtend", "Discussie over schermtijd", "Alles duurt 100 jaar",
        "Geen groente willen eten", "Alles is 'saai'", "100x 'Waarom?' vragen",
        "Snoep stelen", "Verveelt zich met 800 speelgoedjes", "Ligt op de grond in de supermarkt",
        "Altijd trek in iets ongezonds", "Angst"
    ]
}

# --- Adviezen ---
adviezen = {
    "Driftbui": "Blijf kalm. Jij bent de kapitein op het schip. Ook als het schip vuur spuwt.",
    "Niet luisteren": "Zet een gek stemmetje op. Plotseling ben je weer razend interessant.",
    "Agressief gedrag": "Grenzen stellen. Liefdevol. En ja, de bank overleeft het waarschijnlijk.",
    "Concentratieproblemen": "Gebruik een kookwekker. Of doe alsof je kind in een spannende missie zit.",
    "Slaapproblemen": "Rustige routine. En daarna: Netflix voor jou. Je hebt het verdiend.",
    "Angst": "Knuffelmodus aan. Monsters bestaan niet, maar knuffels wel.",
    "Pesten": "Praat, luister, steun. En schrijf een boze brief... die je niet verstuurt.",
    "Snoep stelen": "Snoep verstoppen. Of opeten. Probleem opgelost.",
    "Alles is 'saai'": "Laat ze het huis stofzuigen. Opeens is niks meer saai.",
    "100x 'Waarom?' vragen": "Antwoord: 'Waarom denk jij?' Herhaal tot ze moe zijn.",
    "Wil niet naar school": "Praat, troost, en herinner ze aan de pauzehap.",
    "Kledingcrisis in de ochtend": "Laat ze gisteren kiezen. Of accepteer pailletten in november.",
    "Discussie over schermtijd": "Stel schermregels op. En hou je er zelf (een beetje) aan.",
    "Alles duurt 100 jaar": "Gebruik een timer. Of dans mee tijdens het tandenpoetsen.",
    "Geen groente willen eten": "Verstop het. Of noem broccoli 'mini-bomen van de Hulk'.",
    "Ligt op de grond in de supermarkt": "Kijk omhoog. Doe alsof je haar stylist bent.",
    "Kind denkt dat hij de baas is": "Herinner je kind liefdevol aan de democratie: jij bent de voorzitter.",
    "Altijd trek in iets ongezonds": "Zeg: 'Eerst iets gezonds, dan onderhandelen we'. Werkt soms.",
    "Verveelt zich met 800 speelgoedjes": "Laat ze het speelgoed verkopen en 'ondernemen'. Of niet.",
    "Onverklaarbaar hyper om 22:00 uur": "Spring mee. Of fluister ‘slaapfeest’... en sluit de deur langzaam."
}

# --- Thema kiezen ---
st.subheader("Stap 1: Kies een thema")
thema = st.selectbox("", list(thema_dict.keys()))

# --- Gedrag kiezen ---
st.subheader("Stap 2: Kies een gedrag of situatie")
gedrag = st.selectbox("", thema_dict[thema])

# --- Extra invoerveld ---
st.text_input("Wil je iets toevoegen aan deze situatie?", placeholder="Bijv. Dit gebeurt elke ochtend 😩")

# --- Toon advies ---
if st.button("🎁 Geef mij advies!"):
    st.markdown(f"### 💬 Advies bij: *{gedrag}*")
    st.success(adviezen.get(gedrag, "Geen advies beschikbaar... Bel een opa of oma 😅"))

# --- Willekeurige verrassingstip ---
if st.button("🎲 Verras me!"):
    random_gedrag = random.choice(list(adviezen.keys()))
    st.markdown(f"### 💬 Verrassingstip bij: *{random_gedrag}*")
    st.info(adviezen[random_gedrag])

# --- Footer ---
st.markdown("<div class='footer-style'>© 2025 Gezinsfluencers | Advies met een knipoog</div>", unsafe_allow_html=True)
