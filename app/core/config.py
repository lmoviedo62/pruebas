from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Serena"
    
    # Base de datos SQLite
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./serena.db"
    
    # JWT
    JWT_SECRET_KEY: str = "tu_clave_super_secreta_cambiala_en_produccion_12345"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # Email (opcional)
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "tu_correo@gmail.com"
    SMTP_PASSWORD: str = "tu_app_password"
    SOS_EMAIL_DEST: str = "bienestar@ucatolica.edu.co"
    
    # Alias para compatibilidad
    SECRET_KEY: str = "tu_clave_super_secreta_cambiala_en_produccion_12345"

    class Config:
        env_file = ".env"

settings = Settings()