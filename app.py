import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

# 1. Configurazione Pagina
st.set_page_config(page_title="BREACHMAS_2025", page_icon="💀", layout="centered")

# --- CSS LOOK TERMINALE E PIOGGIA FUNZIONANTE ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; overflow-x: hidden; }
    header, footer, #MainMenu {visibility: hidden;}
    
    .log-text {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 20px !important; 
        line-height: 1.8;
        position: relative;
        z-index: 100;
    }
    
    /* La pioggia di bit (0 1 X M A S 2 0 2 5) */
    .matrix-rain {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        pointer-events: none; z-index: 1;
    }
    .bit {
        position: absolute; top: -30px;
        font-family: monospace; font-size: 18px;
        animation: fall linear infinite;
    }
    @keyframes fall { to { transform: translateY(110vh); } }
    
    /* Nasconde player audio */
    div[data-testid="stAudio"] { position: fixed; bottom: -100px; }
    </style>
    """, unsafe_allow_html=True)

def find_file(name):
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.lower() == name.lower():
                return os.path.join(root, f)
    return None

def get_audio_b64(file_path):
    if file_path and os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def play_audio_b64(b64_string):
    if b64_string:
        audio_html = f"""
            <audio autoplay="true" style="display:none;">
                <source src="data:audio/mp3;base64,{b64_string}" type="audio/mp3">
            </audio>
        """
        components.html(audio_html, height=0, width=0)

def start_cyber_rain():
    import random
    cols = 120
    html_bits = '<div class="matrix-rain">'
    for i in range(cols):
        left = i * 2.5
        duration = random.uniform(2, 6)
        delay = random.uniform(0, 4)
        color = "#00FF41" if i % 2 == 0 else "#FF0000"
        char = random.choice(["0", "1", "X", "M", "A", "S", "2", "0", "2", "5"])
        html_bits += f'<div class="bit" style="left:{left}%; color:{color}; animation-duration:{duration}s; animation-delay:{delay}s;">{char}</div>'
    html_bits += '</div>'
    st.markdown(html_bits, unsafe_allow_html=True)

def main():
    if 'authorized' not in st.session_state:
        st.session_state.authorized = False

    if not st.session_state.authorized:
        st.markdown('<div class="log-text">SYSTEM: CACTUS_SERVER<br>DATE: 25-12-2025<br>STATUS: ENCRYPTED</div>', unsafe_allow_html=True)
        if st.button("RUN EXPLOIT"):
            st.session_state.authorized = True
            st.rerun()
    else:
        # 1. Modem Audio
        modem_b64 = get_audio_b64(find_file("modem.mp3"))
        play_audio_b64(modem_b64)

        log_placeholder = st.empty()
        full_log = ""
        
        # Sequenza log sincronizzata (26 secondi circa)
        steps = [
            ("> Dialing 01010011...", 2.5),
            ("> Carrier detected...", 1.5),
            ("> Handshake: V.90 Protocol...", 6.0),
            ("> Bypassing IDS/IPS...", 4.5),
            ("> Escalating to root...", 3.5),
            ("> Accessing secret_payload...", 3.0),
            ("> Decrypting visual data...", 2.0),
        ]

        for text, delay in steps:
            full_log += text + "<br>"
            log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
            time.sleep(delay)

        # Caricamento musica rock durante l'ultimo log
        full_log += "> Executing payload...<br>"
        log_placeholder.markdown(f'<div class="log-text">{full_log}</div>', unsafe_allow_html=True)
        rock_b64 = get_audio_b64(find_file("musica.mp3"))
        time.sleep(3.0) 

        # --- AZIONE FINALE ---
        play_audio_b64(rock_b64)
        start_cyber_rain()

        # Visualizza ascii.png invece del testo
        ascii_path = find_file("ascii.png")
        if ascii_path:
            st.image(ascii_path, use_container_width=True)
        
        st.success("SUCCESS: Buon Natale, Locandieri!")

        # Visualizza la foto finale (foto.png)
        img_path = find_file("foto.png")
        if img_path:
            st.image(img_path, use_container_width=True)
        
        st.markdown('<div class="log-text">root@cactus_server:~# _</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

