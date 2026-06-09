"""
SaikAI - Premium Custom Sarvam Theme Implementation
"""

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ─────────────────────────────────────────────
# SECURITY CONFIGURATION & MANAGE KEYS
# ─────────────────────────────────────────────
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if "manual_token" not in st.session_state:
    st.session_state.manual_token = None

effective_token = GITHUB_TOKEN if GITHUB_TOKEN else st.session_state.manual_token

if effective_token:
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key=effective_token,
    )
else:
    client = None

MODEL = "gpt-4o"

# ─────────────────────────────────────────────
# CORE SYSTEM ALIGNMENT PROMPT
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """
You are SaikAI, a semantic parser for a deaf/hard-of-hearing accessibility tool.
Your ONLY job is to extract the core conversational intent tokens from the user's input and return them
as a clean, ordered, comma-separated sequence in UPPERCASE.

Rules:
1. Output ONLY the token sequence — no explanation, no punctuation other than commas.
2. Maps keywords, queries, and questions to their closest actionable visual concept:
   - Queries about eating, dinner, meals, or hunger -> FOOD
   - Queries about locations, directions, or state of being lost -> WHERE
   - Greetings or wellness checks -> HAPPY
   - General support or asking what happened -> HELP
3. Use simple tokens: FOOD, WHERE, HAPPY, SAD, HELP, YES, NO, STOP, GO, WATER, HOME, PHONE, MONEY, SICK, DOCTOR, PLEASE, THANK_YOU, WAIT, ANGRY.
4. Maximum 6 tokens per response.
5. If the input is empty or completely unparseable gibberish, return: UNKNOWN
"""

def parse_intent(user_input: str) -> list[str]:
    if not client:
        return ["UNKNOWN"]
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_input},
            ],
            max_tokens=60,
            temperature=0.2,
        )
        raw = response.choices[0].message.content.strip()
        return [t.strip() for t in raw.split(",") if t.strip()]
    except Exception:
        return ["UNKNOWN"]

# ─────────────────────────────────────────────
# LIGHT THEME UI/UX CSS                     
# ─────────────────────────────────────────────
SARVAM_THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

/* Main Canvas Configurations */
body, .stApp { 
    background-color: #ffffff !important; 
    color: #0a0b10 !important;
    font-family: 'Inter', sans-serif !important;
}

/* Custom Header Navigation Bar Component */
.sarvam-navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 14px 40px;
    border-radius: 100px;
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.02);
}

.navbar-brand {
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: #0a0b10;
}

.navbar-links {
    display: flex;
    gap: 32px;
}

.nav-link {
    font-size: 0.95rem;
    font-weight: 500;
    color: #0a0b10;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    text-decoration: none;
}

.navbar-auth-btn {
    background-color: #1c1e27;
    color: #ffffff;
    padding: 10px 24px;
    border-radius: 100px;
    font-size: 0.95rem;
    font-weight: 600;
    text-decoration: none;
}

/* Interface Structure Panels */
.hero-container {
    text-align: center;
    margin: 3rem 0;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: #0a0b10;
    letter-spacing: -0.03em;
    margin-bottom: 0.5rem;
}

.hero-subtitle {
    font-size: 1.1rem;
    color: #64748b;
}

/* Functional Dashboard Blocks */
.workspace-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 24px;
    padding: 2.5rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.015);
    margin-bottom: 2rem;
}

.card-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0a0b10;
    margin-bottom: 0.2rem;
}

.card-subtitle {
    font-size: 0.95rem;
    color: #64748b;
    margin-bottom: 1.5rem;
}

/* Form Fields & Inputs */
.stTextArea textarea {
    background-color: #f8fafc !important;
    color: #0a0b10 !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 16px !important;
    padding: 18px !important;
    font-size: 16px !important;
}

