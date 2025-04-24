from fastapi import FastAPI

from src.app.routers.accommodation_router import accommodation_router
from src.app.routers.city_router import city_router
from src.app.routers.landmark_router import landmark_router


def include_routers(app: FastAPI):
    app.include_router(city_router)
    app.include_router(landmark_router)
    app.include_router(accommodation_router)


def create_app():
    app = FastAPI()
    include_routers(app)
    return app


app = create_app()
