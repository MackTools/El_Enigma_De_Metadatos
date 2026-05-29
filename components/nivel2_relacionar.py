"""
NIVEL 2: RELACIÓN ARCHIVO-METADATO
===================================
Juego de conexiones visuales entre tipos de archivo y sus metadatos
"""

import streamlit as st
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel2_relacionar():
    """Juego de relación: Conectar archivos con sus metadatos"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 02: CONEXIONES DE DATOS ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Conecta cada tipo de archivo con su metadato característico
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-panel">
        <strong>🎯 OBJETIVO:</strong> Cada tipo de archivo tiene metadatos específicos.<br>
        <strong>💡 PISTA:</strong> Piensa en qué información es única para cada formato.
    </div>
    """, unsafe_allow_html=True)
    
    # Si ya completó este nivel
    if st.session_state.niveles_completados[2]:
        st.markdown("""
        <div class="success-message">
            ✅ NIVEL COMPLETADO - Conexiones de metadatos establecidas
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Datos del juego
    archivos = [
        {"nombre": "Fotografía Digital", "icono": "📷", "metadato_correcto": "Datos EXIF (cámara, fecha, ubicación)"},
        {"nombre": "Documento de Texto", "icono": "📝", "metadato_correcto": "Autor, fecha de edición, número de páginas"},
        {"nombre": "Archivo de Audio MP3", "icono": "🎵", "metadato_correcto": "Artista, álbum, año, género musical"},
        {"nombre": "Página Web HTML", "icono": "🌐", "metadato_correcto": "Meta tags (título, descripción, keywords)"},
    ]
    
    opciones_metadatos = [
        "Datos EXIF (cámara, fecha, ubicación)",
        "Autor, fecha de edición, número de páginas",
        "Artista, álbum, año, género musical",
        "Meta tags (título, descripción, keywords)",
    ]
    
    # Mostrar columnas: Archivos | Conexiones | Metadatos
    st.markdown("""
    <div style="display: flex; justify-content: space-between; margin: 40px 0;">
        <div style="flex: 1; text-align: center;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff;">ARCHIVOS</h3>
        </div>
        <div style="flex: 0.5; text-align: center;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00ff88;">⚡</h3>
        </div>
        <div style="flex: 1; text-align: center;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #ff0055;">METADATOS</h3>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    selecciones = {}
    
    for i, archivo in enumerate(archivos):
        col1, col2, col3 = st.columns([1, 0.3, 1])
        
        with col1:
            st.markdown(f"""
            <div class="game-card" style="cursor: default;">
                <span style="font-size: 2rem;">{archivo['icono']}</span><br>
                <strong>{archivo['nombre']}</strong>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="text-align: center; font-size: 2rem; color: #00ffff; line-height: 80px;">
                ⟶
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            selecciones[archivo['nombre']] = st.selectbox(
                f"Metadato para {archivo['nombre']}",
                ["Selecciona el metadato correcto..."] + opciones_metadatos,
                key=f"n2_archivo_{i}",
                label_visibility="collapsed"
            )
    
    # Verificación
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔗 VERIFICAR CONEXIONES", key="verificar_n2", use_container_width=True):
            aciertos = 0
            
            for archivo in archivos:
                if selecciones[archivo['nombre']] == archivo['metadato_correcto']:
                    aciertos += 1
            
            if aciertos == 4:
                st.session_state.intentos_totales += 1
                completar_nivel(2, 200)
                mostrar_feedback('exito', '¡CONEXIONES PERFECTAS! Cada archivo tiene sus metadatos únicos.')
                time.sleep(1.5)
                st.rerun()
            else:
                st.session_state.intentos_totales += 1
                mostrar_feedback('error', f'Tienes {4 - aciertos} conexión(es) incorrecta(s). Cada formato tiene metadatos específicos.')
                st.rerun()
    
    # Mostrar feedback
    if st.session_state.feedback['mostrar']:
        if st.session_state.feedback['tipo'] == 'exito':
            st.markdown(f"""
            <div class="success-message">
                {st.session_state.feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="error-message">
                {st.session_state.feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
        
        time.sleep(2)
        st.session_state.feedback['mostrar'] = False