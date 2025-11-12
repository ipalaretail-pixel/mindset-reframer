import streamlit as st
import requests
import openai
import random

# --- OPENAI SETUP ---
openai.api_key = st.secrets["openai"]["api_key"]
model = "gpt-3.5-turbo"
assert model == "gpt-3.5-turbo", "Wrong model selected!"

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
st.markdown("<h1 style='text-align:center;'>Gratitude, Growth and Abundance<br>Reframe Your Mindset</h1>", unsafe_allow_html=True)
st.write("What's on your mind today? Type in something you're dreading, a frustration that's been nagging you, or just that thing you wish you didn't have to deal with. Let's see it from a different angle.")

# --- INPUT ---
user_statement = st.text_input("Enter your statement:", placeholder="e.g., I have to work through the holidays")

# --- BUTTON TO GENERATE ---
if st.button("Reframe My Mindset", type="primary") and user_statement:
    try:
        # Try AI-powered reframing
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a mindset coach. Reframe the user's statement into Growth, Abundance, and Get-to perspectives. Provide 3 short reframes for each mindset."},
                {"role": "user", "content": user_statement}
            ],
            max_tokens=400
        )
        ai_text = response.choices[0].message["content"]
        st.markdown("### AI-Powered Reframe")
        st.write(ai_text)

    except Exception:
        st.info("⚠️ Using template-based reframing instead...")
        
        # --- TEMPLATE FALLBACK ---
        original = user_statement.strip()
        statement_lower = original.lower()

        # Enhanced patterns
        patterns = {
            "have to": "Choosing to",
            "can't": "I haven't learned yet",
            "hate": "This teaches me resilience",
            "wish I didn't": "This is an opportunity to grow",
            "stuck with": "This helps me practice patience"
        }

        growth_reframes, abundance_reframes, getto_reframes = [], [], []

        # Detect patterns
        if "have to" in statement_lower:
            base = original.lower().replace("have to", "")
            growth_reframes = [
                f"Choosing to{base} helps me build discipline.",
                f"Each time I{base}, I'm developing valuable skills.",
                f"By taking ownership of{base}, I'm investing in my growth."
            ]
            abundance_reframes = [
                f"I get to{base} – which creates opportunities I haven't imagined yet.",
                f"Instead of obligation, I see: I get to{base}.",
                f"The fact that I get to{base} means possibilities are opening."
            ]
            getto_reframes = [
                f"I get to{base} – not everyone has this opportunity.",
                f"What a privilege that I get to{base}.",
                f"I'm grateful I get to{base}."
            ]
        else:
            # General reframes
            growth_reframes = [
                f"Experiencing '{original}' teaches me resilience.",
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

        # Pick random reframes
        growth = random.choice(growth_reframes)
        abundance = random.choice(abundance_reframes)
        get_to = random.choice(getto_reframes)

        st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='reframe-box'><b>Growth Mindset:</b> {growth}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='reframe-box'><b>Abundance Mindset:</b> {abundance}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='reframe-box'><b>Get-to Mindset:</b> {get_to}</div>", unsafe_allow_html=True)

        # Download option
        reframed_text = f"Growth Mindset: {growth}\nAbundance Mindset: {abundance}\nGet-to Mindset: {get_to}"
        st.download_button("Download Your Reframes", reframed_text, file_name="mindset_reframes.txt")
