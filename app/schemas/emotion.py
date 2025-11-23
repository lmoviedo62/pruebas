from pydantic import BaseModel
from datetime import datetime

class EmotionEntryBase(BaseModel):
    emotion: str
    note: str | None = None

class EmotionEntryCreate(EmotionEntryBase):
    pass

class EmotionEntryOut(EmotionEntryBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True