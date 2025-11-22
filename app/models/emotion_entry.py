from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class EmotionEntry(Base):
    __tablename__ = "emotion_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    emotion = Column(String(50), nullable=False)
    note = Column(Text, nullable=True)

    user = relationship("User", backref="entries")
