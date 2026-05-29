"""
NIVEL 1: CLASIFICACIÓN DE METADATOS
====================================
Juego de cartas interactivas para clasificar metadatos vs contenido
"""

import streamlit as st
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel1_clasificar():
    """Juego de clasificación: Click en cartas para clasificar"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 01: CLASIFICACIÓN DE DATOS ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Haz click en cada carta para enviarla a su categoría correcta
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Instrucciones visuales
    st.markdown("""
    <div class="info-panel">
        <strong>🎯 OBJETIVO:</strong> Clasifica 8 elementos en METADATOS o CONTENIDO.<br>
        <strong>💡 PISTA:</strong> Metadato = Describe EL ARCHIVO. Contenido = Lo que hay DENTRO.<br>
        <strong>🖱️ CÓMO JUGAR:</strong> Haz click en "M" para Metadato o "C" para Contenido en cada carta.
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
    
    # Inicializar estado del nivel si no existe
    if 'cartas_clasificadas' not in st.session_state:
        st.session_state.cartas_clasificadas = {}
    if 'carta_actual' not in st.session_state:
        st.session_state.carta_actual = 0
    
    # Datos del juego
    elementos = [
        {"id": 1, "texto": "Fecha de creación del archivo", "tipo": "metadato", "icono": "📅", "pista": "¿Describe CUÁNDO se creó?"},
        {"id": 2, "texto": "Nombre del autor del documento", "tipo": "metadato", "icono": "👤", "pista": "¿Dice QUIÉN lo hizo?"},
        {"id": 3, "texto": "El texto completo de la carta", "tipo": "contenido", "icono": "📄", "pista": "¿Es LO QUE ESTÁ ESCRITO?"},
        {"id": 4, "texto": "Tamaño del archivo en KB", "tipo": "metadato", "icono": "📏", "pista": "¿Describe CUÁNTO pesa?"},
        {"id": 5, "texto": "La imagen dentro del documento", "tipo": "contenido", "icono": "🖼️", "pista": "¿Es LO QUE VES en el archivo?"},
        {"id": 6, "texto": "Formato del archivo (PDF, DOCX)", "tipo": "metadato", "icono": "🔖", "pista": "¿Dice QUÉ TIPO de archivo es?"},
        {"id": 7, "texto": "Hora de última modificación", "tipo": "metadato", "icono": "🕐", "pista": "¿Dice CUÁNDO se modificó?"},
        {"id": 8, "texto": "El poema escrito en el archivo", "tipo": "contenido", "icono": "📝", "pista": "¿Es EL TEXTO del archivo?"},
    ]
    
    # Contadores
    metadatos_correctos = sum(1 for e in elementos if e['tipo'] == 'metadato')
    contenidos_correctos = sum(1 for e in elementos if e['tipo'] == 'contenido')
    
    # Mostrar zonas de clasificación como cajas
    col1, col2 = st.columns(2)
    
    with col1:
        clasificados_meta = [e for e in elementos if st.session_state.cartas_clasificadas.get(e['id']) == 'metadato']
        st.markdown(f"""
        <div style="background: rgba(0, 255, 136, 0.08); border: 2px solid #00ff88; 
                    border-radius: 15px; padding: 20px; min-height: 200px;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00ff88; text-align: center; margin: 0;">
                📁 METADATOS
            </h3>
            <p style="color: #00ff88; text-align: center; font-size: 0.8rem; margin: 5px 0;">
                Datos SOBRE el archivo ({len(clasificados_meta)}/{metadatos_correctos})
            </p>
            <div style="margin-top: 15px;">
    """, unsafe_allow_html=True)
        
        for elemento in clasificados_meta:
            st.markdown(f"""
            <div style="background: rgba(0, 255, 136, 0.1); padding: 10px; margin: 5px 0; 
                        border-radius: 8px; font-family: 'Rajdhani', sans-serif; color: #00ff88;">
                {elemento['icono']} {elemento['texto']}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    with col2:
        clasificados_contenido = [e for e in elementos if st.session_state.cartas_clasificadas.get(e['id']) == 'contenido']
        st.markdown(f"""
        <div style="background: rgba(255, 0, 85, 0.08); border: 2px solid #ff0055; 
                    border-radius: 15px; padding: 20px; min-height: 200px;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #ff0055; text-align: center; margin: 0;">
                📄 CONTENIDO
            </h3>
            <p style="color: #ff0055; text-align: center; font-size: 0.8rem; margin: 5px 0;">
                Lo que hay DENTRO del archivo ({len(clasificados_contenido)}/{contenidos_correctos})
            </p>
            <div style="margin-top: 15px;">
    """, unsafe_allow_html=True)
        
        for elemento in clasificados_contenido:
            st.markdown(f"""
            <div style="background: rgba(255, 0, 85, 0.1); padding: 10px; margin: 5px 0; 
                        border-radius: 8px; font-family: 'Rajdhani', sans-serif; color: #ff0055;">
                {elemento['icono']} {elemento['texto']}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mostrar cartas pendientes
    cartas_pendientes = [e for e in elementos if e['id'] not in st.session_state.cartas_clasificadas]
    
    if cartas_pendientes:
        st.markdown(f"""
        <h4 style="font-family: 'Orbitron', sans-serif; color: #00ffff; text-align: center;">
            🃏 CARTAS PENDIENTES: {len(cartas_pendientes)}
        </h4>
        """, unsafe_allow_html=True)
        
        # Mostrar cartas en grid
        for i in range(0, len(cartas_pendientes), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(cartas_pendientes):
                    elemento = cartas_pendientes[i + j]
                    with cols[j]:
                        st.markdown(f"""
                        <div class="game-card" style="margin: 10px 0;">
                            <div style="font-size: 2.5rem;">{elemento['icono']}</div>
                            <strong style="font-size: 1.1rem;">{elemento['texto']}</strong>
                            <p style="color: #8892b0; font-size: 0.8rem; margin: 5px 0;">💡 {elemento['pista']}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            if st.button(f"📁 METADATO", key=f"meta_{elemento['id']}", use_container_width=True):
                                st.session_state.cartas_clasificadas[elemento['id']] = 'metadato'
                                st.rerun()
                        with col_b:
                            if st.button(f"📄 CONTENIDO", key=f"cont_{elemento['id']}", use_container_width=True):
                                st.session_state.cartas_clasificadas[elemento['id']] = 'contenido'
                                st.rerun()
    
    # Verificar cuando todas las cartas están clasificadas
    if len(st.session_state.cartas_clasificadas) == len(elementos):
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Calcular resultados
        correctas = 0
        for elemento in elementos:
            if st.session_state.cartas_clasificadas[elemento['id']] == elemento['tipo']:
                correctas += 1
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 VERIFICAR CLASIFICACIÓN", key="verificar_n1", use_container_width=True):
                if correctas == len(elementos):
                    # ¡Éxito!
                    st.session_state.intentos_totales += 1
                    completar_nivel(1, 100)
                    # Limpiar estado del nivel
                    del st.session_state.cartas_clasificadas
                    mostrar_feedback('exito', f'¡CLASIFICACIÓN PERFECTA! {correctas}/{len(elementos)} correctas. Los metadatos describen propiedades del archivo.')
                    time.sleep(2)
                    st.rerun()
                else:
                    st.session_state.intentos_totales += 1
                    errores = len(elementos) - correctas
                    mostrar_feedback('error', f'Tienes {errores} error(es). Revisa las cartas mal clasificadas e intenta de nuevo.')
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
            # Botón para reiniciar nivel si hay error
            if st.button("🔄 Reintentar nivel", use_container_width=True):
                st.session_state.cartas_clasificadas = {}
                st.session_state.feedback['mostrar'] = False
                st.rerun()
        
        # Limpiar feedback después de mostrar
        if st.session_state.feedback['tipo'] == 'exito':
            time.sleep(2)
            st.session_state.feedback['mostrar'] = False
