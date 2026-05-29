"""
NIVEL 3: LA MÁQUINA DEL TIEMPO
===============================
Juego visual de ordenar eventos en una línea de tiempo interactiva
"""

import streamlit as st
import random
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel3_ordenar():
    """Juego de timeline: Ordenar eventos cronológicamente"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 03: LA MÁQUINA DEL TIEMPO ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Ordena los eventos en la línea de tiempo correcta
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-panel">
        <strong>⏰ MISIÓN:</strong> La línea temporal de los metadatos se ha desordenado.<br>
        <strong>🖱️ CÓMO JUGAR:</strong> Haz click en los botones ↑↓ para mover cada evento a su posición correcta en el tiempo.
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.niveles_completados[3]:
        st.markdown("""
        <div class="success-message">
            ✅ LÍNEA TEMPORAL RESTAURADA - El flujo de metadatos funciona correctamente
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Eventos de la línea de tiempo
    eventos_correctos = [
        {"id": 1, "texto": "Creación del archivo digital", "icono": "📄", "color": "#ff6b6b", 
         "descripcion": "Alguien crea un nuevo archivo en la computadora"},
        {"id": 2, "texto": "Generación de metadatos", "icono": "⚙️", "color": "#4ecdc4",
         "descripcion": "El sistema crea automáticamente datos sobre el archivo"},
        {"id": 3, "texto": "Almacenamiento organizado", "icono": "💾", "color": "#ffd93d",
         "descripcion": "El archivo y sus metadatos se guardan en la base de datos"},
        {"id": 4, "texto": "Indexación para búsqueda", "icono": "🔍", "color": "#a855f7",
         "descripcion": "Los metadatos se organizan en índices para encontrar rápido"},
        {"id": 5, "texto": "Recuperación y consulta", "icono": "📂", "color": "#00ff88",
         "descripcion": "Usamos los metadatos para buscar y encontrar el archivo"}
    ]
    
    # Inicializar orden aleatorio
    if 'orden_actual' not in st.session_state:
        st.session_state.orden_actual = random.sample(eventos_correctos, len(eventos_correctos))
    
    if 'posiciones_verificadas' not in st.session_state:
        st.session_state.posiciones_verificadas = []
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff;">
            🕐 LÍNEA DE TIEMPO
        </h3>
        <p style="color: #8892b0; font-size: 0.9rem;">Primero ocurre ↑ | Último ocurre ↓</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar eventos en orden actual con botones de movimiento
    for i, evento in enumerate(st.session_state.orden_actual):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        
        with col2:
            # Determinar si está en posición correcta
            if i in st.session_state.posiciones_verificadas and evento['id'] == i + 1:
                borde_color = "#00ff88"
                fondo = "rgba(0, 255, 136, 0.15)"
            else:
                borde_color = evento['color']
                fondo = "rgba(0, 0, 0, 0.3)"
            
            st.markdown(f"""
            <div style="background: {fondo}; border: 2px solid {borde_color}; 
                        border-radius: 15px; padding: 20px; margin: 10px 0;
                        position: relative;">
                <span style="font-size: 2.5rem; position: absolute; left: 15px; top: 10px;">{evento['icono']}</span>
                <div style="margin-left: 70px;">
                    <h4 style="color: {borde_color}; font-family: 'Rajdhani', sans-serif; margin: 0; font-size: 1.2rem;">
                        Posición {i + 1}: {evento['texto']}
                    </h4>
                    <p style="color: #8892b0; margin: 5px 0 0 0; font-size: 0.85rem;">{evento['descripcion']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col1:
            if i > 0:
                if st.button("⬆️", key=f"subir_{i}", help="Mover hacia arriba (más temprano)"):
                    # Intercambiar con el anterior
                    st.session_state.orden_actual[i], st.session_state.orden_actual[i-1] = \
                        st.session_state.orden_actual[i-1], st.session_state.orden_actual[i]
                    st.rerun()
        
        with col3:
            if i < len(st.session_state.orden_actual) - 1:
                if st.button("⬇️", key=f"bajar_{i}", help="Mover hacia abajo (más tarde)"):
                    # Intercambiar con el siguiente
                    st.session_state.orden_actual[i], st.session_state.orden_actual[i+1] = \
                        st.session_state.orden_actual[i+1], st.session_state.orden_actual[i]
                    st.rerun()
    
    # Verificar orden
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("⏰ VERIFICAR LÍNEA TEMPORAL", key="verificar_n3", use_container_width=True):
            es_correcto = True
            for i, evento in enumerate(st.session_state.orden_actual):
                if evento['id'] != i + 1:
                    es_correcto = False
                    break
            
            if es_correcto:
                st.session_state.intentos_totales += 1
                completar_nivel(3, 300)
                # Limpiar estado
                for key in ['orden_actual', 'posiciones_verificadas']:
                    if key in st.session_state:
                        del st.session_state[key]
                mostrar_feedback('exito', '¡LÍNEA TEMPORAL CORRECTA! Los metadatos siguen este orden: crear → extraer → guardar → indexar → buscar.')
                time.sleep(2)
                st.rerun()
            else:
                st.session_state.intentos_totales += 1
                # Marcar cuáles están en posición correcta
                st.session_state.posiciones_verificadas = []
                for i, evento in enumerate(st.session_state.orden_actual):
                    if evento['id'] == i + 1:
                        st.session_state.posiciones_verificadas.append(i)
                
                if len(st.session_state.posiciones_verificadas) > 0:
                    mostrar_feedback('error', f'Tienes {len(st.session_state.posiciones_verificadas)} de 5 en posición correcta. ¡Revisa las que no tienen borde verde!')
                else:
                    mostrar_feedback('error', 'Ningún evento está en su posición correcta. Piensa: ¿qué ocurre PRIMERO cuando creas un archivo?')
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
