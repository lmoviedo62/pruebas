from typing import Literal

EmotionType = Literal["muy_mal", "triste", "neutral", "bien", "muy_bien"]

# ========== DETECCIÓN DE CRISIS ==========
def detect_crisis(text: str) -> bool:
    """Detecta palabras clave de crisis suicida o autolesión"""
    crisis_keywords = [
        "suicidio", "suicidarme", "matarme", "morir", "muerte", "acabar", 
        "terminar todo", "no quiero vivir", "mejor muerto", "muerta",
        "hacerme daño", "lastimarme", "cortarme", "quitarme la vida",
        "ya no aguanto", "no vale la pena", "desaparecer"
    ]
    
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in crisis_keywords)


def get_crisis_response() -> str:
    """Respuesta de emergencia para situaciones de crisis"""
    return """🆘 NECESITAS AYUDA PROFESIONAL INMEDIATA

Siento mucho que estés pasando por tanto dolor. Lo que sientes es real, pero hay personas que pueden ayudarte AHORA.

📞 CONTACTA INMEDIATAMENTE:

🔴 Línea 106 - Línea de la vida (24/7, gratuita)
🔴 Línea 123 - Emergencias
🔴 Bienestar Universitario: bienestar@ucatolica.edu.co

NO ESTÁS SOLO/A. TU VIDA ES VALIOSA.

Si estás en peligro inmediato, ve al servicio de urgencias más cercano o llama al 123."""


