from pydantic_settings import BaseSettings  # 👈 CAMBIO IMPORTANTE

class Settings(BaseSettings):
    PROJECT_NAME: str = "Serena"

    # URL de la base de datos (usando SQLite local)
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./serena.db"

    class Config:
        env_file = ".env"

settings = Settings()
