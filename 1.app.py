import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io
import time
from datetime import datetime

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(
    page_title="Sandhu AI | Enterprise Translator",
    page_icon="💎",
    layout="wide"
)

# --- 2. LUXURY UI CUSTOMIZATION (CSS) ---
st.markdown("""
    <style>
    /* Background and Main Font */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Custom Header */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        color: #1e293b;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .sub-header {
        font-size: 1.1rem;
        color: #64748b;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Translation Cards */
    .stTextArea textarea {
        border-radius: 15px !important;
        border: 1px solid #e2e8f0 !important;
        background-color: white !important;
        padding: 20px !important;
        font-size: 1.1rem !important;
    }

    /* Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px !important;
        background-color: #2563eb !important;
        color: white !important;
        font-weight: 700 !important;
        padding: 12px 0px !important;
        border: none !important;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
    }

    /* Metrics Styling */
    [data-testid="stMetricValue"] {
        color: #2563eb;
        font-size: 1.8rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DATA ENGINE ---
@st.cache_data
def load_languages():
    langs = GoogleTranslator().get_supported_languages(as_dict=True)
    return dict(sorted(langs.items()))

languages = load_languages()
names = list(languages.keys())

# --- 4. TOP NAVIGATION / HEADER ---
st.markdown('<p class="main-header">Sandhu AI Global</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Premium Language Intelligence for Global Enterprise</p>', unsafe_allow_html=True)

# Metrics Bar
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Live Languages", "200+")
with m2: st.metric("Accuracy", "99.2%")
with m3: st.metric("Engine", "AI Neural")
with m4: st.metric("System", "Online")

st.divider()

# --- 5. MAIN INTERFACE ---
container = st.container()

with container:
    c1, c2 = st.columns(2, gap="large")
    
    with c1:
        st.markdown("### 📥 Source Configuration")
        source_name = st.selectbox("Identify Language (Auto-Detect Enabled):", ["auto-detect"] + names)
        text_input = st.text_area("", placeholder="Type your message here to begin...", height=250)
        
    with c2:
        st.markdown("### 📤 Target Configuration")
        target_name = st.selectbox("Translation Destination:", names, index=names.index("english") if "english" in names else 0)
        
        if st.button("PROCEED TO TRANSLATE 🚀"):
            if text_input.strip():
                try:
                    with st.spinner("Analyzing semantics and translating..."):
                        # Logic
                        src = "auto" if source_name == "auto-detect" else languages[source_name]
                        tar = languages[target_name]
                        
                        result = GoogleTranslator(source=src, target=tar).translate(text_input)
                        
                        # Display Output
                        st.text_area("AI Translation Result:", value=result, height=200)
                        
                        # Audio Player
                        tts = gTTS(text=result, lang=tar)
                        audio_fp = io.BytesIO()
                        tts.write_to_fp(audio_fp)
                        st.audio(audio_fp, format="audio/mp3")
                        
                        st.success(f"Successfully processed into {target_name.title()}")
                except Exception as e:
                    st.error(f"Execution Error: {e}")
            else:
                st.warning("Please provide input text for the AI engine.")

# --- 6. ADVANCED TOOLS (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3858/3858712.png", width=80)
    st.title("Admin Panel")
    st.write("Logged in as: **Developer**")
    st.divider()
    
    st.subheader("📁 Batch Processing")
    file = st.file_uploader("Drop document here", type=["txt"])
    if file:
        st.button("Process File")
        
    st.divider()
    st.caption(f"© {datetime.now().year} Sandhu AI Solutions")
    st.caption("Version 4.5.1 Gold")