import streamlit as st
import sys
from pathlib import Path

# Ajouter le dossier racine au PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

# Configuration de la page
st.set_page_config(
    page_title="Mini SOC Intelligent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Global Premium
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap');

    * { font-family: 'Inter', sans-serif; }

    .stApp {
        background: linear-gradient(135deg, #020c1b 0%, #0a192f 50%, #020c1b 100%);
        color: #ccd6f6;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1b2a 0%, #0a192f 100%);
        border-right: 1px solid #1e2a45;
    }
    section[data-testid="stSidebar"] > div { padding-top: 1rem; }

    /* Boutons */
    .stButton > button {
        background: linear-gradient(135deg, #1a2744, #0d1b2a);
        color: #ccd6f6;
        border: 1px solid #1e3a5f;
        border-radius: 8px;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        border-color: #00d4ff;
        color: #00d4ff;
        background: linear-gradient(135deg, #0a2540, #0d1b2a);
        transform: translateY(-1px);
        box-shadow: 0 4px 20px #00d4ff22;
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #1a56db, #1e40af);
        border-color: #3b82f6;
        color: white;
        font-weight: 600;
    }
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        transform: translateY(-2px);
        box-shadow: 0 6px 24px #3b82f644;
    }

    /* Inputs */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        background-color: #0d1b2a;
        border: 1px solid #1e3a5f;
        color: #ccd6f6;
        border-radius: 8px;
    }
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #00d4ff;
        box-shadow: 0 0 0 2px #00d4ff22;
    }

    /* Forms */
    .stForm { background: transparent; border: none; }
    .stForm > div { background: transparent; }

    /* Expander */
    .streamlit-expanderHeader {
        background: #0d1b2a;
        border: 1px solid #1e3a5f;
        border-radius: 8px;
        color: #ccd6f6;
    }
    .streamlit-expanderContent {
        background: #080f1a;
        border: 1px solid #1e3a5f;
        border-top: none;
        border-radius: 0 0 8px 8px;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: #0d1b2a;
        border-radius: 12px;
        padding: 0.3rem;
        gap: 0.3rem;
    }
    .stTabs [data-baseweb="tab"] {
        color: #8892b0;
        background: transparent;
        border-radius: 8px;
        font-weight: 500;
        padding: 0.5rem 1.5rem;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #1a2744, #1e3a5f) !important;
        color: #00d4ff !important;
    }

    /* Metric */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #0d1b2a, #0a192f);
        border: 1px solid #1e3a5f;
        border-radius: 10px;
        padding: 1rem;
    }
    [data-testid="metric-container"] label { color: #8892b0; }
    [data-testid="metric-container"] [data-testid="metric-value"] {
        color: #ccd6f6;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Dataframe */
    .stDataFrame { border-radius: 10px; overflow: hidden; }

    /* Spinner */
    .stSpinner > div { border-color: #00d4ff transparent transparent transparent; }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #0a192f; }
    ::-webkit-scrollbar-thumb { background: #1e3a5f; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #00d4ff; }

    /* Hide Streamlit branding */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 1.5rem 0;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🛡️</div>
        <h1 style="color: #00d4ff; font-size: 1.3rem; margin: 0; font-weight: 800;
                   font-family: 'Inter', sans-serif; letter-spacing: 0.05em;">
            MINI SOC INTELLIGENT
        </h1>
        <p style="color: #4a6fa5; font-size: 0.75rem; margin: 0.3rem 0 0 0; letter-spacing: 0.1em;">
            SECURITY OPERATIONS CENTER
        </p>
    </div>
    <hr style="border-color: #1e2a45; margin: 0 0 1.5rem 0;">
    """, unsafe_allow_html=True)

    # Indicateurs de statut des services
    st.markdown("**⚙️ Statut des Services**")

    import requests
    def check_service(url, name, color):
        try:
            r = requests.get(url, timeout=3)
            status = "🟢 En ligne" if r.status_code == 200 else "🔴 Erreur"
        except:
            status = "🔴 Hors ligne"
        st.markdown(f"""
        <div style="background: #0d1b2a; border-radius: 8px; padding: 0.5rem 0.8rem;
                    margin: 0.3rem 0; display: flex; justify-content: space-between;
                    border: 1px solid #1e2a45;">
            <span style="color: #8892b0; font-size: 0.82rem;">{name}</span>
            <span style="font-size: 0.82rem;">{status}</span>
        </div>
        """, unsafe_allow_html=True)

    check_service("http://localhost:8000/health", "FastAPI Backend", "#00d4ff")
    check_service("http://localhost:11434", "Ollama LLM", "#a78bfa")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**📦 Technologies**")
    tech_list = [
        ("🔍", "LightGBM", "Détection DDoS"),
        ("🧠", "LangChain + FAISS", "Chatbot RAG"),
        ("🤖", "Ollama Llama3", "LLM Local"),
        ("🗄️", "PostgreSQL", "Base de Données"),
        ("⚡", "FastAPI", "API Backend"),
        ("📧", "SMTP Gmail", "Alertes Email"),
    ]
    for icon, name, desc in tech_list:
        st.markdown(f"""
        <div style="padding: 0.3rem 0; border-bottom: 1px solid #1e2a4522;">
            <span style="font-size: 1rem;">{icon}</span>
            <span style="color: #ccd6f6; font-size: 0.82rem; font-weight: 600; margin-left: 0.4rem;">{name}</span>
            <span style="color: #4a6fa5; font-size: 0.75rem; display: block; margin-left: 1.6rem;">{desc}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #0d1b2a; border-radius: 8px; padding: 0.8rem;
                border: 1px solid #1e2a45; font-size: 0.75rem; color: #4a6fa5;">
        📧 <strong style="color: #8892b0;">Alertes SOC</strong><br>
        De : feryelifaoui@gmail.com<br>
        À : moncefifaoui0@gmail.com
    </div>
    """, unsafe_allow_html=True)

# ── Navigation Principale ───────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "  📊  Dashboard SOC  ",
    "  🧠  Chatbot RAG  ",
    "  🤖  Agent IA SOC  ",
])

from frontend.views.dashboard_view import render_dashboard
from frontend.views.chatbot_view import render_chatbot
from frontend.views.agent_view import render_agent

with tab1:
    render_dashboard()

with tab2:
    render_chatbot()

with tab3:
    render_agent()
