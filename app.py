import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gratitude and Growth – Mindset Reframer", page_icon=None, layout="centered")

# --- BRAND COLORS ---
GUNMETAL = "#333F48"
ELECTRIC_BLUE = "#009CDE"
BRONZE = "#AFA9A0"
CREAMTONE = "#F5F1E5"

# --- CUSTOM STYLING ---
st.markdown(f"""
    <style>
        .main {{
            background-color: {CREAMTONE};
            font-family: 'Montserrat', sans-serif;
        }}
        h1, h2, h3 {{
            color: {GUNMETAL};
            font-family: 'Montserrat', sans-serif;
        }}
        .team-header {{
            text-align: center;
            margin-top: 30px;
            margin-bottom: 10px;
        }}
        .team-title {{
            font-size: 24px;
            font-weight: 700;
            color: {GUNMETAL};
            margin-bottom: 15px;
        }}
        .broker-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin: 30px 0;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
        }}
        .broker-card {{
            text-align: center;
            padding: 15px;
            border-bottom: 3px solid {ELECTRIC_BLUE};
        }}
        .broker-name {{
            font-size: 16px;
            font-weight: 700;
            color: {GUNMETAL};
            margin-bottom: 3px;
        }}
        .broker-title {{
            font-size: 12px;
            color: {ELECTRIC_BLUE};
            font-style: italic;
            margin-bottom: 8px;
        }}
        .broker-contact {{
            font-size: 11px;
            color: {GUNMETAL};
            line-height: 1.6;
        }}
        .footer {{
            text-align: center;
            font-size: 14px;
            color: {GUNMETAL};
            margin-top: 50px;
        }}
        .reframe-box {{
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 10px;
            border: 1px solid {BRONZE};
        }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER WITH LOGO ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://i.imgur.com/xG8V4fL.png", width=200)

st.markdown("<h1 style='text-align:center;'>Gratitude and Growth – Try Our Mindset Reframer!</h1>", unsafe_allow_html=True)
st.write("Shift your perspective this holiday season. Enter a statement below and see it reframed into Growth, Abundance, and Get-to mindsets.")

# --- INPUT ---
user_statement = st.text_input("Enter your statement:", placeholder="e.g., I have to finish this report")

# --- REFRAME FUNCTION ---
def reframe_statement(statement):
    original = statement.strip()
    growth = f"Finishing this task helps me learn and improve: '{original}'."
    abundance = f"Completing this task creates new opportunities: '{original}'."
    get_to = f"I get to do this because it benefits me: '{original}'."

    if "have to" in original.lower():
        growth = original.replace("have to", "choose to because it helps me grow")
        abundance = original.replace("have to", "get to, which opens new possibilities")
        get_to = original.replace("have to", "get to")
    elif "can't" in original.lower():
        growth = original.replace("can't", "can learn to")
        abundance = original.replace("can't", "have opportunities to")
        get_to = original.replace("can't", "get to try and improve")

    return growth, abundance, get_to

# --- OUTPUT ---
if user_statement:
    growth, abundance, get_to = reframe_statement(user_statement)
    st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
    st.markdown(f"<div class='reframe-box'><b>Growth Mindset:</b> {growth}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='reframe-box'><b>Abundance Mindset:</b> {abundance}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='reframe-box'><b>Get-to Mindset:</b> {get_to}</div>", unsafe_allow_html=True)

    # Download option
    reframed_text = f"Growth Mindset: {growth}\nAbundance Mindset: {abundance}\nGet-to Mindset: {get_to}"
    st.download_button("Download Your Reframes", reframed_text, file_name="mindset_reframes.txt")

# --- TEAM SECTION ---
st.markdown("""
    <div class='team-header'>
        <div class='team-title'>ANCHORED RETAIL TEAM</div>
    </div>
""", unsafe_allow_html=True)

# IPA Logo centered
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("https://i.imgur.com/xG8V4fL.png", width=150)

st.markdown("""
    <div class='broker-grid'>
        <div class='broker-card'>
            <div class='broker-name'>TOM LAGOS</div>
            <div class='broker-title'>Executive Director</div>
            <div class='broker-contact'>
                C: 310.722.8939<br>
                tlagos@ipausa.com
            </div>
        </div>
        <div class='broker-card'>
            <div class='broker-name'>PATRICK TOOMEY</div>
            <div class='broker-title'>Executive Director</div>
            <div class='broker-contact'>
                C: 310.403.4984<br>
                ptoomey@ipausa.com
            </div>
        </div>
        <div class='broker-card'>
            <div class='broker-name'>JOSE CARRAZANA</div>
            <div class='broker-title'>Director</div>
            <div class='broker-contact'>
                C: 786.973.8929<br>
                jcarrazana@ipausa.com
            </div>
        </div>
        <div class='broker-card'>
            <div class='broker-name'>ENRIQUE WONG</div>
            <div class='broker-title'>First Vice President</div>
            <div class='broker-contact'>
                C: 818.266.5483<br>
                enrique.wong@marcusmillichap.com
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div class='footer'>© 2025 Institutional Property Advisors | ipausa.com</div>", unsafe_allow_html=True)
