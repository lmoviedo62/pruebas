from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    full_name: str

    identificacion: str
    nombre: str
    apellido: str
    programa: str
    semestre: int
    telefono: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # reemplaza orm_mode = True en Pydantic v2


class UserLogin(BaseModel):
    email: EmailStr
    password: str
