"""
GESTIÓN DE ESTADO DEL JUEGO
============================
Maneja el progreso, puntuación y logros
"""

import streamlit as st

def inicializar_estado():
    """Inicializa todas las variables de estado del juego"""
    
    if 'nivel_actual' not in st.session_state:
        st.session_state.nivel_actual = 1
    
    if 'niveles_completados' not in st.session_state:
        st.session_state.niveles_completados = {
            1: False,  # Clasificación
            2: False,  # Relación
            3: False,  # Orden
            4: False   # Enigma final
        }
    
    if 'puntuacion' not in st.session_state:
        st.session_state.puntuacion = 0
    
    if 'intentos_totales' not in st.session_state:
        st.session_state.intentos_totales = 0
    
    if 'trofeos' not in st.session_state:
        st.session_state.trofeos = []
    
    if 'mostrar_premio' not in st.session_state:
        st.session_state.mostrar_premio = False
    
    if 'feedback' not in st.session_state:
        st.session_state.feedback = {
            'mostrar': False,
            'tipo': '',  # 'exito' o 'error'
            'mensaje': ''
        }

def desbloquear_nivel(numero_nivel):
    """Desbloquea el siguiente nivel"""
    if numero_nivel < 4:
        st.session_state.nivel_actual = numero_nivel + 1

def completar_nivel(numero_nivel, puntos_ganados):
    """Marca un nivel como completado y otorga puntos"""
    st.session_state.niveles_completados[numero_nivel] = True
    st.session_state.puntuacion += puntos_ganados
    
    # Otorgar trofeos especiales
    if numero_nivel == 1:
        st.session_state.trofeos.append("🔍 Detective de Datos")
    elif numero_nivel == 2:
        st.session_state.trofeos.append("🔗 Maestro de Conexiones")
    elif numero_nivel == 3:
        st.session_state.trofeos.append("⏱️ Señor del Tiempo")
    elif numero_nivel == 4:
        st.session_state.trofeos.append("🏆 Guardián de la Base de Datos")
        st.session_state.mostrar_premio = True
    
    desbloquear_nivel(numero_nivel)

def mostrar_feedback(tipo, mensaje):
    """Muestra mensaje de feedback al usuario"""
    st.session_state.feedback = {
        'mostrar': True,
        'tipo': tipo,
        'mensaje': mensaje
    }

def limpiar_feedback():
    """Limpia el mensaje de feedback"""
    st.session_state.feedback['mostrar'] = False

def reiniciar_juego():
    """Reinicia completamente el juego"""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    inicializar_estado()