import streamlit as st

st.set_page_config(page_title="Gezinsfluencers Advies", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: #FF69B4;'>🎈Gezinsfluencers Advies App</h1>", 
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>Klik op een gedrag of situatie en krijg direct advies (met een knipoog 😉)</p>", unsafe_allow_html=True)

opties = [
    "Driftbui", "Niet luisteren", "Agressief gedrag", "Concentratieproblemen",
    "Slaapproblemen", "Angst", "Pesten", "Snoep stelen", "Alles is 'saai'",
    "100x 'Waarom?' vragen", "Wil niet naar school", "Kledingcrisis in de ochtend",
    "Discussie over schermtijd", "Alles duurt 100 jaar", "Geen groente willen eten",
    "Ligt op de grond in de supermarkt", "Kind denkt dat hij de baas is",
    "Altijd trek in iets ongezonds", "Verveelt zich met 800 speelgoedjes",
    "Onverklaarbaar hyper om 22:00 uur"
]

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

keuze = st.selectbox("👇 Kies een gedrag of situatie", opties)

if st.button("🎁 Geef mij advies!"):
    st.markdown(f"### 💬 Advies bij: *{keuze}*")
    st.success(adviezen.get(keuze, "Geen advies beschikbaar... Bel een opa of oma 😅"))

st.markdown("---")
st.markdown("<p style='text-align: center; font-size:12px;'>© 2025 Gezinsfluencers | Advies met een knipoog</p>", unsafe_allow_html=True)
