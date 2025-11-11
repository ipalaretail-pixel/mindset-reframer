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
        .loading {{
            text-align: center;
            color: {ELECTRIC_BLUE};
            font-style: italic;
            padding: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align:center;'>Gratitude, Growth and Abundance<br>Reframe Your Mindset</h1>", unsafe_allow_html=True)
st.write("What's on your mind today? Type in something you're dreading, a frustration that's been nagging you, or just that thing you wish you didn't have to deal with. Let's see it from a different angle.")

# --- INPUT ---
user_statement = st.text_input("Enter your statement:", placeholder="e.g., I have to work through the holidays")

# --- AI-POWERED REFRAME FUNCTION ---
async def reframe_with_ai(statement):
    """Use Claude API to generate thoughtful, contextual reframes"""
    
    prompt = f"""You are a thoughtful coach helping someone reframe a negative or draining thought into three different positive perspectives. The person said: "{statement}"

Please provide three distinct reframes, each 1-2 sentences:

1. GROWTH MINDSET: Focus on learning, development, skills gained, or personal evolution from this situation. Be specific to their statement and authentic - not generic.

2. ABUNDANCE MINDSET: Focus on opportunities, possibilities, what this opens up, or alternative perspectives that reveal more options. Be specific and genuine.

3. GET-TO MINDSET: Focus on gratitude, privilege, or the gift of being able to experience this. Make it feel sincere, not forced.

IMPORTANT: 
- Use their exact words and context from their statement
- Make each reframe feel natural and conversational, not like a template
- Vary your language - don't start every sentence the same way
- Be authentic and human - if something genuinely sucks, acknowledge it while still reframing
- Keep it concise - 1-2 sentences each
- DO NOT include labels like "Growth Mindset:" in your response
- DO NOT use quotation marks around their statement

Respond with ONLY the three reframes, separated by | like this:
[growth reframe]|[abundance reframe]|[get-to reframe]"""

    try:
        response = await fetch("https://api.anthropic.com/v1/messages", {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json",
            },
            "body": JSON.stringify({
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 500,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            })
        })
        
        data = await response.json()
        reframes_text = data.content[0].text
        
        # Split by | to get the three reframes
        reframes = reframes_text.split("|")
        
        if len(reframes) == 3:
            return reframes[0].strip(), reframes[1].strip(), reframes[2].strip()
        else:
            # Fallback if format is unexpected
            return (
                "This experience is shaping you in ways you'll appreciate later.",
                "There might be unexpected opportunities hidden in this situation.",
                "You get to face this challenge - that's part of being fully alive."
            )
            
    except Exception as e:
        st.error(f"Having trouble connecting. Please try again. ({str(e)})")
        return None, None, None

# --- OUTPUT ---
if user_statement:
    with st.spinner("Reframing your perspective..."):
        import asyncio
        
        # Run the async function
        try:
            growth, abundance, get_to = asyncio.run(reframe_with_ai(user_statement))
            
            if growth and abundance and get_to:
                st.markdown("<h3>Your Reframed Statements:</h3>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Growth Mindset:</b> {growth}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Abundance Mindset:</b> {abundance}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='reframe-box'><b>Get-to Mindset:</b> {get_to}</div>", unsafe_allow_html=True)

                # Download option
                reframed_text = f"Growth Mindset: {growth}\nAbundance Mindset: {abundance}\nGet-to Mindset: {get_to}"
                st.download_button("Download Your Reframes", reframed_text, file_name="mindset_reframes.txt")
        except Exception as e:
            st.error("Something went wrong. Please refresh and try again.")

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
