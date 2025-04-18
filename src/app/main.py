from fastapi import FastAPI

from src.app.routers.city_router import city_router


def include_routers(app: FastAPI):
 app.include_router(city_router)


def create_app():
 app=FastAPI()
 include_routers(app)
 return app
app=create_app()