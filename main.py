import streamlit as st
import os

# Konfiguracja strony
st.set_page_config(page_title="💕 Walentynka 💕", layout="centered")

# Inicjalizacja stanu sesji (przeniesione na początek)
if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

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
        gap: 20px;
        margin-top: 40px;
        flex-wrap: wrap;
        align-items: center;
    }
    
    /* CSS dla przycisków z lepszym wsparciem mobilnym */
    .stButton > button {
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.3s ease !important;
        min-height: 50px !important;
        min-width: 100px !important;
    }
    
    /* Przycisk TAK */
    .yes-button {
        transform: scale(1) !important;
        background: #28a745 !important;
        color: white !important;
    }
    
    /* Przycisk NIE z dynamicznym skalowaniem */
    .no-button {
        background: #dc3545 !important;
        color: white !important;
        transition: transform 0.3s ease !important;
    }
    
    /* Dodatkowe style dla mobilnych urządzeń */
    @media screen and (max-width: 768px) {
        .stButton > button {
            font-size: 16px !important;
            padding: 10px 20px !important;
            min-height: 45px !important;
        }
        .title-text {
            font-size: 36px !important;
        }
    }
    
    /* Specjalne style dla iOS */
    @supports (-webkit-touch-callout: none) {
        .stButton > button {
            -webkit-tap-highlight-color: transparent !important;
            -webkit-user-select: none !important;
            touch-action: manipulation !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Nagłówek z sercami
st.markdown("""
    <div style="text-align: center; font-size: 40px; margin-bottom: 20px;">
    💕 💕 💕
    </div>
    """, unsafe_allow_html=True)

# Główny tytuł i przyciski (tylko jeśli nie kliknięto TAK i nie kliknięto NIE 5 razy)
if not st.session_state.yes_clicked and st.session_state.no_clicks < 5:
    st.markdown("""
        <div class="title-container">
            <div class="title-text">
            Czy zostaniesz moją walentynką?
            </div>
        </div>
        """, unsafe_allow_html=True)

# Wyświetlanie przycisków tylko jeśli nie kliknięto TAK i nie kliknięto NIE 5 razy
if not st.session_state.yes_clicked and st.session_state.no_clicks < 5:
    # Przyciskowy layout z lepszym wsparciem mobilnym
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div class="button-container">
                <style>
                .no-button-current {
                    transform: scale(""" + str(max(0.3, 1.0 - st.session_state.no_clicks * 0.15)) + """) !important;
                }
                </style>
            </div>
        """, unsafe_allow_html=True)
        
        # Dodajemy JavaScript dla lepszej obsługi na iOS
        st.markdown("""
            <script>
            // Funkcja dla lepszej obsługi touch eventów na iOS
            document.addEventListener('DOMContentLoaded', function() {
                // Znajdź wszystkie przyciski
                const buttons = document.querySelectorAll('.stButton button');
                buttons.forEach(button => {
                    // Dodaj obsługę touch eventów dla iOS
                    button.addEventListener('touchstart', function(e) {
                        e.preventDefault();
                        this.style.transform = this.style.transform.replace('scale(', 'scale(') + ' scale(0.95)';
                    });
                    
                    button.addEventListener('touchend', function(e) {
                        e.preventDefault();
                        // Przywróć oryginalną skalę po krótkim opóźnieniu
                        setTimeout(() => {
                            this.style.transform = this.style.transform.replace(' scale(0.95)', '');
                        }, 100);
                        this.click();
                    });
                });
            });
            </script>
        """, unsafe_allow_html=True)
        
        # Używamy równych kolumn ale CSS do stylowania
        button_col1, button_col2 = st.columns(2)
        
        with button_col1:
            if st.button("TAK", key="yes_button", use_container_width=True):
                st.session_state.yes_clicked = True
                st.session_state.no_clicks = 0
                st.rerun()
        
        with button_col2:
            # Dodajemy CSS klasę dla aktualnego stanu
            st.markdown(f"""
                <style>
                div[data-testid="column"]:nth-child(2) .stButton button {{
                    transform: scale({max(0.3, 1.0 - st.session_state.no_clicks * 0.15)}) !important;
                    background: #dc3545 !important;
                    color: white !important;
                    transition: transform 0.3s ease !important;
                }}
                div[data-testid="column"]:nth-child(1) .stButton button {{
                    background: #28a745 !important;
                    color: white !important;
                }}
                </style>
            """, unsafe_allow_html=True)
            
            if st.button("NIE", key="no_button", use_container_width=True):
                st.session_state.no_clicks += 1
                st.session_state.yes_clicked = False
                st.rerun()

# Wyświetlanie głównej zawartości
if st.session_state.yes_clicked:
    # GIF tańczącego kota w centrum, pokrywający miejsce tytułu i przycisków
    # Centralne miejsce na GIF tańczącego kota
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Sprawdzenie czy plik GIF tańczącego kota istnieje
        happy_cat_gif = "happy_cat.gif"  # GIF tańczącego szczęśliwego kota
        if os.path.exists(happy_cat_gif):
            st.image(happy_cat_gif, use_container_width=True)
        else:
            # Wyświetl placeholder z instrukcją dla GIF-a
            st.markdown("""
                <div style='text-align: center; background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,183,217,0.2)); 
                           border-radius: 20px; padding: 40px; margin: 20px;
                           box-shadow: 0 8px 32px rgba(0,0,0,0.3); backdrop-filter: blur(10px);'>
                    <div style='font-size: 80px; margin-bottom: 20px; animation: dance 2s ease-in-out infinite;'>🐱</div>
                    <div style='color: white; font-size: 20px; font-weight: bold; margin-bottom: 15px;'>
                        🎊 Tutaj zatańczy szczęśliwy kot! 🎊
                    </div>
                    <div style='color: #ffb3d9; font-size: 16px; line-height: 1.4;'>
                        Umieść plik 'happy_cat.gif' w katalogu projektu<br>
                        aby zobaczyć tańczącego kota! 🕺
                    </div>
                </div>
                <style>
                @keyframes dance {
                    0%, 100% { transform: rotate(0deg) scale(1); }
                    25% { transform: rotate(5deg) scale(1.05); }
                    50% { transform: rotate(0deg) scale(1.1); }
                    75% { transform: rotate(-5deg) scale(1.05); }
                }
                </style>
            """, unsafe_allow_html=True)

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
