from typing import Literal
import random

EmotionType = Literal["muy_mal", "triste", "neutral", "bien", "muy_bien"]

# Diccionario para rastrear qué versión se mostró por última vez
last_shown_versions = {}

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


def get_next_version(option_id: str, total_versions: int = 4) -> int:
    """Obtiene la siguiente versión a mostrar de manera rotativa"""
    if option_id not in last_shown_versions:
        # Primera vez, elegir aleatoriamente
        version = random.randint(0, total_versions - 1)
    else:
        # Siguiente versión en la rotación
        version = (last_shown_versions[option_id] + 1) % total_versions
    
    last_shown_versions[option_id] = version
    return version


# ========== CONTENIDO CON 4 VARIACIONES POR OPCIÓN ==========

OPCIONES_CONTENIDO = {
    # ============ MUY MAL ============
    "respiracion_crisis": [
        # Versión 1
        """🫁 RESPIRACIÓN 4-7-8 (Calma inmediata)

1. INHALA por la nariz: 1-2-3-4
2. SOSTÉN: 1-2-3-4-5-6-7
3. EXHALA por la boca: 1-2-3-4-5-6-7-8

Repite 4 veces.

Después del 2do ciclo sentirás más calma.
Después del 4to tu corazón habrá bajado.

Hazlo AHORA. 💜""",
        
        # Versión 2
        """🫁 RESPIRACIÓN CUADRADA (Box Breathing)

Imagina dibujar un cuadrado con tu respiración:

1. INHALA 4 segundos (lado 1)
2. SOSTÉN 4 segundos (lado 2)
3. EXHALA 4 segundos (lado 3)
4. SOSTÉN 4 segundos (lado 4)

Repite 5 cuadrados completos.

Esta técnica la usan Navy SEALs en situaciones de estrés extremo.

Funciona. Inténtalo ahora. 💜""",
        
        # Versión 3
        """🫁 RESPIRACIÓN DE EMERGENCIA

Cuando el pánico te abruma:

1. EXHALA completamente (vacía los pulmones)
2. INHALA profundo por la nariz (5 seg)
3. EXHALA lento por la boca (7 seg)
4. Repite, alargando cada vez más la exhalación

META: Exhalación más larga que inhalación

Esto activa tu sistema nervioso parasimpático (calma).

3 ciclos mínimo. Ya. 💜""",
        
        # Versión 4
        """🫁 RESPIRACIÓN 5-5-5

La más simple en crisis:

INHALA: 1-2-3-4-5
EXHALA: 1-2-3-4-5
PAUSA: 1-2-3-4-5

Cuenta en voz alta si puedes, te ayuda a concentrarte.

Repite hasta sentir que tu corazón se calma.

No necesitas pensar, solo cuenta. Tu cuerpo hará el resto. 💜"""
    ],
    
    "consejo_crisis": [
        # Versión 1
        """💭 PARA TI EN ESTE MOMENTO

• Este momento es TEMPORAL
• Has sobrevivido al 100% de tus peores días
• Los pensamientos NO son hechos
• Pedir ayuda es VALENTÍA, no debilidad

Habrá días mejores. Tu futuro yo te agradece que sigas aquí.

Contacta Bienestar: bienestar@ucatolica.edu.co
O Línea 106 (24/7)

¿Qué UNA cosa puedes hacer HOY para cuidarte? 💜""",
        
        # Versión 2
        """💭 VERDADES EN LA TORMENTA

Cuando todo se siente insoportable:

✓ El dolor emocional es TAN REAL como el físico
✓ Mereces compasión, no juicio
✓ No estás siendo dramático/a
✓ Tu dolor tiene sentido en tu contexto
✓ Habrá alivio, aunque hoy no lo veas

AHORA MISMO:
¿Puedes estar seguro/a por las próximas 24 horas?

Solo 24 horas. Después reevaluamos.

Línea 106: disponible AHORA 💜""",
        
        # Versión 3
        """💭 CUANDO EL FUTURO PARECE IMPOSIBLE

No necesitas ver toda la escalera.
Solo da el siguiente paso.

SIGUIENTE PASO AHORA:
□ ¿Estás seguro/a físicamente? SÍ/NO
□ Si NO → Llamar 123
□ Si SÍ → ¿Puedes contactar a 1 persona?

No planees mañana.
No pienses en el año.

Solo este momento. Solo este paso.

¿Quién puede acompañarte HOY? 💜""",
        
        # Versión 4
        """💭 CARTA A TI MISMO/A

Lee esto en voz alta:

"Sé que duele. Sé que estás cansado/a.
Pero también sé que eres más fuerte de lo que crees.
Has llegado hasta aquí.
Eso cuenta. Eso importa.

No necesito 'mejorar' hoy.
Solo necesito SOBREVIVIR hoy.
Y puedo hacer eso.

Mañana será diferente.
Siempre lo es."

Guarda esto. Léelo cuando lo necesites.

Bienestar: bienestar@ucatolica.edu.co 💜"""
    ],
    
    "grounding_crisis": [
        # Versión 1
        """⚓ TÉCNICA 5-4-3-2-1 (Volver al presente)

Nombra en voz alta:

5 cosas que VES
4 cosas que TOCAS
3 cosas que OYES
2 cosas que HUELES
1 cosa que SABOREAS

Esto te ancla al momento presente y detiene pensamientos negativos.

¿Cómo te sientes ahora? ⚓""",
        
        # Versión 2
        """⚓ GROUNDING FÍSICO

Tu cuerpo te trae al presente:

1. Presiona tus pies contra el suelo (30 seg)
2. Toca algo frío (hielo, agua fría)
3. Estira los brazos al techo
4. Aprieta los puños 10 veces
5. Mueve los hombros en círculos

Siente tu peso. Sientes tu solidez.

No eres tus pensamientos.
Eres este cuerpo, aquí, ahora. ⚓""",
        
        # Versión 3
        """⚓ DESCRIPCIÓN DETALLADA

Elige un objeto frente a ti.

Descríbelo en VOZ ALTA durante 2 minutos:

• Color exacto
• Textura
• Tamaño
• Para qué sirve
• Qué sientes al tocarlo
• Qué recuerdos te trae

Hablar en voz alta saca los pensamientos de la mente.

Tu cerebro no puede entrar en pánico y describir al mismo tiempo. ⚓""",
        
        # Versión 4
        """⚓ GROUNDING DE AGUA

El agua calma el sistema nervioso:

Opción 1: Lava tus manos con agua fría
- Siente la temperatura
- Escucha el sonido
- Huele el jabón
- Cuenta 60 segundos

Opción 2: Bebe agua lentamente
- Siente cómo baja por tu garganta
- Nota la temperatura
- Haz 10 tragos conscientes

El presente es este agua, este momento. ⚓"""
    ],
    
    "recursos_crisis": [
        # Versión 1
        """🆘 RECURSOS AHORA

📞 Línea 106 - 24/7, gratuita, confidencial
📞 Línea 123 - Emergencias
📧 bienestar@ucatolica.edu.co - Atención psicológica
📞 Línea 155 - Salud Mental

¿Qué decir? "Estoy pasando por un momento muy difícil y necesito hablar."

NO tienes que enfrentarlo solo/a. 💜""",
        
        # Versión 2
        """🆘 A QUIÉN LLAMAR AHORA

URGENCIA INMEDIATA:
📞 123 - Si hay peligro físico
📞 106 - Crisis emocional (24/7)

SOPORTE UNIVERSITARIO:
📧 bienestar@ucatolica.edu.co
🏥 Enfermería campus (horario laboral)

¿MIEDO DE LLAMAR?
Es normal. Hazlo igual.
Están entrenados para ayudar.
Miles lo han hecho antes que tú.

Marca ahora. 💜""",
        
        # Versión 3
        """🆘 PLAN DE SEGURIDAD INMEDIATA

1. ¿Estás en peligro AHORA? → 123
2. ¿Pensamientos suicidas? → 106
3. ¿Crisis emocional fuerte? → bienestar@ucatolica.edu.co

SI NO QUIERES LLAMAR:
- Envía WhatsApp a un amigo/familiar
- Ve a un lugar público (no estés solo/a)
- Llama a cualquier persona de confianza

REGLA: No estar solo/a en las próximas horas.

¿Puedes comprometerte a eso? 💜""",
        
        # Versión 4
        """🆘 RED DE APOYO EXTENDIDA

MÁS ALLÁ DE LAS LÍNEAS:

👥 APOYO ENTRE PARES:
- Grupos de apoyo estudiantiles
- Comunidades en línea (moderadas)
- Apps: Calm Harm, StayAlive

📱 APPS ÚTILES:
- "Mi Plan de Seguridad"
- "Virtual Hope Box"
- "MindShift"

🆘 SIEMPRE DISPONIBLE:
106, 123, bienestar@ucatolica.edu.co

Hay más ayuda de la que crees.
No te rindas antes de buscarla. 💜"""
    ],
    
    # ============ TRISTE ============
    "meditacion_tristeza": [
        """🧘 MEDITACIÓN DE ACEPTACIÓN

1. Siéntate cómodo, cierra los ojos
2. Respira naturalmente 2 minutos
3. Nota DÓNDE sientes la tristeza (pecho, garganta, estómago)
4. Respira HACIA esa sensación. No la cambies, solo acompáñala
5. Repite: "Está bien sentir esto. Soy humano/a. Esto pasará"
6. Coloca una mano en tu corazón. Siente su calor
7. Abre los ojos gradualmente

La tristeza es como una ola. Si luchas, te arrastra. Si observas, pasa sobre ti. 💙""",
        
        """🧘 MEDITACIÓN DEL RÍO

Cierra los ojos. Imagina:

Estás junto a un río.
Cada pensamiento triste es una hoja flotando.

NO intentes detener las hojas.
NO te metas al río.
Solo OBSERVA cómo pasan.

"Ahí va un pensamiento sobre..."
"Ahí va un sentimiento de..."

Las hojas siguen su curso.
Tú permaneces en la orilla.

5 minutos. Solo observa. 💙""",
        
        """🧘 ESCANEO CORPORAL CON TRISTEZA

Acuéstate o siéntate cómodo.

Recorre mentalmente tu cuerpo:

PIES: ¿Hay tensión? Respira hacia ellos
PIERNAS: ¿Pesan? Obsérvalas
ESTÓMAGO: ¿Está apretado? Afloja
PECHO: ¿Está oprimido? Dale espacio
GARGANTA: ¿Hay nudo? Tráelo con suavidad
CARA: ¿Ceño fruncido? Relaja

No cambies nada. Solo nota y respira.

El cuerpo guarda la tristeza. Escúchalo. 💙""",
        
        """🧘 RESPIRACIÓN CON COLOR

Cierra los ojos. Visualiza:

INHALA: Luz dorada entra (5 seg)
EXHALA: Gris/negro sale (7 seg)

La luz dorada = calma, calidez, aceptación
El gris/negro = tristeza, pesadez saliendo

No fuerzas nada.
Solo permites el intercambio.

10 respiraciones.

Cada exhalación se lleva un poco de peso. 💙"""
    ],
    
    "consejo_tristeza": [
        """💬 PARA TU TRISTEZA

Está bien no estar bien. Permitirte sentir es honestidad, no debilidad.

Esto NO durará para siempre. Las emociones son temporales.

Eres más fuerte de lo que crees. Estás AQUÍ, buscando ayuda.

PERMISO PARA:
✅ Llorar cuando lo necesites
✅ Pedir apoyo sin culpa
✅ Tomarte tu tiempo
✅ Priorizarte

¿Qué UNA cosa necesita tu cuerpo/mente ahora? (descanso, comida, movimiento, conexión)

Bienestar: bienestar@ucatolica.edu.co 💙""",
        
        """💬 VALIDACIÓN DE TU TRISTEZA

Tu tristeza NO significa que:
✗ Seas débil
✗ Estés exagerando
✗ Debas "superarlo ya"
✗ Seas una carga

Tu tristeza SÍ significa que:
✓ Algo importante para ti se vio afectado
✓ Eres humano con emociones reales
✓ Tienes capacidad de sentir profundamente
✓ Necesitas y mereces apoyo

Sentir tristeza ≠ Ser un problema

¿Qué necesitas hoy? (No lo que "deberías", sino lo que realmente necesitas) 💙""",
        
        """💬 CUANDO LA TRISTEZA PESA

Metáfora útil:

La tristeza es como cargar una mochila pesada.
No puedes simplemente "dejarla".
Pero SÍ puedes:

1. Reconocer que pesa
2. Tomar descansos
3. Pedir ayuda para llevarla
4. Sacar cosas innecesarias (autocrítica, culpa)
5. Avanzar a tu propio ritmo

No necesitas correr con la mochila puesta.
Caminar lento también te lleva adelante.

¿Qué hay en tu mochila que NO es tuyo cargar? 💙""",
        
        """💬 TRISTEZA CON PROPÓSITO

Tu tristeza tiene un mensaje:

Pregúntale:
"¿Qué intentas decirme?"
"¿Qué necesito atender?"
"¿Qué he estado ignorando?"

A veces la tristeza es:
• Duelo por algo perdido
• Agotamiento acumulado
• Necesidad de cambio
• Señal de que algo importa

Escucha sin juzgar.
Tu tristeza no es enemiga.
Es mensajera.

¿Qué crees que intenta decirte? 💙"""
    ],
    
    # Continúa con las demás opciones...
    # Por brevedad, te muestro el patrón. Cada opción tiene 4 versiones
}

