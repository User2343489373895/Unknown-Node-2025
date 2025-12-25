import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="wide")

# 2. CSS DEFINITIVO: Rende TUTTO trasparente e mette la pioggia dietro
st.markdown("""
    <style>
    /* Forza lo sfondo nero di base */
    .stApp {
        background-color: #000000 !important;
    }

    /* RENDE OGNI SINGOLO LIVELLO DI STREAMLIT TRASPARENTE */
    /* Se non facciamo questo, vedrai sempre un 'box' nero che copre la pioggia */
    .stApp, .main, .block-container, [data-testid="stVerticalBlock"], [data-testid="stHorizontalBlock"], .element-container {
        background: transparent !important;
        background-color: transparent !important;
    }

    /* POSIZIONAMENTO IFRAME PIOGGIA (identificato dall'altezza 555) */
    iframe[height="555"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important; /* Dietro a tutto */
        border: none !important;
    }

    /* LOG: Grandi e nitidi (22px) */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 22px !important; 
        line-height: 1.5 !important;
        text-shadow: 0 0 5px #00FF41;
        margin-bottom: 10px !important;
    }

    /* Nasconde player audio e branding Streamlit */
    div[data-testid="stAudio"], iframe[height="0"] { 
        position: fixed; 
        bottom: -100px; 
        opacity: 0; 
    }
    header, footer, #MainMenu, .stDeployButton, .stViewerBadge {
        display: none !important;
        visibility: hidden !important;
    }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower(): return os.path.join(root, f)
    return None

def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def play_audio_hidden(b64_string):
    if b64_string:
        audio_html = f'<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64_string}" type="audio/mp3"></audio>'
        components.html(audio_html, height=0)

# FUNZIONE PIOGGIA: 0, 1, X, M, A, S (Verde e Rosso)
def matrix_rain_js():
    js_code = """
    <html>
    <body style="margin: 0; padding: 0; background: transparent; overflow: hidden;">
    <canvas id="matrix"></canvas>
    <script>
    const canvas = document.getElementById('matrix');
    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    const chars = "010101XMAS";
    const fontSize = 18;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = [];
    for (let i = 0; i < columns; i++) drops[i] = 1;

    function draw() {
        ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < drops.length; i++) {
            const text = chars.charAt(Math.floor(Math.random() * chars.length));
            ctx.fillStyle = (Math.random() > 0.5) ? '#00FF41' : '#FF0000';
            ctx.font = fontSize + 'px monospace';
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);
            
            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }
            drops[i]++;
        }
    }
    setInterv
