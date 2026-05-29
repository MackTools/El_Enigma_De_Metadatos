"""
NIVEL 4: LA SALA DE ESCAPE DIGITAL
===================================
Juego de escape room virtual con múltiples acertijos sobre metadatos
"""

import streamlit as st
import random
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel4_enigma():
    """Escape room: Resolver acertijos para recuperar la base de datos"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 04: LA SALA DE ESCAPE DIGITAL ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Resuelve los 3 acertijos para desbloquear la base de datos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
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
        <strong>🔐 MISIÓN FINAL:</strong> Estás en una sala de escape digital.<br>
        <strong>🖱️ CÓMO JUGAR:</strong> Resuelve cada acertijo para obtener un código. 
        Los 3 códigos desbloquearán la base de datos.
    </div>
    """, unsafe_allow_html=True)
    
    # Inicializar estado de los acertijos
    if 'acertijos_resueltos' not in st.session_state:
        st.session_state.acertijos_resueltos = {
            'palabra_clave': False,
            'codigo_color': False,
            'rompecabezas_final': False
        }
    if 'codigos_obtenidos' not in st.session_state:
        st.session_state.codigos_obtenidos = []
    
    # Mostrar progreso de la sala de escape
    resueltos = sum(st.session_state.acertijos_resueltos.values())
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <span style="font-family: 'Orbitron', sans-serif; color: #00ff88; font-size: 1.2rem;">
            🔐 CÓDIGOS OBTENIDOS: {resueltos} / 3
        </span>
    </div>
    <div style="display: flex; gap: 10px; margin: 20px 0;">
        <div style="flex: 1; height: 5px; background: {'#00ff88' if st.session_state.acertijos_resueltos['palabra_clave'] else '#333'}; border-radius: 3px;"></div>
        <div style="flex: 1; height: 5px; background: {'#00ff88' if st.session_state.acertijos_resueltos['codigo_color'] else '#333'}; border-radius: 3px;"></div>
        <div style="flex: 1; height: 5px; background: {'#00ff88' if st.session_state.acertijos_resueltos['rompecabezas_final'] else '#333'}; border-radius: 3px;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # ====================
    # ACERTIJO 1: PALABRA CLAVE
    # ====================
    if not st.session_state.acertijos_resueltos['palabra_clave']:
        with st.expander("🔑 ACERTIJO 1: LA PALABRA CLAVE", expanded=True):
            st.markdown("""
            <div style="background: rgba(255, 107, 107, 0.1); padding: 20px; border-radius: 10px; margin: 10px 0;">
                <h4 style="color: #ff6b6b; font-family: 'Rajdhani', sans-serif;">
                    🧩 ¿Qué palabra define a los metadatos?
                </h4>
                <p style="color: #ccd6f6;">Son datos que ________________ otros datos.</p>
                <p style="color: #8892b0; font-size: 0.9rem;">
                    Pista: Es un verbo de 8 letras. Empieza con "D".
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            respuesta = st.text_input("Escribe la palabra:", key="acertijo1", placeholder="________").lower().strip()
            
            if st.button("🔓 VERIFICAR PALABRA", key="verificar_acertijo1", use_container_width=True):
                if respuesta == "describen" or respuesta == "describir":
                    st.session_state.acertijos_resueltos['palabra_clave'] = True
                    st.session_state.codigos_obtenidos.append("🔑")
                    st.success("✅ ¡Correcto! Los metadatos DESCRIBEN otros datos.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ No es correcto. Piensa: ¿qué hacen los metadatos con los datos?")
    else:
        st.markdown("""
        <div style="background: rgba(0, 255, 136, 0.1); border: 2px solid #00ff88; 
                    border-radius: 10px; padding: 15px; margin: 10px 0;">
            <strong style="color: #00ff88;">✅ ACERTIJO 1 RESUELTO</strong> - Código obtenido: 🔑
        </div>
        """, unsafe_allow_html=True)
    
    # ====================
    # ACERTIJO 2: CÓDIGO DE COLORES
    # ====================
    if not st.session_state.acertijos_resueltos['codigo_color']:
        with st.expander("🎨 ACERTIJO 2: EL CÓDIGO DE COLORES", expanded=False):
            st.markdown("""
            <div style="background: rgba(78, 205, 196, 0.1); padding: 20px; border-radius: 10px; margin: 10px 0;">
                <h4 style="color: #4ecdc4; font-family: 'Rajdhani', sans-serif;">
                    🎯 ¿Qué metadato NO pertenece a un archivo de audio?
                </h4>
            </div>
            """, unsafe_allow_html=True)
            
            opciones = [
                "Nombre del artista",
                "Duración de la canción",
                "Resolución de la pantalla",
                "Género musical"
            ]
            
            # Aleatorizar opciones
            if 'opciones_acertijo2' not in st.session_state:
                st.session_state.opciones_acertijo2 = random.sample(opciones, len(opciones))
            
            for opcion in st.session_state.opciones_acertijo2:
                if st.button(f"🎵 {opcion}", key=f"opcion_{opcion}", use_container_width=True):
                    if opcion == "Resolución de la pantalla":
                        st.session_state.acertijos_resueltos['codigo_color'] = True
                        st.session_state.codigos_obtenidos.append("🎨")
                        st.success("✅ ¡Correcto! La resolución de pantalla es metadato de imágenes/video, no de audio.")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❌ Este SÍ es un metadato de audio. Busca el que NO corresponde.")
    else:
        st.markdown("""
        <div style="background: rgba(0, 255, 136, 0.1); border: 2px solid #00ff88; 
                    border-radius: 10px; padding: 15px; margin: 10px 0;">
            <strong style="color: #00ff88;">✅ ACERTIJO 2 RESUELTO</strong> - Código obtenido: 🎨
        </div>
        """, unsafe_allow_html=True)
    
    # ====================
    # ACERTIJO 3: ROMPECABEZAS FINAL
    # ====================
        # ====================
    # ACERTIJO 3: ROMPECABEZAS FINAL
    # ====================
    if not st.session_state.acertijos_resueltos['rompecabezas_final']:
        with st.expander("🧩 ACERTIJO 3: EL ROMPECABEZAS FINAL", expanded=False):
            
            # Palabra a adivinar y sus letras desordenadas aleatoriamente
            palabra_correcta = "ORGANIZAR"
            
            # Inicializar letras desordenadas si no existen
            if 'letras_desordenadas' not in st.session_state:
                letras = list(palabra_correcta)
                random.shuffle(letras)
                # Asegurarse de que no quede igual que la original
                while ''.join(letras) == palabra_correcta:
                    random.shuffle(letras)
                st.session_state.letras_desordenadas = letras
            
            # Mostrar las letras desordenadas como tarjetas visuales
            st.markdown(f"""
            <div style="background: rgba(168, 85, 247, 0.1); padding: 20px; border-radius: 10px; margin: 10px 0;">
                <h4 style="color: #a855f7; font-family: 'Rajdhani', sans-serif;">
                    🎯 Ordena las letras para descubrir la función principal de los metadatos
                </h4>
                <div style="display: flex; justify-content: center; gap: 10px; margin: 20px 0; flex-wrap: wrap;">
            """, unsafe_allow_html=True)
            
            # Mostrar cada letra en una tarjeta
            for letra in st.session_state.letras_desordenadas:
                st.markdown(f"""
                    <div style="background: rgba(168, 85, 247, 0.2); 
                                border: 2px solid #a855f7; 
                                border-radius: 10px; 
                                padding: 15px 20px; 
                                font-family: 'Orbitron', sans-serif;
                                font-size: 1.8rem;
                                color: #a855f7;
                                font-weight: 700;
                                display: inline-block;
                                min-width: 50px;
                                text-align: center;">
                        {letra}
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
                </div>
                <p style="color: #8892b0; font-size: 0.9rem; text-align: center;">
                    💡 Pista: Es lo que hacemos con los libros en una biblioteca para encontrarlos fácilmente.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            respuesta = st.text_input(
                "Escribe la palabra ordenada:", 
                key="acertijo3", 
                placeholder="Escribe aquí la palabra...",
                help="Mira las letras desordenadas y escribe la palabra correcta"
            ).upper().strip()
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("🧩 VERIFICAR ROMPECABEZAS", key="verificar_acertijo3", use_container_width=True):
                    if respuesta == palabra_correcta:
                        st.session_state.acertijos_resueltos['rompecabezas_final'] = True
                        st.session_state.codigos_obtenidos.append("🧩")
                        # Limpiar letras para cuando se reinicie
                        if 'letras_desordenadas' in st.session_state:
                            del st.session_state.letras_desordenadas
                        st.success("✅ ¡Correcto! Los metadatos nos ayudan a ORGANIZAR la información.")
                        time.sleep(1)
                        st.rerun()
                    elif respuesta == "":
                        st.error("❌ Debes escribir una palabra.")
                    else:
                        st.error(f"❌ '{respuesta}' no es correcto. Las letras mostradas forman una palabra relacionada con ordenar cosas.")
                        st.info("💡 Pista adicional: Cuando organizas algo, lo pones en su lugar para encontrarlo después.")
    else:
        st.markdown("""
        <div style="background: rgba(0, 255, 136, 0.1); border: 2px solid #00ff88; 
                    border-radius: 10px; padding: 15px; margin: 10px 0;">
            <strong style="color: #00ff88;">✅ ACERTIJO 3 RESUELTO</strong> - Código obtenido: 🧩
        </div>
        """, unsafe_allow_html=True)
    
    # Verificar si todos los acertijos están resueltos
    if all(st.session_state.acertijos_resueltos.values()):
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Animación de códigos
        st.markdown(f"""
        <div style="text-align: center; padding: 30px; background: rgba(0, 255, 136, 0.1); 
                    border-radius: 15px; border: 2px solid #00ff88;">
            <h3 style="color: #00ff88; font-family: 'Orbitron', sans-serif;">
                CÓDIGOS COMPLETOS: {' '.join(st.session_state.codigos_obtenidos)}
            </h3>
            <p style="color: #ccd6f6;">¡Todos los acertijos resueltos!</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔓 DESBLOQUEAR BASE DE DATOS", key="desbloquear_final", use_container_width=True):
                st.session_state.intentos_totales += 1
                completar_nivel(4, 500)
                st.session_state.mostrar_premio = True
                # Limpiar estado
                for key in ['acertijos_resueltos', 'codigos_obtenidos', 'opciones_acertijo2']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.balloons()
                time.sleep(1)
                st.rerun()

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
            > NIVELES COMPLETADOS: 4/4<br>
            > PUNTUACIÓN TOTAL: {st.session_state.puntuacion} puntos<br>
            > EFICIENCIA: {max(0, 100 - (st.session_state.intentos_totales - 4) * 10)}%<br>
            > _________________________________<br>
            > <span style="color: #00ff88;">SISTEMA OPERATIVO - 100% FUNCIONAL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Trofeos
    st.markdown("""
    <h3 style="font-family: 'Orbitron', sans-serif; color: #00ffff; text-align: center;">
        🏅 LOGROS DESBLOQUEADOS
    </h3>
    """, unsafe_allow_html=True)
    
    if st.session_state.trofeos:
        cols = st.columns(len(st.session_state.trofeos))
        iconos = ["🔍", "🔗", "⏱️", "🏆"]
        for i, (col, trofeo) in enumerate(zip(cols, st.session_state.trofeos)):
            with col:
                st.markdown(f"""
                <div class="game-card" style="text-align: center; padding: 20px;">
                    <div style="font-size: 2.5rem;">{iconos[i] if i < len(iconos) else '⭐'}</div>
                    <strong style="color: #00ff88; font-size: 0.9rem;">{trofeo}</strong>
                </div>
                """, unsafe_allow_html=True)
    
    # Diploma digital
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="cyber-container" style="text-align: center; background: linear-gradient(135deg, rgba(0,0,0,0.8), rgba(0,255,136,0.1));">
        <h3 style="font-family: 'Orbitron', sans-serif; color: #ffd93d; font-size: 1.8rem;">
            📜 CERTIFICADO DE MAESTRÍA EN METADATOS
        </h3>
        <p style="font-family: 'Rajdhani', sans-serif; color: #ccd6f6; font-size: 1.1rem;">
            Por completar satisfactoriamente todos los niveles<br>
            y demostrar conocimientos excepcionales en:<br>
            <strong style="color: #00ff88;">Clasificación • Relación • Orden • Recuperación de Metadatos</strong>
        </p>
        <div style="border: 1px solid #00ff88; padding: 15px; margin: 20px; border-radius: 10px;">
            <p style="font-family: 'Courier New', monospace; color: #00ff88; font-size: 0.8rem;">
                HASH DE VERIFICACIÓN: 0x7F3A9B2C1D4E5F6A8B9C0D1E2F3A4B5C<br>
                FECHA: {time.strftime('%Y-%m-%d %H:%M:%S')}<br>
                NIVEL DE ACCESO: MAESTRO
            </p>
        </div>
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