def get_option_content(option_id: str) -> str:
    """Obtiene el contenido rotativo de una opción"""
    if option_id not in OPCIONES_CONTENIDO:
        return "Contenido no encontrado"
    
    versions = OPCIONES_CONTENIDO[option_id]
    version_index = get_next_version(option_id, len(versions))
    return versions[version_index]


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
                {"id": "respiracion_crisis", "label": "🫁 Ejercicio de respiración urgente", "contenido": ""},
                {"id": "consejo_crisis", "label": "💭 Mensaje de esperanza", "contenido": ""},
                {"id": "grounding_crisis", "label": "⚓ Técnica de grounding", "contenido": ""},
                {"id": "recursos_crisis", "label": "🆘 Contactos de ayuda inmediata", "contenido": ""}
            ]
        },
        
        "triste": {
            "mensaje": """💙 Entiendo tu tristeza. Es una emoción válida que nos conecta con lo que valoramos.

A veces los pensamientos se vuelven más negativos de lo necesario. Trabajemos juntos.

¿Qué necesitas?""",
            
            "opciones": [
                {"id": "meditacion_tristeza", "label": "🧘 Meditación de aceptación", "contenido": ""},
                {"id": "consejo_tristeza", "label": "💬 Mensaje de apoyo emocional", "contenido": ""},
                {"id": "activacion_tristeza", "label": "⚡ Ideas para activarme", "contenido": ""},
                {"id": "recurso_tristeza", "label": "📚 Entender la tristeza", "contenido": ""}
            ]
        },
        
        # ... resto de emociones
    }
    
    return responses.get(emotion, {"mensaje": "Emoción no reconocida", "opciones": []})


def respond_free_text(text: str) -> str:
    """Respuesta a texto libre con detección de crisis"""
    
    if detect_crisis(text):
        return get_crisis_response()
    
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