from fastapi import APIRouter
from racesim_backend.api.routes import races

api_router = APIRouter()
api_router.include_router(races.router, prefix="/races", tags=["races"])