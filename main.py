import streamlit as st
import os

# Konfiguracja strony
st.set_page_config(page_title="💕 Walentynka 💕", layout="centered")

# Stylizacja CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #ff69b4 0%, #ff1493 100%);
    }
    .main {
        padding: 50px 20px;
    }
    .title-container {
        text-align: center;
        padding: 40px 20px;
    }
    .title-text {
        font-size: 48px;
        color: white;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 40px;
        flex-wrap: wrap;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicjalizacja stanu sesji
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

# Nagłówek z sercami
st.markdown("""
    <div style="text-align: center; font-size: 40px; margin-bottom: 20px;">
    💕 💕 💕
    </div>
    """, unsafe_allow_html=True)

# Główny tytuł (tylko jeśli nie kliknięto NIE 5 razy)
if st.session_state.no_clicks < 5:
    st.markdown("""
        <div class="title-container">
            <div class="title-text">
            Czy zostaniesz moją walentynką?
            </div>
        </div>
        """, unsafe_allow_html=True)

# Wyświetlanie przycisków tylko jeśli nie kliknięto NIE 5 razy
if st.session_state.no_clicks < 5:
    # Przyciskowy layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # Obliczanie rozmiaru przycisków
    no_width = max(1, 10 - st.session_state.no_clicks)
    yes_width = 10
    
    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        
        # Używamy dynamicznych kolumn zamiast CSS scale
        button_col1, button_col2 = st.columns([yes_width, no_width])
        
        with button_col1:
            if st.button("TAK", key="yes_button", use_container_width=True):
                st.session_state.yes_clicked = True
                st.session_state.no_clicks = 0
                st.rerun()
        
        with button_col2:
            if st.button("NIE", key="no_button", use_container_width=True):
                st.session_state.no_clicks += 1
                st.session_state.yes_clicked = False
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)

# Wyświetlanie obrazów
st.markdown("<br>", unsafe_allow_html=True)

if st.session_state.yes_clicked:
    st.markdown("""
        <div style='text-align: center; color: white; font-size: 24px; font-weight: bold; margin-bottom: 20px;'>
        ❤️ YESSSS! ❤️
        </div>
        """, unsafe_allow_html=True)
    
    # Sprawdzenie czy plik istnieje
    yes_image_path = "yes_image.png"  # Zmień na właściwą ścieżkę
    if os.path.exists(yes_image_path):
        st.image(yes_image_path, use_container_width=True)
    else:
        st.info("📸 Tutaj pojawi się zdjęcie po kliknięciu TAK!\n\nUmieść plik 'yes_image.png' w katalogu projektu")

elif st.session_state.no_clicks >= 5:
    # Sprawdzenie czy plik istnieje
    no_image_path = "pork.jpg"  # Zmienione na pork.jpg
    if os.path.exists(no_image_path):
        st.image(no_image_path, width=400)
    else:
        st.info("📸 Tutaj pojawi się zdjęcie po 5 kliknięciach NIE!\n\nUmieść plik 'pork.jpg' w katalogu projektu")


# Stopka z sercami
st.markdown("""
    <div style="text-align: center; font-size: 40px; margin-top: 60px;">
    💕 💕 💕
    </div>
    """, unsafe_allow_html=True)
