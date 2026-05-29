"""
🎮 EL ENIGMA DE LOS METADATOS
==============================
Juego educativo interactivo sobre metadatos
Desarrollado con Streamlit
Versión: 2.0 - Cyberpunk Edition
"""

import streamlit as st
from utils.estilos import obtener_css_principal
from utils.estado import inicializar_estado
from components.mapa import mostrar_mapa, mostrar_panel_puntuacion
from components.nivel1_clasificar import nivel1_clasificar
from components.nivel2_relacionar import nivel2_relacionar
from components.nivel3_ordenar import nivel3_ordenar
from components.nivel4_enigma import nivel4_enigma

# ============================================================================
# CONFIGURACIÓN INICIAL
# ============================================================================
st.set_page_config(
    page_title="El Enigma de los Metadatos | Juego Educativo",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# APLICACIÓN PRINCIPAL
# ============================================================================
def main():
    """Función principal del juego"""
    
    # Aplicar estilos CSS
    st.markdown(obtener_css_principal(), unsafe_allow_html=True)
    
    # Inicializar estado del juego
    inicializar_estado()
    
    # Panel lateral con puntuación
    mostrar_panel_puntuacion()
    
    # Título principal
    st.markdown('<h1 class="game-title">EL ENIGMA DE LOS METADATOS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="game-subtitle">▸ Sistema de Recuperación de Datos v2.0 ◂</p>', unsafe_allow_html=True)
    
    # Historia de introducción
    with st.expander("📖 HISTORIA DE LA MISIÓN", expanded=False):
        st.markdown("""
        <div class="terminal" style="font-size: 0.9rem;">
            > ALERTA DE SEGURIDAD - NIVEL 5<br>
            > ---------------------------------<br>
            > Un hacker desconocido ha infiltrádo el sistema central<br>
            > y ha eliminado información crítica de metadatos.<br>
            > <br>
            > Tu misión: Recuperar los metadatos perdidos<br>
            > resolviendo 4 desafíos de ingeniería de datos.<br>
            > <br>
            > Los metadatos son "datos sobre los datos":<br>
            > información que describe otros archivos, como<br>
            > fechas, autores, formatos y ubicaciones.<br>
            > <br>
            > Sin ellos, la base de datos es inutilizable.<br>
            > Debes restaurar el sistema antes de que sea tarde.<br>
            > ---------------------------------<br>
            > ¿ACEPTAS LA MISIÓN?
        </div>
        """, unsafe_allow_html=True)
    
    # Mostrar mapa de navegación
    mostrar_mapa()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contenedor principal del juego
    with st.container():
        st.markdown('<div class="cyber-container">', unsafe_allow_html=True)
        
        # Navegación entre niveles
        if st.session_state.nivel_actual == 1:
            nivel1_clasificar()
        elif st.session_state.nivel_actual == 2:
            nivel2_relacionar()
        elif st.session_state.nivel_actual == 3:
            nivel3_ordenar()
        elif st.session_state.nivel_actual == 4:
            nivel4_enigma()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; 
                border-top: 1px solid rgba(0, 255, 255, 0.1);">
        <p style="font-family: 'Rajdhani', sans-serif; color: #555; font-size: 0.8rem;">
            ▸ SISTEMA EDUCATIVO DE METADATOS v2.0 ◂<br>
            Desarrollado para aprendizaje interactivo
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================
if __name__ == "__main__":
    main()
