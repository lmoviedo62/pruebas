from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, get_db
from app.services.chatbot import (
    get_emotion_response, 
    respond_free_text, 
    detect_crisis, 
    get_crisis_response,
    get_option_content,  # ← NUEVA FUNCIÓN
    EmotionType
)
from app.schemas.emotion import EmotionEntryCreate, EmotionEntryOut
from app.models.emotion_entry import EmotionEntry

router = APIRouter()


@router.post("/emotion", response_model=dict)
def choose_emotion(
    emotion: str = Body(..., embed=True)
):
    """
    Endpoint para seleccionar una emoción y obtener opciones de apoyo.
    
    Body esperado:
    {
        "emotion": "muy_mal" | "triste" | "neutral" | "bien" | "muy_bien"
    }
    """
    valid_emotions = ["muy_mal", "triste", "neutral", "bien", "muy_bien"]
    
    if emotion not in valid_emotions:
        return {
            "error": f"Emoción inválida. Debe ser una de: {', '.join(valid_emotions)}"
        }
    
    return get_emotion_response(emotion)


@router.post("/option-detail", response_model=dict)
def get_option_detail(
    option_id: str = Body(..., embed=True)
):
    """
    Obtiene el contenido ROTATIVO de una opción específica.
    
    Cada vez que se llama con el mismo option_id, devuelve una versión diferente.
    
    Ejemplo:
    POST /api/v1/chatbot/option-detail
    {
        "option_id": "respiracion_crisis"
    }
    """
    contenido = get_option_content(option_id)
    
    if contenido == "Contenido no encontrado":
        return {"error": "Opción no encontrada"}
    
    return {
        "option_id": option_id,
        "contenido": contenido
    }


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
    if detect_crisis(message):
        return {"reply": get_crisis_response()}
    
    return {"reply": respond_free_text(message)}

# ============ ENDPOINTS DE DIARIO EMOCIONAL ============

@router.get("/diary/entries", response_model=list[EmotionEntryOut])
def get_diary_entries(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Obtiene todas las entradas del diario del usuario actual,
    ordenadas por fecha (más recientes primero)
    """
    entries = db.query(EmotionEntry).filter(
        EmotionEntry.user_id == current_user.id
    ).order_by(EmotionEntry.id.desc()).all()
    
    return entries


@router.post("/diary/entry", response_model=EmotionEntryOut)
def create_diary_entry(
    note_in: EmotionEntryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Crea una nueva entrada en el diario emocional
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


@router.put("/diary/entry/{entry_id}", response_model=EmotionEntryOut)
def update_diary_entry(
    entry_id: int,
    note_in: EmotionEntryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Actualiza una entrada del diario
    """
    entry = db.query(EmotionEntry).filter(
        EmotionEntry.id == entry_id,
        EmotionEntry.user_id == current_user.id
    ).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Entrada no encontrada")
    
    entry.emotion = note_in.emotion
    entry.note = note_in.note
    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/diary/entry/{entry_id}")
def delete_diary_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Elimina una entrada del diario
    """
    entry = db.query(EmotionEntry).filter(
        EmotionEntry.id == entry_id,
        EmotionEntry.user_id == current_user.id
    ).first()
    
    if not entry:
        raise HTTPException(status_code=404, detail="Entrada no encontrada")
    
    db.delete(entry)
    db.commit()
    return {"message": "Entrada eliminada correctamente", "id": entry_id}