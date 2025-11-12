import streamlit as st
from openai import OpenAI
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Gratitude, Growth and Abundance – Reframe Your Mindset", 
    page_icon=None, 
    layout="centered"
)

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

/* IPA BRANDED BUTTON */
div[data-testid="stButton"] > button {{
    background-color: {ELECTRIC_BLUE} !important;
    color: white !important;
    border: none !important;
    padding: 0.5rem 2rem !important;
    font-weight: 600 !important;
    border-radius: 4px !important;
    font-size: 16px !important;
    width: 100%;
}}

div[data-testid="stButton"] > button:hover {{
    background-color: {GUNMETAL} !important;
    color: white !important;
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
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown(
    "<h1 style='text-align:center;'>Gratitude, Growth and Abundance<br>Reframe Your Mindset</h1>", 
    unsafe_allow_html=True
)
st.write(
    "What's on your mind today? Type in something you're dreading, a frustration that's been nagging you, "
    "or just that thing you wish you didn't have to deal with. Let's see it from a different angle."
)

# --- INPUT ---
user_statement = st.text_input(
    "Enter your statement:", 
    placeholder="e.g., I have to work through the holidays"
)

# --- CENTERED BUTTON ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate_button = st.button("Reframe My Mindset", type="primary", use_container_width=True)

# --- GENERATE REFRAMES ---
if generate_button and user_statement:
    
    with st.spinner("Thinking about this from different angles..."):
        
        try:
            # Initialize OpenAI client
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
            
            # Create the AI prompt
            prompt = f"""You are a thoughtful coach helping someone reframe a negative or draining thought into three different positive perspectives. The person said: "{user_statement}"

Please provide three distinct reframes, each 1-2 sentences:

1. GROWTH MINDSET: Focus on learning, development, skills gained, or personal evolution from this situation. Be specific to their statement and authentic - not generic.

2. ABUNDANCE MINDSET: Focus on opportunities, possibilities, what this opens up, or alternative perspectives that reveal more options. Be specific and genuine.

3. GET-TO MINDSET: Focus on gratitude, privilege, or the gift of being able to experience this. Make it feel sincere, not forced.

IMPORTANT: 
- Use their exact words and context from their statement
- Make each reframe feel natural and conversational, not like a template
- Vary your language - don't start every sentence the same way
- Be authentic and human
- Keep it concise - 1-2 sentences each
- DO NOT include labels like "Growth Mindset:" in your response
- DO NOT use quotation marks around their statement

Respond with ONLY the three reframes, separated by | like this:
[growth reframe]|[abundance reframe]|[get-to reframe]"""

            # Call OpenAI API
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a thoughtful mindset coach who helps people reframe negative thoughts."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            ai_text = response.choices[0].message.content
            
            # Split by | to get the three reframes
            reframes = [r.strip() for r in ai_text.split("|")]
            
            if len(reframes) >= 3:
                growth = reframes[0]
                abundance = reframes[1]
                get_to = reframes[2]
                
                st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Growth Mindset:</b> {growth}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Abundance Mindset:</b> {abundance}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Get-to Mindset:</b> {get_to}</div>", unsafe_allow_html=True)

                # Download option
                reframed_text = f"Growth Mindset: {growth}\nAbundance Mindset: {abundance}\nGet-to Mindset: {get_to}"
                st.download_button(
                    "Download Your Reframes", 
                    reframed_text, 
                    file_name="mindset_reframes.txt"
                )
            else:
                # If format is unexpected, show what we got
                st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'>{ai_text}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.warning("⚠️ AI service temporarily unavailable. Using smart template reframing...")
            
            # --- TEMPLATE FALLBACK ---
            original = user_statement.strip()
            statement_lower = original.lower()

            growth_reframes = []
            abundance_reframes = []
            getto_reframes = []

            if "have to" in statement_lower:
                base = original.lower().replace("have to", "")
                growth_reframes = [
                    f"Choosing to{base} helps me build discipline and commitment.",
                    f"Each time I{base}, I'm developing valuable skills.",
                    f"By taking ownership of{base}, I'm investing in my growth."
                ]
                abundance_reframes = [
                    f"I get to{base} – which creates opportunities I haven't imagined yet.",
                    f"Instead of obligation, I see opportunity: I get to{base}.",
                    f"The fact that I get to{base} means possibilities are opening."
                ]
                getto_reframes = [
                    f"I get to{base} – not everyone has this opportunity.",
                    f"What a privilege that I get to{base}.",
                    f"I'm grateful I get to{base}."
                ]
            elif "can't" in statement_lower or "cannot" in statement_lower:
                growth_reframes = [
                    f"I haven't learned how to do this yet, but I'm on the path.",
                    f"Today {original.lower()}, tomorrow I might surprise myself.",
                    f"What feels impossible now is often tomorrow's breakthrough."
                ]
                abundance_reframes = [
                    f"If one door is closed, I'm curious what other paths are available.",
                    f"This limitation might be redirecting me somewhere better.",
                    f"When {original.lower()}, it often means I need to look at different options."
                ]
                getto_reframes = [
                    f"Even though {original.lower()}, I get to keep learning and trying.",
                    f"I get to have goals that challenge me, even if {original.lower()} right now.",
                    f"The journey matters: I get to work toward this, even if {original.lower()} today."
                ]
            else:
                growth_reframes = [
                    f"Experiencing '{original}' teaches me something about resilience.",
                    f"'{original}' – and I'm learning how I respond to challenges.",
                    f"This situation helps me understand what I need and value."
                ]
                abundance_reframes = [
                    f"Within '{original}' are opportunities I'm starting to see.",
                    f"What seems like '{original}' might be opening unexpected doors.",
                    f"'{original}' – and I'm curious about what else might be true here."
                ]
                getto_reframes = [
                    f"I get to notice '{original}' – that's being present and aware.",
                    f"Even experiencing '{original}' is part of being fully alive.",
                    f"I get to feel and observe '{original}' in this moment."
                ]

            growth = random.choice(growth_reframes)
            abundance = random.choice(abundance_reframes)
            get_to = random.choice(getto_reframes)

            st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='reframe-box'><b>Growth Mindset:</b> {growth}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='reframe-box'><b>Abundance Mindset:</b> {abundance}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='reframe-box'><b>Get-to Mindset:</b> {get_to}</div>", unsafe_allow_html=True)

            reframed_text = f"Growth Mindset: {growth}\nAbundance Mindset: {abundance}\nGet-to Mindset: {get_to}"
            st.download_button(
                "Download Your Reframes", 
                reframed_text, 
                file_name="mindset_reframes.txt"
            )

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

# --- IPA LOGO ---
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
_, center_col, _ = st.columns([1, 1, 1])
with center_col:
    st.image("https://i.imgur.com/xG8V4fL.png", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(
    "<div class='footer'>© 2025 Institutional Property Advisors<br>ipausa.com</div>", 
    unsafe_allow_html=True
)
