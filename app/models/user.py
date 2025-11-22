from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"   # 🔥 ESTA LÍNEA ES OBLIGATORIA

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)

    identificacion = Column(String(50), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    programa = Column(String(150), nullable=False)
    semestre = Column(Integer, nullable=False)
    telefono = Column(String(20), nullable=False)

    is_active = Column(Boolean, default=True)