def get_emotion_response(emotion: EmotionType) -> dict:
    """Respuestas con contenido práctico para cada emoción"""
    
    responses = {
        "muy_mal": {
            "mensaje": """💜 Lamento que te sientas así. Lo que experimentas es válido.

⚠️ SI HAS PENSADO EN HACERTE DAÑO, contacta YA:
• Línea 106 (24/7)
• bienestar@ucatolica.edu.co
• 123 Emergencias

¿Cómo te gustaría que te apoye?""",
            
            "opciones": [
                {
                    "id": "respiracion_crisis",
                    "label": "🫁 Ejercicio de respiración urgente",
                    "contenido": """🫁 RESPIRACIÓN 4-7-8 (Calma inmediata)

1. INHALA por la nariz: 1-2-3-4
2. SOSTÉN: 1-2-3-4-5-6-7
3. EXHALA por la boca: 1-2-3-4-5-6-7-8

Repite 4 veces.

Después del 2do ciclo sentirás más calma.
Después del 4to tu corazón habrá bajado.

Hazlo AHORA. 💜"""
                },
                
                {
                    "id": "consejo_crisis",
                    "label": "💭 Mensaje de esperanza",
                    "contenido": """💭 PARA TI EN ESTE MOMENTO

• Este momento es TEMPORAL
• Has sobrevivido al 100% de tus peores días
• Los pensamientos NO son hechos
• Pedir ayuda es VALENTÍA, no debilidad

Habrá días mejores. Tu futuro yo te agradece que sigas aquí.

Contacta Bienestar: bienestar@ucatolica.edu.co
O Línea 106 (24/7)

¿Qué UNA cosa puedes hacer HOY para cuidarte? 💜"""
                },
                
                {
                    "id": "grounding_crisis",
                    "label": "⚓ Técnica de grounding 5-4-3-2-1",
                    "contenido": """⚓ TÉCNICA 5-4-3-2-1 (Volver al presente)

Nombra en voz alta:

5 cosas que VES
4 cosas que TOCAS
3 cosas que OYES
2 cosas que HUELES
1 cosa que SABOREAS

Esto te ancla al momento presente y detiene pensamientos negativos.

¿Cómo te sientes ahora? ⚓"""
                },
                
                {
                    "id": "recursos_crisis",
                    "label": "🆘 Contactos de ayuda inmediata",
                    "contenido": """🆘 RECURSOS AHORA

📞 Línea 106 - 24/7, gratuita, confidencial
📞 Línea 123 - Emergencias
📧 bienestar@ucatolica.edu.co - Atención psicológica
📞 Línea 155 - Salud Mental

¿Qué decir? "Estoy pasando por un momento muy difícil y necesito hablar."

NO tienes que enfrentarlo solo/a. 💜"""
                }
            ]
        },
        
        "triste": {
            "mensaje": """💙 Entiendo tu tristeza. Es una emoción válida que nos conecta con lo que valoramos.

A veces los pensamientos se vuelven más negativos de lo necesario. Trabajemos juntos.

¿Qué necesitas?""",
            
            "opciones": [
                {
                    "id": "meditacion_tristeza",
                    "label": "🧘 Meditación de aceptación (10 min)",
                    "contenido": """🧘 MEDITACIÓN DE ACEPTACIÓN

1. Siéntate cómodo, cierra los ojos
2. Respira naturalmente 2 minutos
3. Nota DÓNDE sientes la tristeza (pecho, garganta, estómago)
4. Respira HACIA esa sensación. No la cambies, solo acompáñala
5. Repite: "Está bien sentir esto. Soy humano/a. Esto pasará"
6. Coloca una mano en tu corazón. Siente su calor
7. Abre los ojos gradualmente

La tristeza es como una ola. Si luchas, te arrastra. Si observas, pasa sobre ti. 💙"""
                },
                
                {
                    "id": "consejo_tristeza",
                    "label": "💬 Mensaje de apoyo emocional",
                    "contenido": """💬 PARA TU TRISTEZA

Está bien no estar bien. Permitirte sentir es honestidad, no debilidad.

Esto NO durará para siempre. Las emociones son temporales.

Eres más fuerte de lo que crees. Estás AQUÍ, buscando ayuda.

PERMISO PARA:
✅ Llorar cuando lo necesites
✅ Pedir apoyo sin culpa
✅ Tomarte tu tiempo
✅ Priorizarte

¿Qué UNA cosa necesita tu cuerpo/mente ahora? (descanso, comida, movimiento, conexión)

Bienestar: bienestar@ucatolica.edu.co 💙"""
                },
                
                {
                    "id": "activacion_tristeza",
                    "label": "⚡ Ideas para activarme",
                    "contenido": """⚡ ROMPE EL CICLO

La inactividad EMPEORA la tristeza. Acciones pequeñas:

NIVEL BÁSICO:
□ Lávate la cara con agua fría
□ Toma agua
□ Abre una ventana 5 min
□ Ponte ropa limpia

NIVEL MEDIO:
□ Camina 10 minutos
□ Llama a alguien
□ Escucha UNA canción
□ Ordena UN objeto

REGLA DE ORO: "No necesito ganas para hacerlo. Hacerlo me dará ganas."

Elige UNA ahora. ⚡"""
                },
                
                {
                    "id": "recurso_tristeza",
                    "label": "📚 Entender la tristeza",
                    "contenido": """📚 QUÉ ES LA TRISTEZA

FUNCIONES:
• Te dice qué es importante
• Te pide hacer una pausa
• Te conecta con otros

TRISTEZA vs DEPRESIÓN:

Tristeza normal:
• Evento específico
• Días/semanas
• No interfiere mucho
• Puedes disfrutar algunas cosas

Depresión (busca ayuda):
• Sin causa clara
• Más de 2 semanas
• Afecta trabajo/estudio
• No disfrutas NADA
• Cambios en sueño/apetito

⚠️ Si tienes 5+ síntomas de depresión, contacta Bienestar. 📚"""
                }
            ]
        },
        
        "neutral": {
            "mensaje": """😌 Gracias por compartir que te sientes neutral.

Es un buen momento para fortalecer recursos emocionales y prepararte para el futuro.

¿En qué trabajamos hoy?""",
            
            "opciones": [
                {
                    "id": "respiracion_neutral",
                    "label": "🌬️ Respiración coherente",
                    "contenido": """🌬️ RESPIRACIÓN COHERENTE (Equilibrio)

INHALA 5 segundos
EXHALA 5 segundos

Practica 2 minutos mínimo (12 ciclos).

CUÁNDO USAR:
☀️ Mañana → Energiza
🌙 Noche → Mejor sueño
📚 Antes de estudiar → Concentración
🎭 Antes de evento → Reduce ansiedad

Beneficios: Semana 1 más calma, Semana 2 mejor estrés, Semana 3 mejor sueño. 🌬️"""
                },
                
                {
                    "id": "mindfulness_neutral",
                    "label": "🧘 Mindfulness 5 minutos",
                    "contenido": """🧘 MINDFULNESS BÁSICO

1. Siéntate cómodo, espalda recta
2. Cierra los ojos
3. Respira natural 2 min (solo observa)
4. Nota sensaciones en tu cuerpo 1 min
5. Escucha sonidos 1 min
6. Respira profundo 3 veces, abre ojos

BENEFICIOS:
✓ Reduce estrés
✓ Mejora concentración
✓ Aumenta autoconciencia

Practica 5 min al día durante 1 semana. 🧘"""
                },
                
                {
                    "id": "autoconocimiento_neutral",
                    "label": "🔍 Ejercicio de autoconocimiento",
                    "contenido": """🔍 CONÓCETE MEJOR

MIS EMOCIONES FRECUENTES:
¿Cuáles siento más? (ansiedad, tristeza, alegría, calma)
_______________________

MIS DESENCADENANTES:
¿Qué situaciones activan emociones difíciles?
_______________________

MIS RECURSOS:
¿Qué fortalezas tengo?
_______________________

MI RED DE APOYO:
¿A quién puedo acudir?
_______________________

NECESIDADES BÁSICAS (1-10):
Sueño: __ Alimentación: __ Ejercicio: __
Social: __ Tiempo para mí: __

Conocerte es un proceso continuo. 🔍"""
                },
                
                {
                    "id": "herramientas_neutral",
                    "label": "🛠️ Construir mi caja de herramientas",
                    "contenido": """🛠️ TU CAJA DE HERRAMIENTAS

PARA ANSIEDAD:
✓ Respiración 4-7-8
✓ Grounding 5-4-3-2-1
✓ Caminar 10 min

PARA TRISTEZA:
✓ Activación (hacer algo pequeño)
✓ Llamar a alguien
✓ Escribir en diario

PARA ENERGÍA:
✓ Dormir bien (7-9h)
✓ Comer nutritivo
✓ Luz solar 20 min

Esta semana, prueba UNA herramienta nueva cada día.

No esperes a estar en crisis. Practica ahora. 🛠️"""
                }
            ]
        },

        "bien": {
            "mensaje": """🌟 ¡Me alegra que te sientas bien!

Es importante reconocer y fortalecer lo que funciona. El bienestar es resultado de tus acciones.

¿Qué fortalecemos hoy?""",
            
            "opciones": [
                {
                    "id": "gratitud_bien",
                    "label": "🙏 Ejercicio de gratitud",
                    "contenido": """🙏 GRATITUD DIARIA

Escribe 3 cosas específicas:

1. Algo pequeño que disfrutaste hoy:
_______________________

2. Algo que alguien hizo por ti:
_______________________

3. Algo sobre ti que aprecias:
_______________________

DESAFÍO 7 DÍAS:
Cada noche, 3 cosas diferentes.

Resultado: Tu cerebro buscará automáticamente cosas buenas. 🙏"""
                },
                
                {
                    "id": "fortalezas_bien",
                    "label": "💪 Identificar mis fortalezas",
                    "contenido": """💪 TUS FORTALEZAS

Marca las que reconoces:

□ Curiosidad
□ Perseverancia
□ Honestidad
□ Bondad
□ Valentía
□ Creatividad
□ Gratitud
□ Humor
□ Liderazgo
□ Prudencia

TUS TOP 3:
1. _______________________
2. _______________________
3. _______________________

DESAFÍO: Usa una de forma nueva esta semana.

Tus fortalezas son tu superpoder. 💪"""
                },
                
                {
                    "id": "mantener_bien",
                    "label": "🔐 Mantener este bienestar",
                    "contenido": """🔐 PROTEGE TU BIENESTAR

¿QUÉ ESTÁ FUNCIONANDO?
_______________________

3 HÁBITOS NO NEGOCIABLES:
1. _______________________
2. _______________________
3. _______________________

SEÑALES DE ALERTA (actúa aquí):
□ Pospongo actividades
□ Duermo mal
□ Evito gente
□ Más irritable

SI BAJO DE ÁNIMO:
Paso 1 (24h): _______________________
Paso 2 (2-3 días): _______________________
Paso 3 (1 semana): Contactar Bienestar

Mantener es más fácil que recuperar. 🔐"""
                },
                
                {
                    "id": "recurso_bien",
                    "label": "📖 Ciencia del bienestar (PERMA)",
                    "contenido": """📖 FÓRMULA DEL BIENESTAR

P - Emociones Positivas (alegría, gratitud)
E - Compromiso (flow, usar fortalezas)
R - Relaciones (conexiones significativas)
M - Significado (propósito)
A - Logros (metas, progreso)

EVALÚA (1-10):
P: __ E: __ R: __ M: __ A: __

¿Cuál necesita más atención?
_______________________

ACCIÓN HOY:
_______________________

Bienestar = cultivar estas 5 áreas. 📖"""
                }
            ]
        },
        
        "muy_bien": {
            "mensaje": """✨ ¡Qué maravilloso que te sientas muy bien!

Tu bienestar refleja que muchas cosas están funcionando. Vamos a consolidar y celebrar.

¿Qué hacemos?""",
            
            "opciones": [
                {
                    "id": "respiracion_celebracion",
                    "label": "🌟 Respiración de celebración",
                    "contenido": """🌟 RESPIRACIÓN DE GRATITUD

Siéntate cómodo. Cierra los ojos.

INHALA (5 seg): Imagina luz dorada llenando tu cuerpo
EXHALA (5 seg): Sonríe suavemente, siente gratitud

Repite 5 veces, pensando:
"Estoy aquí. Estoy bien. Estoy agradecido/a."

Siente tu corazón. Siente tu fuerza.

Este momento es tuyo. Celébralo. 🌟"""
                },
                
                {
                    "id": "consejo_celebracion",
                    "label": "🎉 Celebrar mis logros",
                    "contenido": """🎉 RECONOCE TU PROGRESO

LOGROS RECIENTES:
• _______________________
• _______________________
• _______________________

QUÉ HICISTE PARA LLEGAR AQUÍ:
_______________________

LECCIÓN APRENDIDA:
_______________________

MENSAJE PARA TI:

Has trabajado duro. Has crecido. Has resistido.

Tu valor NO depende de:
✗ Calificaciones
✗ Productividad
✗ Aprobación de otros

Tu valor es inherente. Existes = importas.

Sigue adelante. 🎉"""
                },
                
                {
                    "id":" meditacion_compasion",
                    "label": "💝 Meditación de autocompasión",
                    "contenido": """💝 AUTOCOMPASIÓN

Siéntate cómodo. Mano en tu corazón.

Repite mentalmente:

"Estoy orgulloso/a de mí."
"He hecho lo mejor que puedo."
"Merezco amabilidad, incluida la mía."
"Celebro quien soy hoy."

Respira profundo. Siente el calor de tu mano.

Eres suficiente. Siempre lo has sido. 💝"""
                },
                
                {
                    "id": "compartir_bien",
                    "label": "🤝 Compartir mi bienestar con otros",
                    "contenido": """🤝 COMPARTIR TU LUZ

Cuando estás bien, puedes ayudar a otros.

IDEAS:
□ Envía un mensaje amable a alguien
□ Pregunta de verdad "¿cómo estás?"
□ Comparte lo que te ha ayudado
□ Ofrece tu tiempo/escucha
□ Sonríe a alguien hoy

ACCIÓN HOY:
_______________________

Tu bienestar puede inspirar a otros.

Brilla. 🤝"""
                }
            ]
        }
    }
    
    return responses[emotion]


def respond_free_text(text: str) -> str:
    """Respuesta a texto libre con detección de crisis"""
    
    # Detectar crisis
    if detect_crisis(text):
        return get_crisis_response()
    
    # Respuesta general empática
    return """Gracias por confiar en Serena y compartir lo que sientes.

Tus emociones son válidas. No tienes que enfrentarlo solo/a.

RECURSOS:
• Bienestar: bienestar@ucatolica.edu.co
• Línea 106 (24/7)

RECUERDA:
✓ Está bien no estar bien
✓ Pedir ayuda es valentía
✓ Pequeños pasos cuentan

¿Hay algo específico en lo que te gustaría que te ayude hoy?"""