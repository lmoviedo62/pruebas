from typing import Literal

EmotionType = Literal["muy_mal", "triste", "neutral", "bien", "muy_bien"]

def get_emotion_options(emotion: EmotionType) -> dict:
    base = {
        "muy_mal": "Siento que te encuentras en un momento muy difícil.",
        "triste": "Veo que estás pasando por una situación triste.",
        "neutral": "Gracias por compartir cómo te sientes.",
        "bien": "Me alegra que te sientas relativamente bien.",
        "muy_bien": "¡Qué bueno que te sientas muy bien hoy!",
    }[emotion]

    options = [
        {"type": "consejo", "label": "Quiero un consejo"},
        {"type": "meditacion", "label": "Quiero una meditación guiada"},
        {"type": "respiracion", "label": "Quiero un ejercicio de respiración"},
    ]

    return {"mensaje": base, "opciones": options}

def respond_free_text(text: str) -> str:
    # Respuesta muy sencilla, modo "psicólogo académico"
    return (
        "Gracias por confiar en Serena y compartir lo que sientes. "
        "Recuerda que tus emociones son válidas. "
        "Te recomiendo hacer una pausa, identificar qué necesitas en este momento "
        "y, si lo consideras necesario, hablar con Bienestar Universitario."
    )
