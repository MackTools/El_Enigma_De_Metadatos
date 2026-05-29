"""
EL ENIGMA DE LOS METADATOS - VERSIÓN INFANTIL
==============================================
App educativa interactiva sobre metadatos
Diseñada para niños de primaria y secundaria
Estilo: Cyberpunk colorido con animaciones divertidas
"""

import streamlit as st
import random
import time

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================
st.set_page_config(
    page_title="El Enigma de los Metadatos 🕵️",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CSS DIVERTIDO Y COLORIDO PARA NIÑOS
# ============================================================================
def aplicar_estilos():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@400;700&display=swap');
        
        /* Fondo con gradiente animado */
        .stApp {
            background: linear-gradient(135deg, #1a0033 0%, #0d1b3e 50%, #1a0a2e 100%);
            animation: fondoMov 10s ease infinite;
            background-size: 400% 400%;
        }
        
        @keyframes fondoMov {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Estrellitas de fondo */
        .stApp::before {
            content: "✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            color: rgba(255, 255, 255, 0.05);
            font-size: 24px;
            letter-spacing: 20px;
            pointer-events: none;
            z-index: -1;
            animation: estrellas 3s linear infinite;
        }
        
        @keyframes estrellas {
            0% { opacity: 0.3; }
            50% { opacity: 0.6; }
            100% { opacity: 0.3; }
        }
        
        /* Título principal */
        .titulo-principal {
            font-family: 'Bangers', cursive;
            font-size: 4rem;
            text-align: center;
            background: linear-gradient(45deg, #ff6b6b, #ffd93d, #6bcb77, #4d96ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: arcoiris 3s linear infinite;
            filter: drop-shadow(0 0 20px rgba(255,255,255,0.5));
            margin: 20px 0;
        }
        
        @keyframes arcoiris {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }
        
        /* Subtítulo */
        .subtitulo {
            font-family: 'Comic Neue', cursive;
            color: #ffd93d;
            text-align: center;
            font-size: 1.5rem;
            animation: flotar 2s ease-in-out infinite;
        }
        
        @keyframes flotar {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        /* Marco de juego */
        .marco-juego {
            background: rgba(0, 0, 0, 0.6);
            border: 3px solid #4d96ff;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(77, 150, 255, 0.3), inset 0 0 30px rgba(0,0,0,0.5);
            margin: 20px 0;
            position: relative;
            overflow: hidden;
        }
        
        .marco-juego::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(77, 150, 255, 0.1), transparent, rgba(255, 217, 61, 0.1), transparent);
            animation: girar 10s linear infinite;
            z-index: -1;
        }
        
        @keyframes girar {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Tarjetas de opciones */
        .tarjeta-opcion {
            background: linear-gradient(135deg, #2a1a4e, #1a2a4e);
            border: 2px solid #4d96ff;
            border-radius: 15px;
            padding: 20px;
            margin: 10px;
            cursor: pointer;
            transition: all 0.3s;
            font-family: 'Comic Neue', cursive;
            font-size: 1.2rem;
            color: white;
            text-align: center;
        }
        
        .tarjeta-opcion:hover {
            transform: scale(1.05) rotate(-2deg);
            border-color: #ffd93d;
            box-shadow: 0 0 25px rgba(255, 217, 61, 0.5);
            background: linear-gradient(135deg, #3a2a6e, #2a3a6e);
        }
        
        /* Botones */
        .boton-aventura {
            background: linear-gradient(45deg, #ff6b6b, #ffd93d);
            border: none;
            color: #1a0033;
            font-family: 'Bangers', cursive;
            font-size: 1.5rem;
            padding: 15px 40px;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            animation: pulso 2s infinite;
            text-transform: uppercase;
            letter-spacing: 3px;
        }
        
        .boton-aventura:hover {
            transform: scale(1.1);
            box-shadow: 0 0 40px rgba(255, 217, 61, 0.8);
        }
        
        @keyframes pulso {
            0%, 100% { box-shadow: 0 0 10px rgba(255, 107, 107, 0.5); }
            50% { box-shadow: 0 0 30px rgba(255, 217, 61, 0.8); }
        }
        
        /* Mensajes */
        .mensaje-exito {
            background: rgba(107, 203, 119, 0.3);
            border: 2px solid #6bcb77;
            color: #6bcb77;
            padding: 20px;
            border-radius: 15px;
            font-family: 'Comic Neue', cursive;
            font-size: 1.5rem;
            text-align: center;
            animation: celebrar 0.5s ease;
        }
        
        @keyframes celebrar {
            0% { transform: scale(0); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        
        .mensaje-error {
            background: rgba(255, 107, 107, 0.3);
            border: 2px solid #ff6b6b;
            color: #ff6b6b;
            padding: 20px;
            border-radius: 15px;
            font-family: 'Comic Neue', cursive;
            font-size: 1.2rem;
            text-align: center;
            animation: temblar 0.5s ease;
        }
        
        @keyframes temblar {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px) rotate(-2deg); }
            75% { transform: translateX(10px) rotate(2deg); }
        }
        
        /* Mapa */
        .mapa-nodo {
            display: inline-block;
            width: 80px;
            height: 80px;
            border-radius: 50%;
            line-height: 80px;
            text-align: center;
            font-family: 'Bangers', cursive;
            font-size: 2rem;
            margin: 10px;
            transition: all 0.3s;
        }
        
        .nodo-bloqueado { background: #333; color: #666; border: 3px solid #444; }
        .nodo-activo { 
            background: #2a1a4e; 
            color: #ffd93d; 
            border: 3px solid #ffd93d;
            animation: pulso 1.5s infinite;
        }
        .nodo-completado { 
            background: #1a4e2a; 
            color: #6bcb77; 
            border: 3px solid #6bcb77;
        }
        
        /* Emojis grandes */
        .emoji-grande {
            font-size: 5rem;
            text-align: center;
            animation: flotar 2s ease-in-out infinite;
        }
        
        /* Ocultar cosas de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Scrollbar bonita */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #1a0033;
        }
        ::-webkit-scrollbar-thumb {
            background: #4d96ff;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# ESTADO INICIAL
# ============================================================================
def iniciar_estado():
    if 'nivel' not in st.session_state:
        st.session_state.nivel = 1
    if 'completados' not in st.session_state:
        st.session_state.completados = []
    if 'puntos' not in st.session_state:
        st.session_state.puntos = 0

# ============================================================================
# MAPA DE AVENTURA
# ============================================================================
def mostrar_mapa():
    st.markdown("### 🗺️ MAPA DE LA AVENTURA")
    
    cols = st.columns(7)
    
    niveles = [
        ("🔍", "Pista 1", 1),
        ("🧩", "Pista 2", 2),
        ("🔗", "Pista 3", 3),
        ("🏆", "Final", 4)
    ]
    
    for i, (col, (emoji, nombre, num)) in enumerate(zip([cols[0], cols[2], cols[4], cols[6]], niveles)):
        with col:
            if num in st.session_state.completados:
                clase = "nodo-completado"
            elif num == st.session_state.nivel:
                clase = "nodo-activo"
            else:
                clase = "nodo-bloqueado"
            
            st.markdown(f"""
            <div style="text-align: center;">
                <div class="mapa-nodo {clase}">{emoji}</div>
                <div style="color: {'#6bcb77' if num in st.session_state.completados else '#ffd93d' if num == st.session_state.nivel else '#666'}; 
                            font-family: 'Comic Neue', cursive;">
                    {nombre}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Flechas entre nodos
    for i in [1, 3, 5]:
        with cols[i]:
            st.markdown(f"""
            <div style="text-align: center; color: {'#ffd93d' if st.session_state.nivel > (i+1)//2 else '#666'}; font-size: 2rem;">
                ➡️
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# NIVEL 1: ROMPECABEZAS DE CLASIFICACIÓN
# ============================================================================
def nivel1_rompecabezas():
    st.markdown("## 🧩 PISTA 1: ¡ENCUENTRA LOS METADATOS!")
    st.markdown("*Arrastra las piezas correctas al cofre del tesoro*")
    
    if 1 in st.session_state.completados:
        st.balloons()
        st.success("🎉 ¡Primera pista encontrada!")
        return
    
    # Piezas del rompecabezas (metadatos vs contenido)
    piezas = [
        {"texto": "📅 Fecha de creación", "es_metadato": True, "emoji": "✅"},
        {"texto": "👤 Nombre del autor", "es_metadato": True, "emoji": "✅"},
        {"texto": "📄 El texto de la carta", "es_metadato": False, "emoji": "❌"},
        {"texto": "📏 Tamaño del archivo", "es_metadato": True, "emoji": "✅"},
        {"texto": "🖼️ La foto dentro del documento", "es_metadato": False, "emoji": "❌"},
        {"texto": "🕒 Hora de modificación", "es_metadato": True, "emoji": "✅"}
    ]
    
    st.markdown("### 🎯 Selecciona las piezas que son METADATOS (datos sobre datos)")
    st.markdown("*Pista: Los metadatos describen el archivo, no son el contenido*")
    
    # Mostrar piezas como tarjetas clickeables
    seleccionados = {}
    cols = st.columns(3)
    
    for i, pieza in enumerate(piezas):
        with cols[i % 3]:
            if st.button(f"{pieza['texto']}", key=f"pieza_{i}", use_container_width=True):
                if i not in seleccionados:
                    seleccionados[i] = True
                else:
                    seleccionados[i] = not seleccionados[i]
    
    # Checkboxes más simples
    st.markdown("---")
    st.markdown("### 📋 Marca los metadatos:")
    
    respuestas = []
    for i, pieza in enumerate(piezas):
        if st.checkbox(pieza['texto'], key=f"check_n1_{i}"):
            respuestas.append(i)
    
    if st.button("🔍 ¡VERIFICAR!", key="verificar1", use_container_width=True):
        correctas = sum(1 for i in respuestas if piezas[i]["es_metadato"])
        incorrectas = sum(1 for i in respuestas if not piezas[i]["es_metadato"])
        
        if incorrectas == 0 and correctas == sum(1 for p in piezas if p["es_metadato"]):
            st.session_state.completados.append(1)
            st.session_state.puntos += 100
            st.session_state.nivel = 2
            st.rerun()
        else:
            st.error(f"❌ ¡Casi! Tienes {correctas} correctas pero {incorrectas} incorrectas")
            st.info("💡 Recuerda: Los metadatos son información SOBRE el archivo, no lo que hay DENTRO")

# ============================================================================
# NIVEL 2: MEMORAMA DE RELACIONES
# ============================================================================
def nivel2_memorama():
    st.markdown("## 🎴 PISTA 2: ¡ENCUENTRA LAS PAREJAS!")
    st.markdown("*Juego de memoria: une cada archivo con su metadato*")
    
    if 2 in st.session_state.completados:
        st.success("🎉 ¡Segunda pista descubierta!")
        return
    
    # Tarjetas del memorama
    archivos = ["📸 Foto digital", "📝 Documento", "🎵 Canción MP3", "🌐 Página Web"]
    metadatos = ["EXIF (cámara, fecha)", "Autor y fecha", "Artista y álbum", "Título y descripción"]
    
    st.markdown("### 🎯 Une cada archivo con su metadato correcto")
    
    selecciones = {}
    cols = st.columns(2)
    
    for i, archivo in enumerate(archivos):
        with cols[0]:
            st.markdown(f"**{archivo}**")
        with cols[1]:
            selecciones[archivo] = st.selectbox(
                f"Metadato para {archivo}",
                ["¿Cuál será? 🤔"] + metadatos,
                key=f"memo_{i}"
            )
    
    if st.button("🎯 ¡COMPROBAR PAREJAS!", key="verificar2", use_container_width=True):
        parejas_correctas = {
            "📸 Foto digital": "EXIF (cámara, fecha)",
            "📝 Documento": "Autor y fecha",
            "🎵 Canción MP3": "Artista y álbum",
            "🌐 Página Web": "Título y descripción"
        }
        
        aciertos = sum(1 for archivo, meta in parejas_correctas.items() 
                      if selecciones[archivo] == meta)
        
        if aciertos == 4:
            st.session_state.completados.append(2)
            st.session_state.puntos += 200
            st.session_state.nivel = 3
            st.balloons()
            st.rerun()
        else:
            st.error(f"❌ Tienes {aciertos} de 4 correctas. ¡Sigue intentando!")
            st.info("💡 Piensa: ¿Qué información describe mejor cada tipo de archivo?")

# ============================================================================
# NIVEL 3: ORDENA LA HISTORIA
# ============================================================================
def nivel3_ordenar():
    st.markdown("## 📜 PISTA 3: ¡ORDENA LA HISTORIA!")
    st.markdown("*Pon en orden cómo viajan los metadatos*")
    
    if 3 in st.session_state.completados:
        st.success("🎉 ¡Tercera pista encontrada!")
        return
    
    # Historia desordenada
    pasos = [
        "🔍 Buscamos el archivo",
        "📸 Creamos el archivo",
        "💾 Guardamos la información",
        "🏷️ Se generan los metadatos",
        "📂 Organizamos para encontrar después"
    ]
    
    orden_correcto = [
        "📸 Creamos el archivo",
        "🏷️ Se generan los metadatos",
        "💾 Guardamos la información",
        "📂 Organizamos para encontrar después",
        "🔍 Buscamos el archivo"
    ]
    
    st.markdown("### 🎯 Ordena los pasos (1 = primero, 5 = último)")
    st.markdown("*¿Qué pasa primero cuando creas un archivo?*")
    
    orden_usuario = {}
    for i, paso in enumerate(pasos):
        orden_usuario[paso] = st.selectbox(
            paso,
            ["Elige el orden..."] + list(range(1, 6)),
            key=f"orden_{i}"
        )
    
    if st.button("✅ ¡VERIFICAR ORDEN!", key="verificar3", use_container_width=True):
        numeros_usados = [v for v in orden_usuario.values() if v != "Elige el orden..."]
        
        if len(set(numeros_usados)) != 5:
            st.error("❌ ¡Usa todos los números del 1 al 5 sin repetir!")
        else:
            es_correcto = True
            for paso, num in orden_usuario.items():
                if orden_correcto.index(paso) + 1 != num:
                    es_correcto = False
                    break
            
            if es_correcto:
                st.session_state.completados.append(3)
                st.session_state.puntos += 300
                st.session_state.nivel = 4
                st.balloons()
                st.rerun()
            else:
                st.error("❌ El orden no es correcto. Piensa: ¿qué viene primero?")

# ============================================================================
# NIVEL 4: PREGUNTA FINAL
# ============================================================================
def nivel4_final():
    st.markdown("## 🏆 ¡EL TESORO FINAL!")
    st.markdown("*Responde la pregunta para recuperar la base de datos*")
    
    if 4 in st.session_state.completados:
        st.balloons()
        st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <div class="emoji-grande">🎉🏆🎉</div>
            <h2 style="color: #ffd93d; font-family: 'Bangers', cursive; font-size: 3rem;">
                ¡MISIÓN COMPLETADA!
            </h2>
            <p style="color: white; font-family: 'Comic Neue', cursive; font-size: 1.5rem;">
                ¡Has recuperado la base de datos!<br>
                Puntuación total: {} puntos 🌟
            </p>
            <p style="color: #6bcb77; font-family: 'Comic Neue', cursive;">
                Los metadatos son como etiquetas mágicas que nos ayudan<br>
                a encontrar y organizar nuestros archivos 📁✨
            </p>
        </div>
        """.format(st.session_state.puntos), unsafe_allow_html=True)
        
        if st.button("🔄 ¡JUGAR DE NUEVO!", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        return
    
    st.markdown("### 🤔 ¿Para qué sirven los metadatos?")
    
    respuesta = st.radio(
        "Elige la respuesta correcta:",
        [
            "A) Para hacer los archivos más pesados 🏋️",
            "B) Para decorar los documentos 🎨",
            "C) Para describir y encontrar archivos fácilmente 🏷️",
            "D) Para borrar información 🗑️"
        ],
        key="pregunta_final"
    )
    
    if st.button("🔑 ¡RESPUESTA FINAL!", key="verificar4", use_container_width=True):
        if "C" in respuesta:
            st.session_state.completados.append(4)
            st.session_state.puntos += 500
            st.session_state.nivel = 4
            st.balloons()
            st.rerun()
        else:
            st.error("❌ ¡No es correcto! Lee bien las opciones")
            st.info("💡 Pista: Los metadatos nos ayudan a saber QUÉ es cada archivo sin abrirlo")

# ============================================================================
# INTERFAZ PRINCIPAL
# ============================================================================
def main():
    aplicar_estilos()
    iniciar_estado()
    
    # Título con animación
    st.markdown('<h1 class="titulo-principal">🕵️ EL ENIGMA DE LOS METADATOS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitulo">🔍 ¡Ayuda a recuperar la base de datos perdida! 🔍</p>', unsafe_allow_html=True)
    
    # Marco de historia
    st.markdown("""
    <div class="marco-juego">
        <p style="color: white; font-family: 'Comic Neue', cursive; font-size: 1.3rem; text-align: center;">
            😱 ¡Un travieso hacker borró información importante!<br>
            🦸 Necesitamos tu ayuda para recuperar los <strong style="color: #ffd93d;">METADATOS</strong><br>
            🧩 Resuelve las 4 pistas para salvar la base de datos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Mostrar mapa
    mostrar_mapa()
    
    # Puntuación
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        <span style="color: #ffd93d; font-family: 'Bangers', cursive; font-size: 1.5rem;">
            ⭐ Puntos: {st.session_state.puntos}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Mostrar nivel actual
    with st.container():
        st.markdown('<div class="marco-juego">', unsafe_allow_html=True)
        
        if st.session_state.nivel == 1:
            nivel1_rompecabezas()
        elif st.session_state.nivel == 2:
            nivel2_memorama()
        elif st.session_state.nivel == 3:
            nivel3_ordenar()
        elif st.session_state.nivel == 4:
            nivel4_final()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Sidebar divertida
    with st.sidebar:
        st.markdown("## 🌟 TU AVENTURA")
        
        progreso = len(st.session_state.completados)
        st.progress(progreso / 4)
        
        st.markdown(f"""
        <div style="font-family: 'Comic Neue', cursive; color: white;">
            🧩 Pistas encontradas: {progreso}/4<br>
            ⭐ Puntos totales: {st.session_state.puntos}<br>
            🎯 Nivel actual: {st.session_state.nivel}
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 💡 ¿QUÉ SON LOS METADATOS?")
        st.info("""
        ¡Son como **etiquetas mágicas**! 🏷️
        
        Imagina que tienes una caja de juguetes:
        - 📅 **Cuándo** lo guardaste
        - 👤 **Quién** lo guardó
        - 📏 **Qué tan grande** es la caja
        - 📝 **Qué tipo** de juguete es
        
        ¡Eso son los metadatos! Datos que describen otros datos.
        """)
        
        if st.button("🔄 REINICIAR AVENTURA", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# ============================================================================
# EJECUTAR
# ============================================================================
if __name__ == "__main__":
    main()
