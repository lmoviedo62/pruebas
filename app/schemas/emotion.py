from pydantic import BaseModel

class EmotionEntryBase(BaseModel):
    emotion: str
    note: str | None = None

class EmotionEntryCreate(EmotionEntryBase):
    pass

class EmotionEntryOut(EmotionEntryBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
