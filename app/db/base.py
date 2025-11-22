# app/db/base.py

from app.db.base_class import Base

# IMPORTA TODOS LOS MODELOS PARA QUE SQLALCHEMY LOS REGISTRE
from app.models.user import User
from app.models.emotion_entry import EmotionEntry
