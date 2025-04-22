from typing import TypeVar, Type

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database.database import get_db, Base
from src.app.models import Landmark
from src.app.models.city import City
from src.app.repositories.base_repository import BaseRepository
from src.app.repositories.city_repository import CityRepository
from src.app.repositories.landmark_repository import LandmarkRepository
from src.app.services.base_service import BaseService
from src.app.services.city_service import CityService
from src.app.services.landmark_service import LandmarkService

ModelType = TypeVar('ModelType', bound=Base)


def get_base_repository(model_class: Type[ModelType]):
    def _get_repository(session: AsyncSession = Depends(get_db)) -> BaseRepository:
        return BaseRepository(model_class, session)

    return _get_repository


def get_base_service(model_class: Type[ModelType]):
    def _get_service(repository: BaseRepository = Depends(get_base_repository(model_class))) -> BaseService:
        return BaseService(repository)

    return _get_service


def get_city_repository(session: AsyncSession = Depends(get_db)) -> CityRepository:
    return CityRepository(City, session)


def get_city_service(repository: CityRepository = Depends(get_city_repository)) -> CityService:
    return CityService(repository)


def get_landmark_repository(session: AsyncSession = Depends(get_db)) -> LandmarkRepository:
    return LandmarkRepository(Landmark, session)


def get_landmark_service(repository: LandmarkRepository = Depends(get_landmark_repository)) -> LandmarkService:
    return LandmarkService(repository)