/* Custom Interactive Buttons */
.stButton button {
    background-color: #ffffff !important;
    color: #0a0b10 !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 100px !important;
    padding: 12px 28px !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

.stButton button:hover {
    border-color: #0a0b10 !important;
    background-color: #f8fafc !important;
}

div.stButton > button[kind="primary"] {
    background: #1c1e27 !important;
    color: #ffffff !important;
    border: none !important;
}

div.stButton > button[kind="primary"]:hover {
    background: #0a0b10 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
}

/* Premium Token Output Capsules */
.token-card {
    display: inline-block;
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
    padding: 0.6rem 1.4rem !important;
    margin: 0.4rem !important;
    border-radius: 100px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.9rem !important;
    font-weight: 700;
    letter-spacing: 0.05em !important;
}

#MainMenu, footer, header {visibility: hidden;}
</style>
"""

TOKEN_COLORS = {
    "HAPPY": "#10b981", "FOOD": "#f59e0b", "HELP": "#ef4444",
    "SAD": "#3b82f6", "UNKNOWN": "#64748b"
}

def render_tokens(tokens: list[str]) -> str:
    cards = ""
    for t in tokens:
        color = TOKEN_COLORS.get(t, "#64748b")
        cards += f'<div class="token-card" style="border-left: 4px solid {color} !important; color: {color} !important;">{t}</div>'
    return f'<div style="text-align:center; margin:1.5rem 0;">{cards}</div>'

def main():
    st.set_page_config(page_title="SaikAI Workspace", page_icon="🤝", layout="centered")
    st.markdown(SARVAM_THEME_CSS, unsafe_allow_html=True)

    # State Configurations
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "app_mode" not in st.session_state:
        st.session_state.app_mode = "Srotra"
    if "last_tokens" not in st.session_state:
        st.session_state.last_tokens = []

    # Replicated Sarvam AI Top Navigation Bar Layout Component
    auth_label = "LOG OUT" if st.session_state.authenticated else "LOG IN"
    st.markdown(f"""
    <div class="sarvam-navbar">
        <div class="navbar-brand">saikAI</div>
        <div class="navbar-links">
            <a class="nav-link" href="#">Platform</a>
            <a class="nav-link" href="#">Developers</a>
            <a class="nav-link" href="#">Resources</a>
        </div>
        <div class="navbar-auth-btn">{auth_label}</div>
    </div>
    """, unsafe_allow_html=True)

    # GATEWAY INTERACTION 1: Mandatory Authentication Portal
    if not st.session_state.authenticated:
        st.markdown('<div class="hero-container"><h1 class="hero-title">Welcome to SaikAI</h1>'
                    '<p class="hero-subtitle">Authentication required to mount processing engines.</p></div>', unsafe_allow_html=True)
        
        col_l, col_c, col_r = st.columns([1, 2, 1])
        with col_c:
            st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
            st.text_input("Username / Email Registration Address", placeholder="name@company.ai")
            st.text_input("Security Access Password", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Authenticate Identity Portal Session", type="primary", use_container_width=True):
                st.session_state.authenticated = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        return

    # GATEWAY INTERACTION 2: Hub Navigation
    st.markdown('<div class="hero-container"><h1 class="hero-title">Workspace Framework</h1>'
                '<p class="hero-subtitle">Select a visual language module to begin translating conversational inputs.</p></div>', unsafe_allow_html=True)

    tab_col1, tab_col2 = st.columns(2)
    with tab_col1:
        if st.button("Srotra \n (Hear.ai)", use_container_width=True, type="primary" if st.session_state.app_mode == "Srotra" else "secondary"):
            st.session_state.app_mode = "Srotra"
            st.session_state.last_tokens = []
            st.rerun()
            
    with tab_col2:
        if st.button("Vadatibru \n (Speak.ai)", use_container_width=True, type="primary" if st.session_state.app_mode == "Vadatibru" else "secondary"):
            st.session_state.app_mode = "Vadatibru"
            st.session_state.last_tokens = []
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Render Active Workspace Module Block
    if st.session_state.app_mode == "Srotra":
        st.markdown(f"""
        <div class="workspace-card">
            <div class="card-header">Srotra Portal Active</div>
            <div class="card-subtitle">Optimized text translation engine for assistive comprehension.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="workspace-card">
            <div class="card-header">Vadatibru Portal Active</div>
            <div class="card-subtitle">Optimized generative sign stream formulation maps.</div>
        </div>
        """, unsafe_allow_html=True)

    user_input = st.text_area(
        "Conversational Stream Input Feed:",
        height=130,
        placeholder="Type conversational sentences or text data streams here...",
        key="main_text_stream"
    )

    action1, action2, action3 = st.columns([2, 2, 1])
    with action1:
        run = st.button("▶ Parse Intent Tokens", use_container_width=True, type="primary")
    with action2:
        if st.button("🔄 Reset Local Environment", use_container_width=True):
            st.session_state.last_tokens = []
            st.rerun()
    with action3:
        if st.button("Sign Out", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    # Inference Execution Processing Pipeline Block
    if run and user_input.strip():
        with st.spinner("Compiling Semantic Vectors..."):
            tokens = parse_intent(user_input)
            st.session_state.last_tokens = tokens

    # Display Intent Results
    if st.session_state.last_tokens:
        st.markdown("<br><h4 style='text-align:center; font-weight:700;'>Generated Intent Vectors</h4>", unsafe_allow_html=True)
        st.markdown(render_tokens(st.session_state.last_tokens), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
