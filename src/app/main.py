from fastapi import FastAPI

from src.app.routers import social_media_restaurant_router, city_router, landmark_router, accommodation_router, \
    social_media_accommodation_router, social_media_event_router


def include_routers(app: FastAPI):
    app.include_router(city_router)
    app.include_router(landmark_router)
    app.include_router(accommodation_router)
    app.include_router(social_media_accommodation_router)
    app.include_router(social_media_event_router)
    app.include_router(social_media_restaurant_router)


def create_app():
    app = FastAPI()
    include_routers(app)
    return app


app = create_app()
