"""
NIVEL 3: ORDEN CRONOLÓGICO
===========================
Timeline interactivo para ordenar el flujo de metadatos
"""

import streamlit as st
import time
from utils.estado import completar_nivel, mostrar_feedback

def nivel3_ordenar():
    """Juego de ordenamiento: Timeline de metadatos"""
    
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00ffff; font-size: 2rem;">
            ▸ NIVEL 03: LÍNEA TEMPORAL ◂
        </h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: #8892b0; font-size: 1.1rem;">
            Ordena correctamente el ciclo de vida de los metadatos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-panel">
        <strong>🎯 OBJETIVO:</strong> Los metadatos siguen un flujo lógico desde su creación hasta su uso.<br>
        <strong>💡 PISTA:</strong> Primero se crean, luego se almacenan, después se organizan y finalmente se consultan.
    </div>
    """, unsafe_allow_html=True)
    
    # Si ya completó este nivel
    if st.session_state.niveles_completados[3]:
        st.markdown("""
        <div class="success-message">
            ✅ NIVEL COMPLETADO - Flujo de metadatos optimizado
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Pasos del flujo (desordenados)
    pasos = [
        {"id": 1, "texto": "Creación del archivo digital", "icono": "📄"},
        {"id": 2, "texto": "Generación automática de metadatos", "icono": "⚙️"},
        {"id": 3, "texto": "Almacenamiento en base de datos", "icono": "💾"},
        {"id": 4, "texto": "Indexación para búsquedas rápidas", "icono": "🔍"},
        {"id": 5, "texto": "Recuperación y consulta de archivos", "icono": "📂"},
    ]
    
    # Orden correcto
    orden_correcto = [1, 2, 3, 4, 5]
    
    st.markdown("""
    <h4 style="font-family: 'Orbitron', sans-serif; color: #00ffff; text-align: center; margin: 30px 0;">
        ▼ ORDENA LOS PASOS DEL 1 AL 5 ▼
    </h4>
    """, unsafe_allow_html=True)
    
    # Mostrar timeline visual
    orden_usuario = {}
    
    for i, paso in enumerate(pasos):
        col1, col2 = st.columns([0.1, 0.9])
        
        with col1:
            st.markdown(f"""
            <div style="font-size: 2rem; text-align: center; line-height: 60px;">
                {paso['icono']}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            orden_usuario[paso['id']] = st.selectbox(
                f"**{paso['texto']}**",
                options=["Selecciona el orden (1-5)..."] + list(range(1, 6)),
                key=f"n3_paso_{paso['id']}",
            )
        
        if i < len(pasos) - 1:
            st.markdown("""
            <div style="text-align: center; color: #00ffff; font-size: 1.5rem; margin: 10px 0;">
                ↓
            </div>
            """, unsafe_allow_html=True)
    
    # Verificación
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("⏱️ VERIFICAR ORDEN", key="verificar_n3", use_container_width=True):
            # Verificar que todos los números son diferentes
            valores = [v for v in orden_usuario.values() if v != "Selecciona el orden (1-5)..."]
            
            if len(valores) != 5:
                mostrar_feedback('error', 'Debes asignar un orden a todos los pasos (1 al 5).')
                st.rerun()
            elif len(set(valores)) != 5:
                mostrar_feedback('error', 'No puedes repetir números. Cada paso debe tener un orden único.')
                st.rerun()
            else:
                # Verificar orden correcto
                es_correcto = all(orden_usuario[paso_id] == idx + 1 
                                for idx, paso_id in enumerate(orden_correcto))
                
                if es_correcto:
                    st.session_state.intentos_totales += 1
                    completar_nivel(3, 300)
                    mostrar_feedback('exito', '¡ORDEN PERFECTO! Los metadatos siguen este flujo: crear → extraer → almacenar → indexar → consultar.')
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.session_state.intentos_totales += 1
                    mostrar_feedback('error', 'El orden no es correcto. Piensa: ¿qué ocurre primero?')
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