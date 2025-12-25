import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="wide")

# 2. CSS: Sfondo nero, log verdi grandi e pioggia sullo sfondo
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow-x: hidden; }
    
    /* Forza l'iframe della pioggia a stare dietro tutto */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important;
        border: none !important;
    }

    /* Rende il contenuto di Streamlit trasparente per vedere la pioggia */
    .main .block-container {
        background-color: transparent !important;
        max-width: 100% !important;
        padding-top: 1.5rem !important;
    }

    /* LOG: Grandi e nitidi (22px) */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 22px !important; 
        line-height: 1.6 !important;
        text-shadow: 0 0 5px #00FF41;
        margin-bottom: 10px !important;
    }
    
    /* Nasconde player audio */
    div[data-testid="stAudio"] { position: fixed; bottom: -100px; opacity: 0; }
    header, footer, #MainMenu { visibility: hidden; }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower(): return os.path.join(root, f)
    return None

def play_audio(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            audio_html = f"""
                <audio autoplay="true" style="display:none;">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
            """
            components.html(audio_html, height=0)

# FUNZIONE PIOGGIA: 0, 1, X, M, A, S (Verde e Rosso)
def start_matrix_rain():
    js_code = """
    <body style="margin: 0; background: black; overflow: hidden;">
    <canvas id="q"></canvas>
    <script>
    var q = document.getElementById('q'),
        s = window.screen,
        w = q.width = s.width,
        h = q.height = s.height,
        p = Array(256).join(1).split(''),
        c = "010101XMAS",
        ctx = q.getContext('2d');

    function draw() {
        ctx.fillStyle = 'rgba(0,0,0,0.1)';
        ctx.fillRect(0, 0, w, h);
        p.map(function(v, i) {
            ctx.fillStyle = Math.random() > 0.5 ? '#00FF41' : '#FF0000';
            ctx.font = '18px monospace';
            ctx.fillText(c.charAt(Math.floor(Math.random() * c.length)), i * 15, v);
            p[i] = v > h + Math.random() * 1000 ? 0 : v + 15;
        });
    }
    setInterval(draw, 35);
    </script>
    </body>
    """
    components.html(js_code)

# --- LOGICA APPLICAZIONE ---

if 'authorized' not in st.session_state:
    st.session_state.authorized = False

if not st.session_state.authorized:
    st.markdown('<div class="log-text">SYSTEM: CACTUS_SERVER<br>DATE: 25-12-2025<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
    if st.button("RUN EXPLOIT"):
        st.session_state.authorized = True
        st.rerun()
else:
    # 1. MODEM (Parte subito, dura 26s)
    play_audio(find_file("modem.mp3"))

    log_area = st.empty()
    full_log = ""
    
    # Lista step sincronizzata (Totale circa 26 secondi)
    steps = [
        ("> Dialing 01010011...", 2.5),
        ("> Carrier detected...", 1.5),
        ("> Handshake: V.90 Protocol...", 6.0),
        ("> Bypassing IDS/IPS...", 4.5),
        ("> Escalating to root...", 3.5),
        ("> Accessing secret_payload...", 3.0),
        ("> Decrypting visual data...", 5.0),
    ]

    for text, delay in steps:
        full_log += text + "<br>"
        log_area.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
        time.sleep(delay)

    # --- AZIONE FINALE ---
    start_matrix_rain() # Parte la pioggia sullo sfondo
    play_audio(find_file("musica.mp3")) # Parte la musica Rock
    
    # Visualizza ascii.png
    ascii_path = find_file("ascii.png")
    if ascii_path:
        st.image(ascii_path, use_container_width=True)
    
    st.success("SUCCESS: Buon Natale, Locandieri!")

    # Visualizza foto.png
    foto_path = find_file("foto.png")
    if foto_path:
        st.image(foto_path, use_container_width=True)
    
    st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)
