import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gratitude, Growth and Abundance – Reframe Your Mindset", page_icon=None, layout="centered")

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
        .logo-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
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
        .stColumn {{
            padding: 0 !important;
        }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align:center;'>Gratitude, Growth and Abundance<br>Reframe Your Mindset</h1>", unsafe_allow_html=True)
st.write("What's on your mind today? Type in something you're dreading, a frustration that's been nagging you, or just that thing you wish you didn't have to deal with. Let's see it from a different angle.")

# --- INPUT ---
user_statement = st.text_input("Enter your statement:", placeholder="e.g., I have to work through the holidays")

# --- IMPROVED REFRAME FUNCTION ---
def reframe_statement(statement):
    original = statement.strip()
    
    # Handle common negative patterns with smart replacements
    statement_lower = original.lower()
    
    # GROWTH MINDSET - Focus on learning and improvement
    if "have to" in statement_lower:
        growth = original.lower().replace("have to", "choose to")
        growth = f"I {growth} because it helps me grow and learn."
    elif "can't" in statement_lower:
        growth = original.lower().replace("can't", "haven't yet learned to")
        growth = f"{growth.capitalize()}, but I'm developing this skill."
    elif "too" in statement_lower and ("hot" in statement_lower or "cold" in statement_lower or "hard" in statement_lower or "difficult" in statement_lower):
        growth = f"While {original.lower()}, this challenge helps me build resilience and adaptability."
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed"]):
        growth = f"Even though {original.lower()}, I'm learning what I need to adjust and improve."
    else:
        growth = f"Experiencing '{original.lower()}' teaches me something valuable about myself and how I respond to circumstances."
    
    # ABUNDANCE MINDSET - Focus on opportunities and possibilities
    if "have to" in statement_lower:
        abundance = original.lower().replace("have to", "get to")
        abundance = f"I {abundance} - this opens new possibilities for me."
    elif "can't" in statement_lower:
        abundance = original.lower().replace("can't", "will find another way to")
        abundance = f"{abundance.capitalize()} - there are always multiple paths forward."
    elif "too" in statement_lower and ("hot" in statement_lower or "cold" in statement_lower):
        abundance = f"While {original.lower()}, I'm grateful I can experience different conditions and have options to adapt."
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed"]):
        abundance = f"Rather than being limited by feeling that {original.lower()}, I can see this as redirecting me toward better opportunities."
    else:
        abundance = f"Instead of just noticing that '{original.lower()},' I recognize this situation offers me new perspectives and opportunities."
    
    # GET-TO MINDSET - Focus on gratitude and privilege
    if "have to" in statement_lower:
        get_to = original.lower().replace("have to", "get to")
        get_to = f"I {get_to} - and I'm grateful for this opportunity."
    elif "can't" in statement_lower:
        get_to = original.lower().replace("can't", "will eventually be able to")
        get_to = f"I {get_to}, and I appreciate the journey toward that goal."
    elif "too" in statement_lower and ("hot" in statement_lower or "cold" in statement_lower):
        get_to = f"Even though {original.lower()}, I get to experience this moment and I have the resources to be comfortable."
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed"]):
        get_to = f"Though {original.lower()}, I get to have experiences that shape who I'm becoming."
    else:
        get_to = f"Noticing that '{original.lower()}' reminds me that I get to be present and aware in this moment."
    
    # Capitalize first letter
    growth = growth[0].upper() + growth[1:]
    abundance = abundance[0].upper() + abundance[1:]
    get_to = get_to[0].upper() + get_to[1:]
    
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

# --- BROKER CARDS ---
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

# --- TEAM SECTION ---
st.markdown("""
    <div class='team-header'>
        <div class='team-title'>ANCHORED RETAIL TEAM</div>
    </div>
""", unsafe_allow_html=True)

# IPA Logo
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    st.image("https://i.imgur.com/xG8V4fL.png", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div class='footer'>© 2025 Institutional Property Advisors | ipausa.com</div>", unsafe_allow_html=True)
