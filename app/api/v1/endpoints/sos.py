from fastapi import APIRouter

router = APIRouter()

@router.get("/resources", response_model=list[dict])
def list_resources():
    return [
        {
            "nombre": "Línea Nacional de Emergencias",
            "tipo": "Teléfono",
            "contacto": "123",
            "region": "Colombia",
        },
        {
            "nombre": "Bienestar Universitario",
            "tipo": "Correo",
            "contacto": "bienestar@ucatolica.edu.co",
            "region": "Universidad",
        },
    ]
