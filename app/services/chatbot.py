from typing import Literal

EmotionType = Literal["muy_mal", "triste", "neutral", "bien", "muy_bien"]

def get_emotion_options(emotion: EmotionType) -> dict:
    """
    Respuestas empáticas basadas en principios de psicología cognitivo-conductual.
    Valida las emociones del usuario y ofrece apoyo personalizado.
    """
    
    responses = {
        "muy_mal": {
            "mensaje": (
                "Lamento mucho que te sientas así en este momento. Lo que estás experimentando "
                "es válido y tiene sentido. Cuando nos sentimos muy mal, nuestro cuerpo y mente "
                "nos están enviando una señal importante de que algo necesita atención.\n\n"
                "Quiero que sepas que no estás solo/a en esto. Muchas personas atraviesan momentos "
                "difíciles, y buscar apoyo es un acto de valentía y autocuidado. Tu bienestar "
                "es importante y mereces sentirte mejor.\n\n"
                "Antes de continuar, quiero preguntarte: ¿Te sientes en peligro inmediato o has "
                "pensado en hacerte daño? Si es así, es fundamental que contactes de inmediato con "
                "Bienestar Universitario (bienestar@ucatolica.edu.co) o la Línea 106 (disponible 24/7)."
            ),
            "opciones": [
                {
                    "type": "respiracion",
                    "label": "Quiero un ejercicio de respiración para calmarme ahora",
                    "descripcion": "Te guiaré en una técnica de respiración que ayuda a regular el sistema nervioso"
                },
                {
                    "type": "validacion",
                    "label": "Necesito hablar sobre lo que siento",
                    "descripcion": "Creemos un espacio seguro para explorar tus emociones"
                },
                {
                    "type": "recursos_urgente",
                    "label": "Necesito ayuda profesional urgente",
                    "descripcion": "Te conectaré con recursos de apoyo inmediato"
                },
                {
                    "type": "pensamiento_util",
                    "label": "Ayúdame a ordenar mis pensamientos",
                    "descripcion": "Trabajemos juntos para identificar y modificar pensamientos que generan malestar"
                }
            ]
        },
        
        "triste": {
            "mensaje": (
                "Entiendo que estás pasando por un momento de tristeza. La tristeza es una emoción "
                "humana completamente natural y válida; nos conecta con lo que valoramos y nos "
                "muestra qué es importante para nosotros.\n\n"
                "A veces, cuando estamos tristes, nuestros pensamientos pueden volverse más negativos "
                "de lo que la realidad merece. Es como si lleváramos puestos unos 'lentes oscuros' "
                "que filtran nuestra percepción. Parte de mi trabajo es ayudarte a reconocer estos "
                "patrones y encontrar una perspectiva más equilibrada.\n\n"
                "Recuerda: sentir tristeza no significa debilidad. Significa que eres humano/a y que "
                "tu experiencia emocional es rica y compleja. Estoy aquí para acompañarte."
            ),
            "opciones": [
                {
                    "type": "exploracion",
                    "label": "Quiero explorar de dónde viene esta tristeza",
                    "descripcion": "Identifiquemos juntos qué situaciones o pensamientos están influyendo en tu estado"
                },
                {
                    "type": "activacion",
                    "label": "Dame ideas para activarme y sentirme mejor",
                    "descripcion": "La activación conductual puede ayudarte a romper el ciclo de la tristeza"
                },
                {
                    "type": "meditacion",
                    "label": "Quiero una meditación para aceptar esta emoción",
                    "descripcion": "Practicaremos mindfulness para observar tu tristeza sin juzgarla"
                },
                {
                    "type": "reestructuracion",
                    "label": "Ayúdame a ver las cosas desde otra perspectiva",
                    "descripcion": "Trabajaremos en identificar y cuestionar pensamientos negativos automáticos"
                }
            ]
        },
        
        "neutral": {
            "mensaje": (
                "Gracias por compartir cómo te sientes. Estar en un estado neutral también es "
                "válido y puede ser un buen momento para reflexionar y fortalecerte emocionalmente.\n\n"
                "A veces, la neutralidad puede significar calma y estabilidad, otras veces puede "
                "ser señal de desconexión emocional o de estar 'en pausa'. Ambas son experiencias "
                "comunes y está bien sentirse así.\n\n"
                "Este puede ser un momento ideal para desarrollar herramientas de autocuidado, "
                "explorar tus patrones de pensamiento, o simplemente practicar habilidades que te "
                "preparen para cuando vengan momentos más desafiantes. La prevención y el desarrollo "
                "personal son tan importantes como trabajar en crisis."
            ),
            "opciones": [
                {
                    "type": "autoconocimiento",
                    "label": "Quiero conocerme mejor emocionalmente",
                    "descripcion": "Exploremos tus patrones emocionales y cómo respondes a diferentes situaciones"
                },
                {
                    "type": "herramientas",
                    "label": "Enséñame herramientas para el futuro",
                    "descripcion": "Desarrollemos estrategias de afrontamiento para cuando las necesites"
                },
                {
                    "type": "mindfulness",
                    "label": "Quiero practicar presencia plena",
                    "descripcion": "La atención plena te ayuda a conectar con el momento presente"
                },
                {
                    "type": "metas",
                    "label": "Ayúdame a establecer metas de bienestar",
                    "descripcion": "Identifiquemos objetivos concretos para tu desarrollo emocional"
                }
            ]
        },
        
        "bien": {
            "mensaje": (
                "¡Me alegra mucho saber que te sientes bien! Es importante reconocer y celebrar "
                "estos momentos positivos. A veces, cuando las cosas van bien, tendemos a no "
                "prestarles atención, pero son igual de valiosos que los momentos difíciles.\n\n"
                "Sentirse bien no es casualidad: generalmente es el resultado de pensamientos más "
                "equilibrados, acciones constructivas y un buen manejo de tus emociones. Es valioso "
                "que identifiques qué está funcionando para ti en este momento.\n\n"
                "Este es un excelente momento para fortalecer tus recursos emocionales y desarrollar "
                "habilidades que puedas usar cuando enfrentes desafíos futuros. La resiliencia se "
                "construye tanto en los buenos momentos como en los difíciles."
            ),
            "opciones": [
                {
                    "type": "consolidacion",
                    "label": "Quiero identificar qué me hace sentir bien",
                    "descripcion": "Reconozcamos tus fortalezas y recursos personales"
                },
                {
                    "type": "gratitud",
                    "label": "Practicar gratitud y valorar lo positivo",
                    "descripcion": "La gratitud fortalece el bienestar emocional a largo plazo"
                },
                {
                    "type": "prevencion",
                    "label": "Prepararme para futuros desafíos",
                    "descripcion": "Desarrollemos un plan de acción para mantener tu bienestar"
                },
                {
                    "type": "compartir",
                    "label": "Reflexionar sobre mi progreso personal",
                    "descripcion": "Celebremos tus logros y aprendizajes recientes"
                }
            ]
        },
        
        "muy_bien": {
            "mensaje": (
                "¡Qué maravilloso que te sientas muy bien en este momento! Tu estado emocional "
                "positivo es un reflejo de que muchas cosas están funcionando correctamente en tu "
                "vida: tus pensamientos son más equilibrados, tus acciones te están acercando a tus "
                "valores, y tu bienestar está en un buen lugar.\n\n"
                "Es fundamental que reconozcas este estado y valores lo que has hecho para llegar "
                "aquí. Cada momento de bienestar es una evidencia de tu capacidad de cuidarte y de "
                "construir una vida significativa.\n\n"
                "Este es el momento perfecto para consolidar tus fortalezas, agradecer tu esfuerzo, "
                "y prepararte emocionalmente para el futuro. El bienestar sostenible no es estar "
                "siempre feliz, sino tener las herramientas para navegar todas las emociones con "
                "sabiduría y compasión hacia ti mismo/a."
            ),
            "opciones": [
                {
                    "type": "celebracion",
                    "label": "Quiero celebrar y reconocer mis logros",
                    "descripcion": "Valoremos conscientemente tu progreso y tus fortalezas"
                },
                {
                    "type": "profundizacion",
                    "label": "Explorar qué factores contribuyen a mi bienestar",
                    "descripcion": "Identifiquemos los elementos clave de tu felicidad para mantenerlos"
                },
                {
                    "type": "ayudar_otros",
                    "label": "Usar mi bienestar para ayudar a otros",
                    "descripcion": "Cuando estamos bien, podemos ser fuente de apoyo para quienes nos rodean"
                },
                {
                    "type": "plan_mantenimiento",
                    "label": "Crear un plan para mantener este bienestar",
                    "descripcion": "Desarrollemos estrategias concretas para preservar tu estado positivo"
                }
            ]
        }
    }
    
    return responses[emotion]


