"""
NIVEL 4: ENIGMA FINAL - RECUPERACIÓN
=====================================
Acertijo final para restaurar la base de datos
"""

import streamlit as st
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel4_enigma():
    """Enigma final: Recuperación de la base de datos"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 04: RECUPERACIÓN FINAL ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Resuelve el enigma para restaurar la base de datos perdida
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Si ya completó este nivel (mostrar premio)
    if st.session_state.niveles_completados[4] and st.session_state.mostrar_premio:
        mostrar_premio_final()
        return
    elif st.session_state.niveles_completados[4]:
        st.markdown("""
        <div class="success-message">
            ✅ BASE DE DATOS RESTAURADA - Misión completada con éxito
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown("""
    <div class="info-panel">
        <strong>🎯 MISIÓN FINAL:</strong> Demuestra tu comprensión sobre metadatos.<br>
        <strong>⚠️ ADVERTENCIA:</strong> Solo hay una oportunidad para responder correctamente.
    </div>
    """, unsafe_allow_html=True)
    
    # Terminal hacker
    st.markdown("""
    <div class="terminal">
        > Iniciando protocolo de recuperación...<br>
        > Accediendo a sector cifrado...<br>
        > Se requiere autenticación de conocimiento...<br>
        > <span style="color: #ff0055;">PREGUNTA DE SEGURIDAD ACTIVADA</span><br>
        > _________________________________
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pregunta del enigma
    st.markdown("""
    <div class="cyber-container">
        <h3 style="font-family: 'Orbitron', sans-serif; color: #ff0055; text-align: center;">
            ⚠️ PREGUNTA DE VERIFICACIÓN ⚠️
        </h3>
        <p style="font-family: 'Rajdhani', sans-serif; color: #ccd6f6; font-size: 1.3rem; text-align: center;">
            ¿Cuál es la función PRINCIPAL de los metadatos en un sistema de información?
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    respuesta = st.radio(
        "Selecciona la respuesta correcta:",
        [
            "A) Aumentar el tamaño de los archivos para hacerlos más seguros",
            "B) Describir, organizar y facilitar la búsqueda y recuperación de información",
            "C) Encriptar el contenido para que nadie pueda leerlo",
            "D) Eliminar automáticamente archivos antiguos del sistema"
        ],
        key="pregunta_final",
        index=None
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("🔑 DESBLOQUEAR BASE DE DATOS", key="verificar_n4", use_container_width=True):
            if respuesta and "B)" in respuesta:
                st.session_state.intentos_totales += 1
                completar_nivel(4, 500)
                st.session_state.mostrar_premio = True
                st.balloons()
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.intentos_totales += 1
                mostrar_feedback('error', 'Respuesta incorrecta. Los metadatos sirven para DESCRIBIR y ORGANIZAR la información.')
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

def mostrar_premio_final():
    """Muestra la pantalla de victoria con premio"""
    
    st.balloons()
    
    st.markdown(f"""
    <div class="trophy-container">
        <div style="font-size: 5rem; animation: float 2s ease-in-out infinite;">
            🏆
        </div>
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ff88; font-size: 2.5rem; margin: 20px 0;">
            ¡BASE DE DATOS RESTAURADA!
        </h2>
        <div class="terminal" style="text-align: left; max-width: 600px; margin: 30px auto;">
            > ESTADO: RECUPERACIÓN COMPLETA<br>
            > SECTORES RESTAURADOS: 4/4<br>
            > PUNTUACIÓN TOTAL: {st.session_state.puntuacion} puntos<br>
            > INTENTOS TOTALES: {st.session_state.intentos_totales}<br>
            > EFICIENCIA: {100 - (st.session_state.intentos_totales - 4) * 5}%<br>
            > _________________________________<br>
            > <span style="color: #00ff88;">SISTEMA OPERATIVO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mostrar trofeos obtenidos
    st.markdown("""
    <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff; text-align: center;">
        LOGROS DESBLOQUEADOS
    </h3>
    """, unsafe_allow_html=True)
    
    cols = st.columns(len(st.session_state.trofeos))
    for i, (col, trofeo) in enumerate(zip(cols, st.session_state.trofeos)):
        with col:
            st.markdown(f"""
            <div class="game-card" style="text-align: center; padding: 20px;">
                <div style="font-size: 2rem;">{'🔍' if i == 0 else '🔗' if i == 1 else '⏱️' if i == 2 else '🏆'}</div>
                <strong style="color: #00ff88;">{trofeo}</strong>
            </div>
            """, unsafe_allow_html=True)
    
    # Certificado de finalización
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="cyber-container" style="text-align: center;">
        <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff;">
            📜 CERTIFICADO DE RECUPERACIÓN
        </h3>
        <p style="font-family: 'Rajdhani', sans-serif; color: #ccd6f6;">
            Por la presente se certifica que el agente ha demostrado<br>
            conocimientos excepcionales en metadatos y ha logrado<br>
            restaurar completamente la base de datos del sistema.
        </p>
        <p style="font-family: 'Courier New', monospace; color: #00ff88; font-size: 0.8rem;">
            FIRMA DIGITAL: 0x7F3A9B2C1D4E5F6A8B9C0D1E2F3A4B5C
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón para reiniciar
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 NUEVA MISIÓN", use_container_width=True, key="nueva_mision"):
            from utils.estado import reiniciar_juego
            reiniciar_juego()
            st.rerun()