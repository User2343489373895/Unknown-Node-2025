import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="wide")

# 2. CSS DEFINITIVO: Nasconde branding e FORZA la pioggia sullo sfondo totale
st.markdown("""
    <style>
    /* Sfondo Nero Totale */
    .stApp { 
        background-color: #000000; 
        overflow-x: hidden;
    }
    
    /* NASCONDE OGNI TRACCIA DI STREAMLIT CLOUD */
    header, footer, .stAppDeployButton, #MainMenu, .stViewerBadge, 
    #streamlit_share_connect_button, [data-testid="stStatusWidget"],
    [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
    .st-emotion-cache-zq59db, .st-emotion-cache-10trblm {
        display: none !important;
        visibility: hidden !important;
    }

    /* FORZA L'IFRAME DELLA PIOGGIA A TUTTO SCHERMO DIETRO TUTTO */
    iframe[title="matrix_rain_background"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: -1 !important;
        border: none !important;
    }

    /* Rende il contenitore di Streamlit trasparente per vedere la pioggia sotto */
    .main .block-container {
        background-color: transparent !important;
        max-width: 100% !important;
        padding-top: 1rem !important;
        position: relative;
        z-index: 10;
    }

    /* LOG: Grandi e nitidi */
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 22px !important; 
        line-height: 1.5 !important;
        text-shadow: 0 0 5px #00FF41;
        margin-bottom: 10px !important;
    }

    /* Nasconde player audio */
    div[data-testid="stAudio"] { position: fixed; bottom: -100px; opacity: 0; }
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

def play_audio_hidden(b64_string, title):
    if b64_string:
        audio_html = f'<audio autoplay="true" style="display:none;"><source src="data:audio/mp3;base64,{b64_string}" type="audio/mp3"></audio>'
        components.html(audio_html, height=0, width=0, title=title)

# FUNZIONE PIOGGIA: Sincronizzata con lo schermo
def matrix_rain_js():
    js_code = """
    <html>
    <body style="margin: 0; padding: 0; background-color: black; overflow: hidden;">
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
    setInterval(draw, 35);
    </script>
    </body>
    </html>
    """
    # Usiamo un titolo specifico per l'iframe così il CSS lo riconosce
    components.html(js_code, title="matrix_rain_background")

def main():
    if 'authorized' not in st.session_state: st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<div class="log-text">SYSTEM: CACTUS_SERVER<br>DATE: 25-12-2025<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # 1. MODEM (26s)
        modem_b64 = get_audio_b64(find_file("modem.mp3"))
        play_audio_hidden(modem_b64, "modem_audio")

        log_placeholder = st.empty()
        full_log = ""
        
        steps = [
            ("> Dialing 01010011...", 2.5),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90 Protocol...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 3.5),
            ("> Accessing secret_payload...", 3.0),
            ("> Decrypting visual data...", 5.0),
        ]

        for i, (text, delay) in enumerate(steps):
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            if i == 4: rock_b64 = get_audio_b64(find_file("musica.mp3"))
            time.sleep(delay)

        # --- AZIONE FINALE ---
        play_audio_hidden(rock_b64, "rock_audio")
        matrix_rain_js() # Parte la pioggia a tutto schermo

        # Visualizza ascii.png
        ascii_img_path = find_file("ascii.png")
        if ascii_img_path:
            st.image(ascii_img_path, use_container_width=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        # Visualizza foto.png
        foto_path = find_file("foto.png")
        if foto_path:
            st.image(foto_path, use_container_width=True)
        
        st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