def respond_free_text(text: str) -> str:
    """
    Respuesta empática y profesional a texto libre del usuario.
    Basada en validación emocional y principios de terapia cognitivo-conductual.
    """
    
    # Detectar palabras clave de crisis
    crisis_keywords = [
        "suicidio", "matarme", "morir", "acabar", "terminar todo",
        "no quiero vivir", "mejor muerto", "hacerme daño"
    ]
    
    text_lower = text.lower()
    is_crisis = any(keyword in text_lower for keyword in crisis_keywords)
    
    if is_crisis:
        return (
            "🆘 **ESTO ES IMPORTANTE**\n\n"
            "Lamento mucho que estés pasando por tanto dolor en este momento. Lo que sientes "
            "es real y entiendo que debe ser abrumador.\n\n"
            "**Por favor, busca ayuda profesional AHORA:**\n"
            "• 📞 Línea 106 - Línea de la vida (24/7, gratuita)\n"
            "• 📧 bienestar@ucatolica.edu.co - Bienestar Universitario\n"
            "• 🚨 123 - Línea de emergencias\n\n"
            "No estás solo/a. Hay personas capacitadas esperando ayudarte en este momento. "
            "Tu vida tiene valor y mereces recibir el apoyo adecuado.\n\n"
            "Si estás en peligro inmediato, dirígete al servicio de urgencias más cercano o "
            "llama al 123."
        )
    
    # Detectar emociones en el texto
    emotional_words = {
        "ansiedad": ["ansiedad", "ansioso", "ansiosa", "nervioso", "nerviosa", "pánico", "preocupado"],
        "tristeza": ["triste", "deprimido", "deprimida", "solo", "sola", "vacío", "desesperado"],
        "enojo": ["enojado", "enojada", "furioso", "furiosa", "molesto", "molesta", "frustrado"],
        "miedo": ["miedo", "temor", "asustado", "asustada", "terror", "pánico"],
        "soledad": ["solo", "sola", "abandonado", "abandonada", "aislado", "aislada"]
    }
    
    detected_emotion = None
    for emotion, keywords in emotional_words.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_emotion = emotion
            break
    
    # Respuestas empáticas personalizadas
    if detected_emotion == "ansiedad":
        return (
            "Noto en tus palabras que estás experimentando ansiedad, y quiero que sepas que "
            "entiendo lo difícil que puede ser. La ansiedad es una respuesta natural de tu cuerpo "
            "ante situaciones que percibe como amenazantes, pero a veces puede activarse incluso "
            "cuando no hay peligro real.\n\n"
            "**Lo que podemos hacer juntos:**\n"
            "1. **Ahora mismo**: Practica respiración diafragmática (inhala 4 segundos, sostén 4, "
            "exhala 6). Esto activa tu sistema nervioso parasimpático y te ayuda a calmarte.\n\n"
            "2. **Identificar pensamientos**: ¿Qué pensamientos están alimentando tu ansiedad? "
            "A menudo son predicciones catastróficas del futuro. Escribirlos puede ayudarte a verlos "
            "con más claridad.\n\n"
            "3. **Anclar al presente**: Nombra 5 cosas que ves, 4 que tocas, 3 que oyes, 2 que hueles "
            "y 1 que saboreas. Esto te devuelve al aquí y ahora.\n\n"
            "Recuerda: La ansiedad es incómoda pero no peligrosa. Puedes sentir ansiedad y aún así "
            "estar seguro/a. ¿Te gustaría que profundicemos en alguna de estas estrategias?"
        )
    
    elif detected_emotion == "tristeza":
        return (
            "Gracias por confiar en mí y compartir tu tristeza. Puedo sentir en tus palabras que "
            "estás atravesando un momento difícil, y quiero validar esa experiencia: tu tristeza "
            "es real, es válida, y tiene sentido.\n\n"
            "La tristeza nos enseña sobre nuestros valores y sobre lo que es importante para nosotros. "
            "Aunque duela, también es una señal de tu humanidad y de tu capacidad para conectar "
            "profundamente con la vida.\n\n"
            "**Algunas reflexiones que pueden ayudarte:**\n"
            "• Los sentimientos, incluso los dolorosos, son temporales. Lo que sientes hoy no "
            "es lo que sentirás siempre.\n"
            "• La tristeza no significa que algo esté 'mal' contigo. Eres una persona completa "
            "que está viviendo una experiencia humana difícil.\n"
            "• Pequeñas acciones pueden ayudar: dar un paseo, hablar con alguien de confianza, "
            "escuchar música, escribir tus sentimientos.\n\n"
            "¿Te gustaría hablar sobre qué situación o pensamiento está contribuyendo a tu tristeza? "
            "A veces, ponerlo en palabras ayuda a procesarlo mejor."
        )
    
    elif detected_emotion == "soledad":
        return (
            "Siento que estás experimentando soledad en este momento, y quiero que sepas que "
            "tu sentimiento es completamente comprensible. La soledad puede ser una de las experiencias "
            "más dolorosas, porque como seres humanos estamos diseñados para la conexión.\n\n"
            "Es importante distinguir entre estar físicamente solo/a y sentirse solo/a emocionalmente. "
            "A veces podemos estar rodeados de gente y aún sentirnos solos si no tenemos conexiones "
            "auténticas y significativas.\n\n"
            "**Lo que es importante recordar:**\n"
            "• La soledad es una señal, no una sentencia. Te está diciendo que necesitas conexión, "
            "y eso es información valiosa.\n"
            "• Estás dando un paso importante al comunicarte aquí. Buscar ayuda es ya una forma "
            "de romper el aislamiento.\n"
            "• Hay recursos disponibles: Bienestar Universitario ofrece grupos de apoyo donde "
            "puedes conectar con otros estudiantes que comparten experiencias similares.\n\n"
            "¿Te gustaría explorar maneras concretas de construir conexiones más profundas, o "
            "preferirías hablar más sobre lo que estás sintiendo?"
        )
    
    # Respuesta general empática
    return (
        "Gracias por confiar en mí y compartir lo que estás sintiendo. He leído tus palabras "
        "con atención y quiero que sepas que lo que experimentas es importante y merece ser escuchado.\n\n"
        "En la terapia cognitivo-conductual, creemos que hay una relación profunda entre lo que "
        "pensamos, lo que sentimos y cómo actuamos. A veces, nuestros pensamientos automáticos "
        "pueden intensificar nuestras emociones de maneras que no nos ayudan.\n\n"
        "**Algunas preguntas para reflexionar:**\n"
        "• ¿Qué pensamientos han estado pasando por tu mente últimamente?\n"
        "• ¿Hay alguna situación específica que haya desencadenado cómo te sientes?\n"
        "• ¿Qué necesitarías en este momento para sentirte un poco mejor o más apoyado/a?\n\n"
        "Recuerda que:\n"
        "✓ Tus emociones son válidas, sin importar cuáles sean\n"
        "✓ No tienes que enfrentar esto solo/a - hay recursos y personas que quieren ayudarte\n"
        "✓ Pequeños pasos cuentan: cada momento de autocuidado es valioso\n"
        "✓ Está bien no estar bien todo el tiempo\n\n"
        "Si sientes que necesitas apoyo más profundo, te animo a contactar con Bienestar "
        "Universitario (bienestar@ucatolica.edu.co). Ellos pueden ofrecerte acompañamiento "
        "psicológico profesional personalizado.\n\n"
        "Estoy aquí para escucharte. ¿Hay algo específico en lo que te gustaría que te ayudara hoy?"
    )