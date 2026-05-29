"""
MAPA DE NAVEGACIÓN INTERACTIVO
==============================
Tablero visual que muestra el progreso del jugador
"""

import streamlit as st

def mostrar_mapa():
    """Renderiza el mapa de navegación del juego"""
    
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 1.5rem; letter-spacing: 5px;">
            ▸ SISTEMA DE NAVEGACIÓN ◂
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Crear columnas para el mapa
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 0.5, 1, 0.5, 1, 0.5, 1])
    
    niveles = [
        {"num": 1, "icono": "01", "nombre": "CLASIFICAR"},
        {"num": 2, "icono": "02", "nombre": "RELACIONAR"},
        {"num": 3, "icono": "03", "nombre": "ORDENAR"},
        {"num": 4, "icono": "04", "nombre": "RECUPERAR"}
    ]
    
    # Posiciones: col1, col3, col5, col7 para los nodos
    # Posiciones: col2, col4, col6 para las líneas conectoras
    posiciones_nodos = [col1, col3, col5, col7]
    posiciones_lineas = [col2, col4, col6]
    
    for i, (nivel, pos_nodo) in enumerate(zip(niveles, posiciones_nodos)):
        with pos_nodo:
            # Determinar estado del nodo
            if st.session_state.niveles_completados[nivel["num"]]:
                clase = "node-completed"
                estado = "COMPLETADO"
                color = "#00ff88"
            elif nivel["num"] == st.session_state.nivel_actual:
                clase = "node-active"
                estado = "ACTIVO"
                color = "#00ffff"
            else:
                clase = "node-locked"
                estado = "BLOQUEADO"
                color = "#555"
            
            st.markdown(f"""
            <div class="map-node">
                <div class="node-circle {clase}">{nivel["icono"]}</div>
                <div class="node-label" style="color: {color};">{nivel["nombre"]}</div>
                <div style="font-size: 0.7rem; color: {color}; margin-top: 3px;">{estado}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Dibujar línea conectora (excepto después del último nodo)
        if i < len(posiciones_lineas):
            with posiciones_lineas[i]:
                # Determinar estado de la línea
                if st.session_state.niveles_completados[nivel["num"]]:
                    clase_linea = "line-completed"
                elif nivel["num"] == st.session_state.nivel_actual:
                    clase_linea = "line-active"
                else:
                    clase_linea = ""
                
                st.markdown(f"""
                <div class="connection-line {clase_linea}" style="margin-top: 35px;"></div>
                """, unsafe_allow_html=True)
    
    # Leyenda del mapa
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 30px; margin-top: 20px; font-family: 'Rajdhani', sans-serif; font-size: 0.8rem;">
        <span style="color: #555;">⬤ BLOQUEADO</span>
        <span style="color: #00ffff;">⬤ ACTIVO</span>
        <span style="color: #00ff88;">⬤ COMPLETADO</span>
    </div>
    """, unsafe_allow_html=True)

def mostrar_panel_puntuacion():
    """Muestra el panel lateral con puntuación y trofeos"""
    
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 1.2rem;">
                ▸ PANEL DE CONTROL ◂
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Progreso general
        progreso = sum(st.session_state.niveles_completados.values())
        st.markdown(f"""
        <div class="info-panel">
            <strong>PROGRESO:</strong> {progreso}/4<br>
            <strong>PUNTUACIÓN:</strong> {st.session_state.puntuacion} pts
        </div>
        """, unsafe_allow_html=True)
        
        # Barra de progreso
        st.progress(progreso / 4)
        
        # Trofeos obtenidos
        if st.session_state.trofeos:
            st.markdown("""
            <div style="margin-top: 30px;">
                <h4 style="font-family: 'Orbitron', sans-serif; color: #00ff88; font-size: 0.9rem;">
                    🏆 TROFEOS OBTENIDOS
                </h4>
            </div>
            """, unsafe_allow_html=True)
            
            for trofeo in st.session_state.trofeos:
                st.markdown(f"""
                <div class="game-card" style="padding: 10px; margin: 5px 0; text-align: left;">
                    {trofeo}
                </div>
                """, unsafe_allow_html=True)
        
        # Botón de reinicio
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 REINICIAR SISTEMA", use_container_width=True):
            from utils.estado import reiniciar_juego
            reiniciar_juego()
            st.rerun()