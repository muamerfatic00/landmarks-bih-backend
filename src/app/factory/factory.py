from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.database.database import get_db
from src.app.repositories.city_repository import CityRepository
from src.app.services.city_service import CityService
from src.app.models.city import City

def get_city_repository(session: AsyncSession = Depends(get_db)) -> CityRepository:
    return CityRepository(City,session)

def get_city_service(repository: CityRepository = Depends(get_city_repository)) -> CityService:
    return CityService(repository)