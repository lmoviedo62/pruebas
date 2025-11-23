from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base


class EmotionEntry(Base):
    __tablename__ = "emotion_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    emotion = Column(String(50), nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)  # ← NUEVO
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # ← NUEVO

    user = relationship("User", backref="entries")