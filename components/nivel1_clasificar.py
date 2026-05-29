"""
NIVEL 1: CLASIFICACIÓN DE METADATOS
====================================
Puzzle visual donde el jugador arrastra tarjetas a categorías
"""

import streamlit as st
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel1_clasificar():
    """Juego de clasificación: Metadatos vs Contenido"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 01: CLASIFICACIÓN DE DATOS ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Identifica qué elementos son METADATOS y cuáles son CONTENIDO
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instrucciones visuales
    st.markdown("""
    <div class="info-panel">
        <strong>🎯 OBJETIVO:</strong> Los metadatos son "datos que describen otros datos".<br>
        <strong>💡 PISTA:</strong> Si describe ALGO SOBRE el archivo → METADATO. Si es LO QUE HAY DENTRO → CONTENIDO.
    </div>
    """, unsafe_allow_html=True)
    
    # Si ya completó este nivel
    if st.session_state.niveles_completados[1]:
        st.markdown("""
        <div class="success-message">
            ✅ NIVEL COMPLETADO - Sistema de clasificación restaurado
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Datos del juego
    elementos = [
        {"id": 1, "texto": "Fecha de creación del archivo", "tipo": "metadato", "icono": "📅"},
        {"id": 2, "texto": "Nombre del autor del documento", "tipo": "metadato", "icono": "✍️"},
        {"id": 3, "texto": "El texto completo de la carta", "tipo": "contenido", "icono": "📄"},
        {"id": 4, "texto": "Tamaño del archivo en kilobytes", "tipo": "metadato", "icono": "📏"},
        {"id": 5, "texto": "La fotografía dentro del documento", "tipo": "contenido", "icono": "🖼️"},
        {"id": 6, "texto": "Formato del archivo (PDF, DOCX)", "tipo": "metadato", "icono": "🔖"},
        {"id": 7, "texto": "Hora de última modificación", "tipo": "metadato", "icono": "🕐"},
        {"id": 8, "texto": "El poema escrito en el archivo", "tipo": "contenido", "icono": "📝"},
    ]
    
    # Mostrar las dos zonas de clasificación
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(0, 255, 136, 0.05); 
                    border: 2px dashed #00ff88; border-radius: 10px; min-height: 400px;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00ff88;">METADATOS</h3>
            <p style="color: #00ff88; font-size: 0.8rem;">Datos SOBRE el archivo</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(255, 0, 85, 0.05); 
                    border: 2px dashed #ff0055; border-radius: 10px; min-height: 400px;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #ff0055;">CONTENIDO</h3>
            <p style="color: #ff0055; font-size: 0.8rem;">Lo que hay DENTRO del archivo</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tarjetas para clasificar
    st.markdown("""
    <h4 style="font-family: 'Orbitron', sans-serif; color: #00ffff; text-align: center;">
        ▼ ARRASTRA CADA ELEMENTO A SU CATEGORÍA ▼
    </h4>
    """, unsafe_allow_html=True)
    
    # Selección mediante checkboxes organizados visualmente
    seleccionados_metadato = []
    
    st.markdown("### Selecciona los METADATOS:")
    cols = st.columns(2)
    
    for i, elemento in enumerate(elementos):
        with cols[i % 2]:
            seleccionado = st.checkbox(
                f"{elemento['icono']} {elemento['texto']}",
                key=f"n1_elem_{elemento['id']}",
                help="Marca si crees que es un METADATO"
            )
            if seleccionado:
                seleccionados_metadato.append(elemento['id'])
    
    # Botón de verificación
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔍 VERIFICAR CLASIFICACIÓN", key="verificar_n1", use_container_width=True):
            correctas = 0
            incorrectas = 0
            
            for elemento in elementos:
                es_metadato_real = elemento['tipo'] == 'metadato'
                fue_seleccionado = elemento['id'] in seleccionados_metadato
                
                if es_metadato_real and fue_seleccionado:
                    correctas += 1
                elif not es_metadato_real and not fue_seleccionado:
                    correctas += 1
                else:
                    incorrectas += 1
            
            if incorrectas == 0:
                # ¡Éxito!
                st.session_state.intentos_totales += 1
                completar_nivel(1, 100)
                mostrar_feedback('exito', '¡CLASIFICACIÓN PERFECTA! Has identificado correctamente todos los metadatos.')
                time.sleep(1.5)
                st.rerun()
            else:
                st.session_state.intentos_totales += 1
                mostrar_feedback('error', f'Tienes {incorrectas} error(es). Recuerda: los metadatos DESCRIBEN el archivo, no son el contenido.')
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
        
        # Limpiar feedback después de mostrar
        time.sleep(2)
        st.session_state.feedback['mostrar'] = False