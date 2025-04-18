from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.app.dto.city import CityResponse, CityRequest
from src.app.models import City
from src.app.repositories.city_repository import CityRepository
from src.app.utils.dto_utils import to_dto


class CityService:
    def __init__(self, repository: CityRepository):
        self.repository = repository

    async def create(self, data: CityRequest) -> Optional[City]:
        try:
            return await self.repository.create(data.__dict__)
        except Exception as e:
            if isinstance(e, IntegrityError):
                raise HTTPException(status_code=409, detail=f"City with name {data.name} already exists.")
            raise HTTPException(status_code=422, detail="Invalid city format")

    async def get_by_id(self, id: int) -> Optional[CityResponse]:
        try:
            city = await self.repository.get_by("id", id, True)
            if not city:
                raise NoResultFound(f"City with id {id} does not exist.")
            city_response = to_dto(CityResponse, city)
            return city_response
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))

    async def get_all(self) -> list[CityResponse]:
        try:
            all_cities = await self.repository.get_all()
            if not all_cities:
                raise NoResultFound("No city exists.")
            all_cities_response = [to_dto(CityResponse, city) for city in all_cities]
            return all_cities_response
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))

    async def delete(self, id: int) -> None:
        try:
            city_for_delete = await self.repository.get_by("id", id, True)
            if not city_for_delete:
                raise NoResultFound(f"City with id {id} does not exist.")
            await self.repository.delete(city_for_delete)
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))
