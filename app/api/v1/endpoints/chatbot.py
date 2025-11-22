from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.services.chatbot import get_emotion_options, respond_free_text, EmotionType
from app.schemas.emotion import EmotionEntryCreate, EmotionEntryOut
from app.models.emotion_entry import EmotionEntry
from app.api.deps import get_db

router = APIRouter()

@router.post("/emotion", response_model=dict)
def choose_emotion(emotion: EmotionType):
    return get_emotion_options(emotion)

@router.post("/note", response_model=EmotionEntryOut)
def save_note(
    note_in: EmotionEntryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
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
def free_text(message: str):
    return {"reply": respond_free_text(message)}
