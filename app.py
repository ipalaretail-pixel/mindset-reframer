import streamlit as st
import random

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

# --- DYNAMIC REFRAME FUNCTION WITH MORE VARIETY ---
def reframe_statement(statement):
    original = statement.strip()
    statement_lower = original.lower()
    
    # GROWTH MINDSET VARIATIONS (10+ options per category)
    growth_templates = []
    if "have to" in statement_lower:
        replaced = original.lower().replace("have to", "choose to")
        growth_templates = [
            f"I {replaced} because it helps me develop new skills.",
            f"By choosing to {replaced.replace('i choose to ', '')}, I'm investing in my growth.",
            f"I {replaced}, and each time I do, I become more capable.",
            f"Reframing this: I {replaced} - and that's building my character.",
            f"I {replaced}, which means I'm taking ownership of my development.",
            f"When I {replaced}, I'm actively shaping who I'm becoming.",
            f"I {replaced} - this is how I practice discipline and commitment.",
            f"By deciding to {replaced.replace('i choose to ', '')}, I strengthen my resilience.",
            f"I {replaced}, learning something valuable each time.",
            f"Choosing means growing: I {replaced} to expand my capabilities."
        ]
    elif "can't" in statement_lower:
        growth_templates = [
            f"I haven't mastered this yet, but '{original.lower()}' is part of my learning journey.",
            f"Right now {original.lower()}, but I'm developing the skills to change that.",
            f"What feels like '{original.lower()}' today is tomorrow's breakthrough waiting to happen.",
            f"'{original}' - yet. I'm still growing into this capability.",
            f"Today {original.lower()}, but every expert was once a beginner.",
            f"I'm in the 'not yet' phase of learning this - {original.lower()} is temporary.",
            f"'{original}' right now, but I'm building toward it step by step.",
            f"This feeling that {original.lower()} shows me exactly where my growth edge is.",
            f"I {original.lower()} today, but I'm curious about what I'll learn on the path to getting there.",
            f"'{original}' - which means I've identified my next area for development."
        ]
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed", "dreading", "hate", "don't want"]):
        growth_templates = [
            f"While {original.lower()}, I'm discovering what I need to adjust and improve.",
            f"This feeling that {original.lower()} is teaching me about my boundaries and resilience.",
            f"Even though {original.lower()}, I'm learning how to navigate difficult emotions.",
            f"Experiencing that {original.lower()} shows me where I can grow stronger.",
            f"When {original.lower()}, I'm getting valuable data about what matters to me.",
            f"Though {original.lower()}, this discomfort is information I can use.",
            f"I notice that {original.lower()} - and noticing is the first step to change.",
            f"Feeling that {original.lower()} helps me understand what I value and need.",
            f"While {original.lower()}, I'm building emotional intelligence and self-awareness.",
            f"Even as {original.lower()}, I'm practicing resilience in real-time."
        ]
    else:
        growth_templates = [
            f"'{original}' - this situation is teaching me something valuable about adaptability.",
            f"Noticing that '{original.lower()}' helps me understand how I respond to challenges.",
            f"What seems like '{original.lower()}' is actually an opportunity to practice resilience.",
            f"'{original}' might be uncomfortable, but discomfort often signals growth.",
            f"Observing that '{original.lower()}' gives me insight into my patterns.",
            f"'{original}' - and paying attention to this is how I learn.",
            f"This experience of '{original.lower()}' is building my capacity to handle complexity.",
            f"When '{original.lower()},' I get to practice responding intentionally.",
            f"'{original}' presents a chance to develop skills I'll use again.",
            f"Recognizing that '{original.lower()}' is the beginning of adapting to it."
        ]
    
    # ABUNDANCE MINDSET VARIATIONS (10+ options per category)
    abundance_templates = []
    if "have to" in statement_lower:
        replaced = original.lower().replace("have to", "get to")
        abundance_templates = [
            f"I {replaced} - which means new doors are opening for me.",
            f"Instead of obligation, I see opportunity: I {replaced}.",
            f"I {replaced}, and this creates possibilities I haven't even imagined yet.",
            f"Shifting perspective: I {replaced}, which expands what's available to me.",
            f"I {replaced} - this is abundance showing up in my life.",
            f"Rather than scarcity thinking, I recognize: I {replaced}.",
            f"I {replaced}, and with that comes unexpected opportunities.",
            f"Flipping the script: I {replaced}, opening paths I didn't know existed.",
            f"I {replaced} - each obligation is really an invitation to more.",
            f"When I realize I {replaced}, I see how much is actually available to me."
        ]
    elif "can't" in statement_lower:
        abundance_templates = [
            f"While right now {original.lower()}, there are multiple paths I haven't explored yet.",
            f"What feels like '{original.lower()}' is redirecting me toward something better aligned.",
            f"I may not be able to do it that way, but '{original.lower()}' opens up alternative routes.",
            f"Rather than limitation, '{original.lower()}' reveals unexplored opportunities.",
            f"Today {original.lower()}, but the universe might be steering me somewhere better.",
            f"If {original.lower()} this way, perhaps there's an even better way waiting.",
            f"'{original}' - which frees me up to discover options I hadn't considered.",
            f"Not being able to do it one way means I {original.lower()} - yet - but I'm open to alternatives.",
            f"When {original.lower()}, it often means I'm being redirected to abundance elsewhere.",
            f"'{original}' on this path, so maybe there's a more abundant path for me."
        ]
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed", "dreading", "hate", "don't want"]):
        abundance_templates = [
            f"Though {original.lower()}, this redirects my energy toward what truly matters.",
            f"Instead of being stopped by feeling that {original.lower()}, I can see what else is available to me.",
            f"When {original.lower()}, it's often because better opportunities are waiting.",
            f"Rather than dwelling on how {original.lower()}, I can look for what's opening up.",
            f"Even while {original.lower()}, there's something valuable trying to emerge.",
            f"If {original.lower()}, maybe I'm being pointed toward something more aligned.",
            f"Though {original.lower()}, I trust there's opportunity in this moment I haven't noticed yet.",
            f"Feeling that {original.lower()} might be clearing space for something better.",
            f"When {original.lower()}, I remember: this too is part of an abundant life.",
            f"While {original.lower()}, I'm curious about what possibilities this is creating."
        ]
    else:
        abundance_templates = [
            f"Beyond just noticing '{original.lower()},' I see this moment is full of possibility.",
            f"'{original}' - and within this situation are opportunities I'm beginning to recognize.",
            f"What appears as '{original.lower()}' could be pointing me toward something valuable.",
            f"Instead of accepting that '{original.lower()},' I'm curious about what else might be true.",
            f"'{original}' - and I trust there's more here than meets the eye.",
            f"Observing '{original.lower()}' reminds me that life is full of unexpected gifts.",
            f"'{original}' might seem simple, but there's abundance in every moment.",
            f"When '{original.lower()},' I remember there's always more available than I first see.",
            f"'{original}' - and I'm open to discovering the opportunity within it.",
            f"Even noticing '{original.lower()}' shows me I'm alive to possibility."
        ]
    
    # GET-TO MINDSET VARIATIONS (10+ options per category)
    getto_templates = []
    if "have to" in statement_lower:
        replaced = original.lower().replace("have to", "get to")
        getto_templates = [
            f"I {replaced} - what a gift to have this opportunity.",
            f"I {replaced}, and I'm genuinely grateful this is possible for me.",
            f"Reframed: I {replaced}. Not everyone has this chance.",
            f"I {replaced} - and I don't take that privilege for granted.",
            f"I {replaced} - this is something I'm lucky to experience.",
            f"What privilege: I {replaced}.",
            f"I {replaced}, and that's something to be thankful for.",
            f"I {replaced} - many people wish they had this opportunity.",
            f"How fortunate that I {replaced}.",
            f"I {replaced} - I'm grateful my life includes this possibility."
        ]
    elif "can't" in statement_lower:
        getto_templates = [
            f"Even though right now {original.lower()}, I get to work toward it, and that's meaningful.",
            f"Today {original.lower()}, but I get to be on a journey toward it.",
            f"While {original.lower()} yet, I appreciate that I get to keep trying.",
            f"I {original.lower()} at this moment, but I get to have the desire and the path forward.",
            f"Though {original.lower()}, I get to dream about it and work toward it.",
            f"Right now {original.lower()}, but I get to have goals that inspire me.",
            f"I {original.lower()} today, but I get to be someone who reaches for more.",
            f"Even if {original.lower()}, I get to be on a growth journey.",
            f"While {original.lower()}, I'm grateful I get to aspire to it.",
            f"Though {original.lower()} right now, I get to imagine and pursue it."
        ]
    elif any(word in statement_lower for word in ["stuck", "frustrated", "annoyed", "tired", "stressed", "dreading", "hate", "don't want"]):
        getto_templates = [
            f"Even when {original.lower()}, I get to feel deeply and be human.",
            f"Though {original.lower()}, I get to experience the full range of what life offers.",
            f"Yes, {original.lower()}, and I get to learn from every emotion I experience.",
            f"When {original.lower()}, I remember I get to face challenges rather than avoid life.",
            f"While {original.lower()}, I get to be alive and aware.",
            f"Though {original.lower()}, I get to show up for my life exactly as it is.",
            f"Even as {original.lower()}, I get to be present in this moment.",
            f"When {original.lower()}, I'm reminded I get to feel everything - that's being alive.",
            f"Though {original.lower()}, I get to practice responding with grace.",
            f"While {original.lower()}, I get to be someone who experiences life fully."
        ]
    else:
        getto_templates = [
            f"Noticing '{original.lower()}' reminds me I get to be present and aware.",
            f"'{original}' - and I get to experience this moment, whatever it brings.",
            f"I get to observe that '{original.lower()}' and respond with intention.",
            f"Even just recognizing that '{original.lower()}' means I get to be mindful right now.",
            f"'{original}' - I get to witness life as it unfolds.",
            f"Seeing that '{original.lower()}' is a gift of awareness.",
            f"'{original}' - and I get to be conscious of it.",
            f"I get to notice '{original.lower()}' - that's the privilege of being present.",
            f"'{original}' - I get to experience this part of life too.",
            f"Observing '{original.lower()}' reminds me I get to show up fully for my life."
        ]
    
    # Pick random variation from each list
    growth = random.choice(growth_templates)
    abundance = random.choice(abundance_templates)
    get_to = random.choice(getto_templates)
    
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
