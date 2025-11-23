from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.services.chatbot import get_emotion_response, respond_free_text, detect_crisis, get_crisis_response, EmotionType
from app.schemas.emotion import EmotionEntryCreate, EmotionEntryOut
from app.models.emotion_entry import EmotionEntry

router = APIRouter()


@router.post("/emotion", response_model=dict)
def choose_emotion(emotion: EmotionType = Body(...)):
    """
    Endpoint para seleccionar una emoción y obtener opciones de apoyo.
    
    Body esperado:
    "muy_mal" | "triste" | "neutral" | "bien" | "muy_bien"
    """
    return get_emotion_response(emotion)


@router.post("/note", response_model=EmotionEntryOut)
def save_note(
    note_in: EmotionEntryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Guarda una nota emocional del usuario en la base de datos.
    """
    entry = EmotionEntry(
        user_id=current_user.id,
        emotion=note_in.emotion,
        note=note_in.note,
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.post("/free-text", response_model=dict)
def free_text(message: str = Body(..., embed=True)):
    """
    Endpoint para texto libre del usuario.
    Detecta crisis y responde apropiadamente.
    """
    # Detectar si es una situación de crisis
    if detect_crisis(message):
        return {"reply": get_crisis_response()}
    
    # Respuesta normal
    return {"reply": respond_free_text(message)}


@router.post("/option-detail", response_model=dict)
def get_option_detail(
    emotion: EmotionType,
    option_id: str = Body(..., embed=True)
):
    """
    Obtiene el contenido detallado de una opción específica.
    
    Ejemplo:
    POST /api/v1/chatbot/option-detail
    {
        "emotion": "muy_mal",
        "option_id": "respiracion_crisis"
    }
    """
    response = get_emotion_response(emotion)
    
    # Buscar la opción específica
    for option in response.get("opciones", []):
        if option["id"] == option_id:
            return {
                "label": option["label"],
                "contenido": option["contenido"]
            }
    
    return {"error": "Opción no encontrada"}