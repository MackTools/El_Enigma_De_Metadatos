"""
ESTILOS VISUALES - Tema Cyberpunk Industrial
=============================================
Diseño inmersivo tipo juego con efectos visuales avanzados
"""

def obtener_css_principal():
    """Retorna todo el CSS principal del juego"""
    return """
    <style>
        /* ============================================
           FUENTES Y TIPOGRAFÍA
           ============================================ */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
        
        /* ============================================
           FONDO Y ATMÓSFERA
           ============================================ */
        .stApp {
            background: #0a0a0f;
            background-image: 
                radial-gradient(ellipse at 20% 50%, rgba(0, 255, 255, 0.05) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 20%, rgba(255, 0, 255, 0.05) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 80%, rgba(0, 255, 136, 0.05) 0%, transparent 50%);
        }
        
        /* Efecto de grid tecnológico */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 255, 0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            pointer-events: none;
            z-index: -1;
            animation: gridMove 20s linear infinite;
        }
        
        @keyframes gridMove {
            0% { background-position: 0 0; }
            100% { background-position: 50px 50px; }
        }
        
        /* ============================================
           TÍTULOS Y ENCABEZADOS
           ============================================ */
        .game-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 3.5rem;
            font-weight: 900;
            text-align: center;
            background: linear-gradient(45deg, #00ffff, #00ff88, #00ffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 40px rgba(0, 255, 255, 0.5);
            letter-spacing: 5px;
            margin: 30px 0;
            animation: titleGlow 3s ease-in-out infinite;
        }
        
        @keyframes titleGlow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }
        
        .game-subtitle {
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.3rem;
            font-weight: 500;
            text-align: center;
            color: #8892b0;
            letter-spacing: 8px;
            text-transform: uppercase;
            margin-bottom: 40px;
        }
        
        /* ============================================
           CONTENEDORES Y MARCOS
           ============================================ */
        .cyber-container {
            background: rgba(10, 10, 20, 0.8);
            border: 1px solid rgba(0, 255, 255, 0.2);
            border-radius: 12px;
            padding: 30px;
            position: relative;
            backdrop-filter: blur(10px);
            box-shadow: 
                0 0 30px rgba(0, 255, 255, 0.1),
                inset 0 0 30px rgba(0, 0, 0, 0.5);
            margin: 20px 0;
        }
        
        .cyber-container::before {
            content: '';
            position: absolute;
            top: -1px;
            left: -1px;
            right: -1px;
            bottom: -1px;
            border-radius: 13px;
            background: linear-gradient(45deg, 
                transparent 0%, 
                rgba(0, 255, 255, 0.3) 50%, 
                transparent 100%);
            z-index: -1;
            animation: borderGlow 3s linear infinite;
        }
        
        @keyframes borderGlow {
            0% { opacity: 0.3; }
            50% { opacity: 0.7; }
            100% { opacity: 0.3; }
        }
        
        /* Panel de información */
        .info-panel {
            background: rgba(0, 255, 255, 0.05);
            border-left: 4px solid #00ffff;
            padding: 20px;
            border-radius: 0 8px 8px 0;
            font-family: 'Rajdhani', sans-serif;
            color: #ccd6f6;
            font-size: 1.1rem;
            margin: 20px 0;
        }
        
        /* ============================================
           MAPA DE NAVEGACIÓN
           ============================================ */
        .map-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 30px 20px;
            margin: 30px 0;
            background: rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(0, 255, 255, 0.15);
            border-radius: 12px;
            position: relative;
        }
        
        .map-node {
            position: relative;
            z-index: 2;
            text-align: center;
        }
        
        .node-circle {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.8rem;
            font-weight: 700;
            position: relative;
            transition: all 0.5s ease;
            margin: 0 auto;
        }
        
        .node-locked {
            background: rgba(20, 20, 30, 0.8);
            border: 2px solid #333;
            color: #555;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.5);
        }
        
        .node-active {
            background: rgba(0, 255, 255, 0.1);
            border: 2px solid #00ffff;
            color: #00ffff;
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.4);
            animation: nodePulse 2s infinite;
        }
        
        .node-completed {
            background: rgba(0, 255, 136, 0.15);
            border: 2px solid #00ff88;
            color: #00ff88;
            box-shadow: 0 0 25px rgba(0, 255, 136, 0.3);
        }
        
        @keyframes nodePulse {
            0%, 100% { box-shadow: 0 0 30px rgba(0, 255, 255, 0.4); }
            50% { box-shadow: 0 0 50px rgba(0, 255, 255, 0.8); }
        }
        
        .node-label {
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.9rem;
            font-weight: 600;
            margin-top: 8px;
            letter-spacing: 2px;
            text-transform: uppercase;
        }
        
        .connection-line {
            flex-grow: 1;
            height: 3px;
            background: #1a1a2e;
            margin: 0 10px;
            position: relative;
            z-index: 1;
        }
        
        .line-active {
            background: linear-gradient(90deg, #00ffff, #00ff88);
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
        }
        
        .line-completed {
            background: #00ff88;
            box-shadow: 0 0 15px rgba(0, 255, 136, 0.5);
        }
        
        /* ============================================
           BOTONES INTERACTIVOS
           ============================================ */
        .cyber-button {
            background: linear-gradient(135deg, rgba(0, 255, 255, 0.1), rgba(0, 255, 136, 0.1));
            border: 2px solid #00ffff;
            color: #00ffff;
            font-family: 'Orbitron', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            padding: 12px 30px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 3px;
            position: relative;
            overflow: hidden;
            width: 100%;
        }
        
        .cyber-button:hover {
            background: rgba(0, 255, 255, 0.2);
            border-color: #00ff88;
            color: #00ff88;
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.5);
            transform: translateY(-2px);
        }
        
        .cyber-button:active {
            transform: translateY(1px);
        }
        
        /* ============================================
           TARJETAS PARA JUEGOS
           ============================================ */
        .game-card {
            background: rgba(20, 20, 40, 0.6);
            border: 1px solid rgba(0, 255, 255, 0.2);
            border-radius: 10px;
            padding: 20px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.1rem;
            color: #ccd6f6;
            text-align: center;
        }
        
        .game-card:hover {
            border-color: #00ffff;
            box-shadow: 0 0 25px rgba(0, 255, 255, 0.3);
            transform: translateY(-5px);
            background: rgba(0, 255, 255, 0.1);
        }
        
        .game-card.selected {
            border-color: #00ff88;
            background: rgba(0, 255, 136, 0.15);
            color: #00ff88;
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
        }
        
        /* ============================================
           MENSAJES Y NOTIFICACIONES
           ============================================ */
        .success-message {
            background: rgba(0, 255, 136, 0.1);
            border: 2px solid #00ff88;
            color: #00ff88;
            padding: 20px;
            border-radius: 10px;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.2rem;
            text-align: center;
            animation: slideInRight 0.5s ease;
        }
        
        .error-message {
            background: rgba(255, 0, 85, 0.1);
            border: 2px solid #ff0055;
            color: #ff0055;
            padding: 20px;
            border-radius: 10px;
            font-family: 'Rajdhani', sans-serif;
            font-size: 1.2rem;
            text-align: center;
            animation: shake 0.5s ease;
        }
        
        @keyframes slideInRight {
            from { transform: translateX(-50px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            20% { transform: translateX(-10px); }
            40% { transform: translateX(10px); }
            60% { transform: translateX(-10px); }
            80% { transform: translateX(10px); }
        }
        
        /* ============================================
           TERMINAL DE HACKER
           ============================================ */
        .terminal {
            background: #000;
            border: 1px solid #00ff88;
            border-radius: 8px;
            padding: 20px;
            font-family: 'Courier New', monospace;
            color: #00ff88;
            font-size: 0.9rem;
            line-height: 1.6;
        }
        
        .terminal::before {
            content: '> ';
            color: #00ffff;
        }
        
        /* ============================================
           PREMIO FINAL
           ============================================ */
        .trophy-container {
            text-align: center;
            padding: 40px;
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.1), rgba(0, 255, 255, 0.1));
            border-radius: 20px;
            border: 2px solid #00ff88;
            animation: trophyGlow 2s infinite;
        }
        
        @keyframes trophyGlow {
            0%, 100% { box-shadow: 0 0 30px rgba(0, 255, 136, 0.3); }
            50% { box-shadow: 0 0 60px rgba(0, 255, 136, 0.6); }
        }
        
        /* ============================================
           OCULTAR ELEMENTOS STREAMLIT
           ============================================ */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Scrollbar personalizada */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0a0f;
        }
        ::-webkit-scrollbar-thumb {
            background: #00ffff;
            border-radius: 4px;
        }
    </style>
    """