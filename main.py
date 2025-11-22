from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import engine
from app.db.base_class import Base
from app.db import base


Base.metadata.create_all(bind=engine)

# IMPORTANTE: para la BD
from app.db.session import engine
from app.db.base_class import Base      # Base sin importar modelos aquí             # AQUI se importan los modelos sin causar circular import


app = FastAPI(title="Serena")

# 👇 Esto crea TODAS las tablas definidas en tus modelos (incluida users)
Base.metadata.create_all(bind=engine)

# ----------- MIDDLEWARE CORS --------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # para pruebas está bien así
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- ESTÁTICOS Y TEMPLATES --------
# OJO: ajusta la ruta si tus carpetas están dentro de app/frontend/*
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

# ----------- PÁGINAS HTML --------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/panel", response_class=HTMLResponse)
async def panel_page(request: Request):
    return templates.TemplateResponse("panel.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})

@app.get("/sos", response_class=HTMLResponse)
async def sos_page(request: Request):
    return templates.TemplateResponse("sos.html", {"request": request})

@app.get("/politica-privacidad", response_class=HTMLResponse)
async def politicas_page(request: Request):
    return templates.TemplateResponse("politicas.html", {"request": request})

# ----------- API REST -------------------

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
