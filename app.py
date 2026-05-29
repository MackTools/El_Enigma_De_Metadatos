import streamlit as st
import random
import time
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN INICIAL DE LA PÁGINA
# ============================================================================
st.set_page_config(
    page_title="El Enigma de los Metadatos",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS PERSONALIZADO - ESTILO INDUSTRIAL FUTURISTA
# ============================================================================
def aplicar_estilo_hud():
    st.markdown("""
    <style>
        /* Importar fuentes */
        @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap');
        
        /* Fondo general */
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 30%, #16213e 60%, #0f3460 100%);
            background-attachment: fixed;
        }
        
        /* Overlay de textura industrial */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 2px,
                    rgba(255, 255, 255, 0.03) 2px,
                    rgba(255, 255, 255, 0.03) 4px
                ),
                radial-gradient(circle at 50% 50%, rgba(255, 140, 0, 0.05) 0%, transparent 70%);
            pointer-events: none;
            z-index: -1;
        }
        
        /* Tipografía principal */
        .main-title {
            font-family: 'Share Tech Mono', monospace;
            color: #ff6b00;
            text-shadow: 0 0 10px rgba(255, 107, 0, 0.5), 0 0 20px rgba(255, 107, 0, 0.3);
            font-size: 3.5rem;
            text-align: center;
            letter-spacing: 4px;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-family: 'Rajdhani', sans-serif;
            color: #a0a0a0;
            text-align: center;
            font-size: 1.2rem;
            letter-spacing: 3px;
            margin-bottom: 2rem;
        }
        
        /* Marco HUD */
        .hud-frame {
            border: 2px solid rgba(255, 107, 0, 0.3);
            border-radius: 8px;
            padding: 20px;
            background: rgba(10, 10, 10, 0.7);
            box-shadow: 
                inset 0 0 30px rgba(0, 0, 0, 0.5),
                0 0 20px rgba(255, 107, 0, 0.1);
            position: relative;
        }
        
        .hud-frame::before {
            content: "◆";
            position: absolute;
            top: -10px;
            left: 20px;
            color: #ff6b00;
            font-size: 20px;
        }
        
        .hud-frame::after {
            content: "◆";
            position: absolute;
            bottom: -10px;
            right: 20px;
            color: #ff6b00;
            font-size: 20px;
        }
        
        /* Mapa de progreso */
        .map-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 107, 0, 0.2);
            border-radius: 10px;
            margin: 20px 0;
            position: relative;
        }
        
        .map-node {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            z-index: 1;
        }
        
        .node-circle {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Share Tech Mono', monospace;
            font-size: 1.5rem;
            border: 2px solid;
            position: relative;
        }
        
        .node-circle.locked {
            background: #1a1a1a;
            border-color: #333;
            color: #666;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        
        .node-circle.unlocked {
            background: #0a0a0a;
            border-color: #ff6b00;
            color: #ff6b00;
            box-shadow: 0 0 15px rgba(255, 107, 0, 0.5);
            animation: pulse 2s infinite;
        }
        
        .node-circle.completed {
            background: #0a2a0a;
            border-color: #00ff00;
            color: #00ff00;
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
        }
        
        .node-line {
            flex-grow: 1;
            height: 3px;
            background: #333;
            margin: 0 -2px;
            z-index: 0;
        }
        
        .node-line.active {
            background: linear-gradient(90deg, #ff6b00, #ff6b00);
            box-shadow: 0 0 10px rgba(255, 107, 0, 0.5);
        }
        
        .node-line.completed {
            background: linear-gradient(90deg, #00ff00, #00ff00);
            box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 15px rgba(255, 107, 0, 0.5); }
            50% { box-shadow: 0 0 25px rgba(255, 107, 0, 0.8); }
            100% { box-shadow: 0 0 15px rgba(255, 107, 0, 0.5); }
        }
        
        /* Botones personalizados */
        .cyber-button {
            background: linear-gradient(45deg, #1a1a1a, #2a2a2a);
            border: 2px solid #ff6b00;
            color: #ff6b00;
            font-family: 'Share Tech Mono', monospace;
            padding: 10px 25px;
            font-size: 1.1rem;
            cursor: pointer;
            border-radius: 4px;
            transition: all 0.3s;
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
        }
        
        .cyber-button:hover {
            background: #ff6b00;
            color: #000;
            box-shadow: 0 0 30px rgba(255, 107, 0, 0.6);
            transform: translateY(-2px);
        }
        
        /* Mensajes de feedback */
        .success-message {
            background: rgba(0, 255, 0, 0.1);
            border: 1px solid #00ff00;
            color: #00ff00;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Share Tech Mono', monospace;
            margin: 15px 0;
            animation: slideIn 0.5s ease;
        }
        
        .error-message {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            color: #ff0000;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Share Tech Mono', monospace;
            margin: 15px 0;
            animation: shake 0.5s ease;
        }
        
        @keyframes slideIn {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }
        
        /* Terminal style */
        .terminal {
            background: #0a0a0a;
            border: 1px solid #333;
            padding: 15px;
            font-family: 'Share Tech Mono', monospace;
            color: #00ff00;
            margin: 15px 0;
            border-radius: 4px;
        }
        
        /* Ocultar elementos de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# INICIALIZACIÓN DEL ESTADO DE LA SESIÓN
# ============================================================================
def inicializar_estado():
    if 'progreso' not in st.session_state:
        st.session_state.progreso = {
            'nodo1': False,  # Clasificación
            'nodo2': False,  # Relación
            'nodo3': False,  # Orden lógico
            'nodo4': False,  # Enigma final
        }
    if 'nodo_actual' not in st.session_state:
        st.session_state.nodo_actual = 1
    if 'intentos' not in st.session_state:
        st.session_state.intentos = 0
    if 'mensaje_feedback' not in st.session_state:
        st.session_state.mensaje_feedback = None

# ============================================================================
# COMPONENTE: MAPA DE PROGRESO
# ============================================================================
def mostrar_mapa_progreso():
    st.markdown("### MAPA DE NODOS DE RECUPERACIÓN")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 0.5, 1, 0.5, 1, 1])
    
    nodos = [
        ("N1", "Clasificación", 1),
        ("N2", "Relación", 2),
        ("N3", "Orden", 3),
        ("N4", "Recuperación", 4)
    ]
    
    with col1:
        estado = st.session_state.progreso['nodo1']
        clase = "completed" if estado else "unlocked" if st.session_state.nodo_actual == 1 else "locked"
        st.markdown(f"""
        <div class="map-node">
            <div class="node-circle {clase}">N1</div>
            <span style="color: {'#00ff00' if estado else '#ff6b00' if st.session_state.nodo_actual == 1 else '#666'}; 
                        font-size: 0.8rem; margin-top: 5px;">CLASIFICACIÓN</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        estado_linea = "completed" if st.session_state.progreso['nodo1'] else "active" if st.session_state.nodo_actual > 1 else ""
        st.markdown(f"<div class='node-line {estado_linea}'></div>", unsafe_allow_html=True)
    
    with col3:
        estado = st.session_state.progreso['nodo2']
        clase = "completed" if estado else "unlocked" if st.session_state.nodo_actual == 2 else "locked"
        st.markdown(f"""
        <div class="map-node">
            <div class="node-circle {clase}">N2</div>
            <span style="color: {'#00ff00' if estado else '#ff6b00' if st.session_state.nodo_actual == 2 else '#666'}; 
                        font-size: 0.8rem; margin-top: 5px;">RELACIÓN</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        estado_linea = "completed" if st.session_state.progreso['nodo2'] else "active" if st.session_state.nodo_actual > 2 else ""
        st.markdown(f"<div class='node-line {estado_linea}'></div>", unsafe_allow_html=True)
    
    with col5:
        estado = st.session_state.progreso['nodo3']
        clase = "completed" if estado else "unlocked" if st.session_state.nodo_actual == 3 else "locked"
        st.markdown(f"""
        <div class="map-node">
            <div class="node-circle {clase}">N3</div>
            <span style="color: {'#00ff00' if estado else '#ff6b00' if st.session_state.nodo_actual == 3 else '#666'}; 
                        font-size: 0.8rem; margin-top: 5px;">ORDEN</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        estado_linea = "completed" if st.session_state.progreso['nodo3'] else "active" if st.session_state.nodo_actual > 3 else ""
        st.markdown(f"<div class='node-line {estado_linea}'></div>", unsafe_allow_html=True)
    
    with col7:
        estado = st.session_state.progreso['nodo4']
        clase = "completed" if estado else "unlocked" if st.session_state.nodo_actual == 4 else "locked"
        st.markdown(f"""
        <div class="map-node">
            <div class="node-circle {clase}">N4</div>
            <span style="color: {'#00ff00' if estado else '#ff6b00' if st.session_state.nodo_actual == 4 else '#666'}; 
                        font-size: 0.8rem; margin-top: 5px;">RECUPERACIÓN</span>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# JUEGO 1: CLASIFICACIÓN DE METADATOS
# ============================================================================
def juego_clasificacion():
    st.markdown("## 🎯 NODO 1: CLASIFICACIÓN DE METADATOS")
    st.markdown("*Identifica qué elementos son metadatos y cuáles son datos de contenido*")
    
    if st.session_state.progreso['nodo1']:
        st.success("✅ Nodo completado - Base de datos parcialmente restaurada")
        return
    
    # Definir elementos para clasificar
    elementos = [
        {"nombre": "Fecha de creación del archivo", "es_metadato": True},
        {"nombre": "Autor del documento", "es_metadato": True},
        {"nombre": "Contenido del texto del documento", "es_metadato": False},
        {"nombre": "Formato del archivo (PDF, DOCX)", "es_metadato": True},
        {"nombre": "Tamaño del archivo en bytes", "es_metadato": True},
        {"nombre": "Párrafo principal del documento", "es_metadato": False},
        {"nombre": "Fecha de última modificación", "es_metadato": True},
        {"nombre": "Imagen incluida en el documento", "es_metadato": False},
    ]
    
    # Inicializar selección si no existe
    if 'clasificacion_seleccion' not in st.session_state:
        st.session_state.clasificacion_seleccion = {}
    
    st.markdown("#### 📊 Selecciona los METADATOS de la lista:")
    st.markdown("*Marca las casillas de los elementos que consideres METADATOS*")
    
    # Crear checkboxes para cada elemento
    for i, elemento in enumerate(elementos):
        key = f"check_{i}"
        st.session_state.clasificacion_seleccion[key] = st.checkbox(
            elemento["nombre"], 
            value=st.session_state.clasificacion_seleccion.get(key, False),
            key=key
        )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔍 VERIFICAR CLASIFICACIÓN", key="verificar_clasificacion"):
            # Verificar respuestas
            correctas = 0
            total_metadatos = sum(1 for e in elementos if e["es_metadato"])
            
            for i, elemento in enumerate(elementos):
                key = f"check_{i}"
                seleccion_usuario = st.session_state.clasificacion_seleccion.get(key, False)
                if seleccion_usuario == elemento["es_metadato"]:
                    correctas += 1
            
            if correctas == len(elementos):
                st.session_state.progreso['nodo1'] = True
                st.session_state.mensaje_feedback = {
                    'tipo': 'exito',
                    'mensaje': '🔓 ¡CLASIFICACIÓN CORRECTA! Los metadatos describen propiedades del archivo, no su contenido.'
                }
                st.rerun()
            else:
                st.session_state.intentos += 1
                st.session_state.mensaje_feedback = {
                    'tipo': 'error',
                    'mensaje': f'⚠️ Clasificación incorrecta. Recuerda: los metadatos son "datos sobre los datos", no el contenido en sí.'
                }
                st.rerun()
    
    # Mostrar feedback
    if st.session_state.mensaje_feedback:
        if st.session_state.mensaje_feedback['tipo'] == 'exito':
            st.markdown(f"""
            <div class="success-message">
                {st.session_state.mensaje_feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.mensaje_feedback = None
            st.rerun()
        else:
            st.markdown(f"""
            <div class="error-message">
                {st.session_state.mensaje_feedback['mensaje']}<br>
                Intentos: {st.session_state.intentos}
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# JUEGO 2: RELACIÓN ARCHIVO-METADATO
# ============================================================================
def juego_relacion():
    st.markdown("## 🔗 NODO 2: RELACIÓN ARCHIVO-METADATO")
    st.markdown("*Une cada tipo de archivo con su metadato más característico*")
    
    if not st.session_state.progreso['nodo1']:
        st.warning("⚠️ Debes completar el Nodo 1 primero")
        return
    
    if st.session_state.progreso['nodo2']:
        st.success("✅ Nodo completado - Relaciones establecidas correctamente")
        return
    
    # Pares archivo-metadato
    pares = {
        "Fotografía digital": "Datos EXIF (apertura, ISO, velocidad)",
        "Documento de Word": "Autor y fecha de última edición",
        "Archivo de audio MP3": "Etiquetas ID3 (artista, álbum, género)",
        "Página Web HTML": "Meta tags (description, keywords)"
    }
    
    st.markdown("#### 🗂️ Selecciona el metadato correcto para cada archivo:")
    
    respuestas = {}
    archivos = list(pares.keys())
    opciones = list(pares.values())
    random.shuffle(opciones)
    
    for archivo in archivos:
        respuestas[archivo] = st.selectbox(
            f"**{archivo}**:",
            options=["Selecciona un metadato..."] + opciones,
            key=f"relacion_{archivo}"
        )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔗 VERIFICAR RELACIONES", key="verificar_relacion"):
            correctas = 0
            for archivo, metadato_correcto in pares.items():
                if respuestas[archivo] == metadato_correcto:
                    correctas += 1
            
            if correctas == len(pares):
                st.session_state.progreso['nodo2'] = True
                st.session_state.mensaje_feedback = {
                    'tipo': 'exito',
                    'mensaje': '🔓 ¡RELACIONES CORRECTAS! Cada tipo de archivo tiene metadatos específicos según su naturaleza.'
                }
                st.rerun()
            else:
                st.session_state.intentos += 1
                st.session_state.mensaje_feedback = {
                    'tipo': 'error',
                    'mensaje': f'⚠️ {len(pares) - correctas} relación(es) incorrecta(s). Piensa en qué información describe mejor cada tipo de archivo.'
                }
                st.rerun()
    
    # Mostrar feedback
    if st.session_state.mensaje_feedback:
        if st.session_state.mensaje_feedback['tipo'] == 'exito':
            st.markdown(f"""
            <div class="success-message">
                {st.session_state.mensaje_feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.mensaje_feedback = None
            st.rerun()
        else:
            st.markdown(f"""
            <div class="error-message">
                {st.session_state.mensaje_feedback['mensaje']}<br>
                Intentos: {st.session_state.intentos}
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# JUEGO 3: ORDEN LÓGICO DE METADATOS
# ============================================================================
def juego_orden():
    st.markdown("## 📋 NODO 3: ORDEN LÓGICO DE METADATOS")
    st.markdown("*Ordena correctamente el flujo de trabajo con metadatos*")
    
    if not st.session_state.progreso['nodo2']:
        st.warning("⚠️ Debes completar el Nodo 2 primero")
        return
    
    if st.session_state.progreso['nodo3']:
        st.success("✅ Nodo completado - Flujo de metadatos establecido")
        return
    
    # Pasos del flujo de metadatos
    pasos_desordenados = [
        "Consulta y búsqueda de archivos",
        "Almacenamiento en base de datos",
        "Captura o generación del metadato",
        "Indexación para búsqueda rápida",
        "Extracción automática de metadatos"
    ]
    
    orden_correcto = [
        "Captura o generación del metadato",
        "Extracción automática de metadatos",
        "Almacenamiento en base de datos",
        "Indexación para búsqueda rápida",
        "Consulta y búsqueda de archivos"
    ]
    
    st.markdown("#### 🔄 Ordena los pasos del flujo de metadatos (1 = primer paso, 5 = último):")
    st.markdown("*Enumera del 1 al 5 según el orden lógico del proceso*")
    
    orden_usuario = {}
    
    for i, paso in enumerate(pasos_desordenados):
        orden_usuario[paso] = st.selectbox(
            f"**{paso}**",
            options=["Seleccionar orden..."] + list(range(1, 6)),
            key=f"orden_{i}"
        )
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📋 VERIFICAR ORDEN", key="verificar_orden"):
            # Verificar que todos los números son únicos
            numeros_usados = [v for v in orden_usuario.values() if v != "Seleccionar orden..."]
            
            if len(set(numeros_usados)) != 5:
                st.session_state.mensaje_feedback = {
                    'tipo': 'error',
                    'mensaje': '⚠️ Debes asignar un número diferente a cada paso (1-5)'
                }
                st.rerun()
            else:
                # Verificar orden
                correcto = True
                for paso, orden in orden_usuario.items():
                    indice_correcto = orden_correcto.index(paso) + 1
                    if orden != indice_correcto:
                        correcto = False
                        break
                
                if correcto:
                    st.session_state.progreso['nodo3'] = True
                    st.session_state.mensaje_feedback = {
                        'tipo': 'exito',
                        'mensaje': '🔓 ¡ORDEN CORRECTO! Los metadatos siguen un flujo lógico: captura → extracción → almacenamiento → indexación → consulta'
                    }
                    st.rerun()
                else:
                    st.session_state.intentos += 1
                    st.session_state.mensaje_feedback = {
                        'tipo': 'error',
                        'mensaje': '⚠️ Orden incorrecto. Piensa en el ciclo de vida de los metadatos.'
                    }
                    st.rerun()
    
    # Mostrar feedback
    if st.session_state.mensaje_feedback:
        if st.session_state.mensaje_feedback['tipo'] == 'exito':
            st.markdown(f"""
            <div class="success-message">
                {st.session_state.mensaje_feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.mensaje_feedback = None
            st.rerun()
        else:
            st.markdown(f"""
            <div class="error-message">
                {st.session_state.mensaje_feedback['mensaje']}<br>
                Intentos: {st.session_state.intentos}
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# JUEGO 4: ENIGMA FINAL
# ============================================================================
def enigma_final():
    st.markdown("## 🔐 NODO 4: ENIGMA FINAL - RECUPERACIÓN DE BASE DE DATOS")
    st.markdown("*Resuelve el acertijo final para restaurar completamente la base de datos*")
    
    if not st.session_state.progreso['nodo3']:
        st.warning("⚠️ Debes completar el Nodo 3 primero")
        return
    
    if st.session_state.progreso['nodo4']:
        st.balloons()
        st.success("🎉 ¡BASE DE DATOS COMPLETAMENTE RESTAURADA! ¡MISIÓN CUMPLIDA!")
        
        # Mostrar resumen final
        st.markdown("""
        <div class="hud-frame">
            <h3 style="color: #00ff00; text-align: center;">📊 RESUMEN DE LA MISIÓN</h3>
            <div class="terminal">
                > Estado: RECUPERACIÓN COMPLETA<br>
                > Nodos completados: 4/4<br>
                > Metadatos restaurados: 100%<br>
                > Base de datos: OPERATIVA<br>
                > Hacker: NEUTRALIZADO<br><br>
                > Gracias a tu conocimiento sobre metadatos,<br>
                > has logrado recuperar información crítica.<br>
                > Los metadatos son fundamentales para la<br>
                > organización y recuperación de información.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Preguntas del enigma final
    preguntas = [
        {
            "pregunta": "¿Cuál es el propósito principal de los metadatos en una base de datos?",
            "opciones": [
                "A) Hacer que los archivos sean más pesados",
                "B) Describir, organizar y facilitar la búsqueda de datos",
                "C) Encriptar el contenido de los archivos",
                "D) Eliminar información innecesaria"
            ],
            "respuesta_correcta": 1  # índice 1 = opción B
        },
        {
            "pregunta": "Si encuentras un archivo sin metadatos, ¿qué problema principal enfrentarías?",
            "opciones": [
                "A) El archivo no se puede abrir",
                "B) Sería difícil determinar su origen, autor y contexto",
                "C) El archivo ocuparía más espacio",
                "D) El archivo se eliminaría automáticamente"
            ],
            "respuesta_correcta": 1  # índice 1 = opción B
        }
    ]
    
    st.markdown("#### 🧩 Responde correctamente a las preguntas para restaurar la base de datos:")
    
    respuestas_usuario = {}
    
    for i, pregunta in enumerate(preguntas):
        st.markdown(f"**Pregunta {i+1}:** {pregunta['pregunta']}")
        respuestas_usuario[i] = st.radio(
            "Selecciona tu respuesta:",
            options=range(len(pregunta['opciones'])),
            format_func=lambda x: pregunta['opciones'][x],
            key=f"enigma_{i}"
        )
        st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔑 VERIFICAR RESPUESTAS", key="verificar_enigma"):
            correctas = sum(1 for i, pregunta in enumerate(preguntas) 
                          if respuestas_usuario.get(i) == pregunta['respuesta_correcta'])
            
            if correctas == len(preguntas):
                st.session_state.progreso['nodo4'] = True
                st.session_state.mensaje_feedback = {
                    'tipo': 'exito',
                    'mensaje': '🔓 ¡ENIGMA RESUELTO! Has demostrado comprender la importancia de los metadatos.'
                }
                st.rerun()
            else:
                st.session_state.intentos += 1
                st.session_state.mensaje_feedback = {
                    'tipo': 'error',
                    'mensaje': f'⚠️ {len(preguntas) - correctas} respuesta(s) incorrecta(s). Los metadatos son descriptores, no el contenido en sí.'
                }
                st.rerun()
    
    # Mostrar feedback
    if st.session_state.mensaje_feedback:
        if st.session_state.mensaje_feedback['tipo'] == 'exito':
            st.markdown(f"""
            <div class="success-message">
                {st.session_state.mensaje_feedback['mensaje']}
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
            st.session_state.mensaje_feedback = None
            st.rerun()
        else:
            st.markdown(f"""
            <div class="error-message">
                {st.session_state.mensaje_feedback['mensaje']}<br>
                Intentos: {st.session_state.intentos}
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================
def main():
    # Aplicar estilos
    aplicar_estilo_hud()
    
    # Inicializar estado
    inicializar_estado()
    
    # Título principal
    st.markdown('<h1 class="main-title">EL ENIGMA DE LOS METADATOS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">◆ RECUPERACIÓN DE BASE DE DATOS INDUSTRIAL ◆</p>', unsafe_allow_html=True)
    
    # Marco HUD con contexto
    st.markdown("""
    <div class="hud-frame" style="margin-bottom: 30px;">
        <div class="terminal">
            > ALERTA: Base de datos comprometida<br>
            > Un hacker ha eliminado metadatos críticos<br>
            > Misión: Recuperar la información mediante ingeniería de metadatos<br>
            > Completa los 4 nodos para restaurar el sistema<br>
            > Estado: <span style="color: #ff6b00;">EN PROGRESO</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar mapa de progreso
    mostrar_mapa_progreso()
    
    # Determinar qué juego mostrar según el progreso
    st.markdown("---")
    
    # Lógica de navegación entre nodos
    if not st.session_state.progreso['nodo1']:
        st.session_state.nodo_actual = 1
    elif not st.session_state.progreso['nodo2']:
        st.session_state.nodo_actual = 2
    elif not st.session_state.progreso['nodo3']:
        st.session_state.nodo_actual = 3
    elif not st.session_state.progreso['nodo4']:
        st.session_state.nodo_actual = 4
    else:
        st.session_state.nodo_actual = 4
    
    # Contenedor principal para el juego activo
    with st.container():
        st.markdown('<div class="hud-frame">', unsafe_allow_html=True)
        
        # Mostrar el juego correspondiente al nodo actual
        if st.session_state.nodo_actual == 1:
            juego_clasificacion()
        elif st.session_state.nodo_actual == 2:
            juego_relacion()
        elif st.session_state.nodo_actual == 3:
            juego_orden()
        elif st.session_state.nodo_actual == 4:
            enigma_final()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Información adicional en sidebar
    with st.sidebar:
        st.markdown("## 📊 ESTADÍSTICAS DE MISIÓN")
        st.markdown(f"""
        <div class="terminal" style="font-size: 0.9rem;">
            > Nodos completados: {sum(st.session_state.progreso.values())}/4<br>
            > Intentos totales: {st.session_state.intentos}<br>
            > Progreso: {int(sum(st.session_state.progreso.values())/4*100)}%<br>
            > Estado: {'COMPLETADA' if all(st.session_state.progreso.values()) else 'EN PROGRESO'}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("## ℹ️ ACERCA DE LOS METADATOS")
        st.info("""
        Los metadatos son **"datos sobre los datos"**. 
        
        Describen características como:
        - Fecha de creación
        - Autor
        - Formato
        - Tamaño
        
        Son fundamentales para organizar, buscar y gestionar información digital.
        """)
        
        if all(st.session_state.progreso.values()):
            if st.button("🔄 REINICIAR MISIÓN", key="reiniciar"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()

# ============================================================================
# EJECUCIÓN PRINCIPAL
# ============================================================================
if __name__ == "__main__":
    main()