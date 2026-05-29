"""
NIVEL 2: EL DETECTIVE DE ARCHIVOS
==================================
Juego de memoria y deducción visual para conectar archivos con metadatos
"""

import streamlit as st
import random
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel2_relacionar():
    """Juego de detective: Encontrar pistas de cada archivo"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 02: EL DETECTIVE DE ARCHIVOS ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Investiga cada archivo y descubre su metadato secreto
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-panel">
        <strong>🔍 MISIÓN:</strong> Eres un detective digital. Cada archivo escondió una pista sobre sí mismo.<br>
        <strong>🖱️ CÓMO JUGAR:</strong> Haz click en cada archivo para revelar sus pistas. Luego selecciona la pista correcta.
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.niveles_completados[2]:
        st.markdown("""
        <div class="success-message">
            ✅ CASO RESUELTO - Todos los archivos identificados correctamente
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Inicializar estado
    if 'archivo_actual' not in st.session_state:
        st.session_state.archivo_actual = 0
    if 'pistas_encontradas' not in st.session_state:
        st.session_state.pistas_encontradas = {}
    if 'archivos_resueltos' not in st.session_state:
        st.session_state.archivos_resueltos = []
    
    # Datos de los archivos misteriosos
    casos = [
        {
            "id": 1,
            "archivo": "Fotografía Misteriosa",
            "icono": "📸",
            "color": "#ff6b6b",
            "descripcion": "Una imagen encontrada en la cámara de seguridad",
            "pistas": [
                "Tiene datos de la cámara que la tomó",
                "Muestra una fiesta de cumpleaños",
                "Pesa 2.5 megabytes",
                "Se tomó un lunes"
            ],
            "pista_correcta": 0,
            "metadato": "Datos EXIF: modelo de cámara, fecha, hora, ubicación GPS"
        },
        {
            "id": 2,
            "archivo": "Documento Secreto",
            "icono": "📝",
            "color": "#4ecdc4",
            "descripcion": "Un archivo de texto con información clasificada",
            "pistas": [
                "Contiene una receta de cocina",
                "Registra quién lo escribió y cuándo",
                "Está escrito en español",
                "Tiene 5 páginas"
            ],
            "pista_correcta": 1,
            "metadato": "Propiedades del documento: autor, fecha de creación, última edición"
        },
        {
            "id": 3,
            "archivo": "Audio Enigmático",
            "icono": "🎵",
            "color": "#ffd93d",
            "descripcion": "Una grabación de audio encontrada en el servidor",
            "pistas": [
                "Suena música rock",
                "Dura 3 minutos con 42 segundos",
                "Tiene etiquetas con nombre del artista y álbum",
                "Se escuchan aplausos"
            ],
            "pista_correcta": 2,
            "metadato": "Etiquetas ID3: artista, álbum, año, género musical, duración"
        },
        {
            "id": 4,
            "archivo": "Página Web Perdida",
            "icono": "🌐",
            "color": "#a855f7",
            "descripcion": "Un sitio web que desapareció de los buscadores",
            "pistas": [
                "Tiene fondo de color azul",
                "Muestra fotos de vacaciones",
                "Contiene etiquetas ocultas con título y descripción",
                "Se carga en 2 segundos"
            ],
            "pista_correcta": 2,
            "metadato": "Meta tags HTML: título, descripción, palabras clave para buscadores"
        }
    ]
    
    # Mezclar casos para aleatoriedad
    if 'casos_mezclados' not in st.session_state:
        st.session_state.casos_mezclados = random.sample(casos, len(casos))
    
    casos_orden = st.session_state.casos_mezclados
    
    # Mostrar progreso
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <span style="font-family: 'Orbitron', sans-serif; color: #00ff88; font-size: 1.2rem;">
            🔍 CASOS RESUELTOS: {len(st.session_state.archivos_resueltos)} / {len(casos)}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar archivos como casos pendientes o resueltos
    for caso in casos_orden:
        if caso['id'] in st.session_state.archivos_resueltos:
            # Caso resuelto
            st.markdown(f"""
            <div style="background: rgba(0, 255, 136, 0.1); border: 2px solid #00ff88; 
                        border-radius: 15px; padding: 20px; margin: 10px 0;">
                <span style="font-size: 2rem;">{caso['icono']}</span>
                <strong style="color: #00ff88; font-family: 'Rajdhani', sans-serif; font-size: 1.2rem;">
                    {caso['archivo']} - ¡RESUELTO!
                </strong>
                <p style="color: #00ff88; margin: 5px 0;">✅ {caso['metadato']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Caso pendiente - Mostrar como tarjeta interactiva
            with st.expander(f"{caso['icono']} {caso['archivo']} - {caso['descripcion']}", expanded=False):
                st.markdown(f"""
                <div style="background: rgba({','.join(str(int(caso['color'].lstrip('#')[i:i+2], 16)) for i in (0, 2, 4))}, 0.1); 
                            padding: 15px; border-radius: 10px; margin: 10px 0;">
                    <h4 style="color: {caso['color']}; font-family: 'Rajdhani', sans-serif; margin: 0;">
                        🔎 PISTAS ENCONTRADAS:
                    </h4>
                </div>
                """, unsafe_allow_html=True)
                
                # Mostrar pistas como botones
                pistas_aleatorias = random.sample(list(enumerate(caso['pistas'])), len(caso['pistas']))
                
                for idx_original, pista in pistas_aleatorias:
                    if st.button(f"🔍 {pista}", key=f"pista_{caso['id']}_{idx_original}", use_container_width=True):
                        if idx_original == caso['pista_correcta']:
                            # ¡Correcto!
                            st.session_state.archivos_resueltos.append(caso['id'])
                            st.session_state.pistas_encontradas[caso['id']] = True
                            st.rerun()
                        else:
                            st.error("❌ ¡Esta no es la pista correcta! Sigue investigando...")
    
    # Verificar si todos los casos están resueltos
    if len(st.session_state.archivos_resueltos) == len(casos):
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🏆 PRESENTAR INFORME FINAL", key="verificar_n2", use_container_width=True):
                st.session_state.intentos_totales += 1
                completar_nivel(2, 200)
                mostrar_feedback('exito', '¡INFORME COMPLETADO! Has descubierto que cada tipo de archivo guarda diferentes metadatos sobre sí mismo.')
                time.sleep(2)
                # Limpiar estado
                for key in ['archivo_actual', 'pistas_encontradas', 'archivos_resueltos', 'casos_mezclados']:
                    if key in st.session_state:
                        del st.session_state[key]
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
