from fastapi import APIRouter

from .endpoints import auth, users, chatbot, sos

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])
api_router.include_router(sos.router, prefix="/sos", tags=["sos"])
