from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database.database import get_db
from src.app.models import Landmark
from src.app.models.city import City
from src.app.repositories.city_repository import CityRepository
from src.app.repositories.landmark_repository import LandmarkRepository
from src.app.services.city_service import CityService
from src.app.services.landmark_service import LandmarkService


def get_city_repository(session: AsyncSession = Depends(get_db)) -> CityRepository:
    return CityRepository(City, session)


def get_city_service(repository: CityRepository = Depends(get_city_repository)) -> CityService:
    return CityService(repository)


def get_landmark_repository(session: AsyncSession = Depends(get_db)) -> LandmarkRepository:
    return LandmarkRepository(Landmark, session)


def get_landmark_service(repository: LandmarkRepository = Depends(get_landmark_repository)) -> LandmarkService:
    return LandmarkService(repository)
