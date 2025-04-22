from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.app.dto.city.city import CityResponse, CityRequest, CityUpdateRequest
from src.app.dto.city.city_without_landmark import CityWithoutLandmarkResponse
from src.app.repositories.city_repository import CityRepository
from src.app.schemas.pagination import PaginationParam
from src.app.utils.dto_utils import to_dto


class CityService:
    def __init__(self, repository: CityRepository):
        self.repository = repository

    async def create(self, data: CityRequest) -> Optional[CityWithoutLandmarkResponse]:
        try:
            created_city = await self.repository.create(data.__dict__)
            return to_dto(CityWithoutLandmarkResponse, created_city)
        except Exception as e:
            if isinstance(e, IntegrityError):
                raise HTTPException(status_code=409, detail=f"City with name {data.name} already exists.")
            raise HTTPException(status_code=422, detail="Invalid city format")

    async def get_paginated(self, pagination_param: PaginationParam):
        try:
            paginated_list = await self.repository.get_paginated(pagination_param, join=True)
            paginated_list.items = [to_dto(CityResponse, item) for item in paginated_list.items]
            return paginated_list
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_by_id(self, id: int) -> Optional[CityResponse]:
        try:
            city = await self.repository.get_by("id", id, unique=True, join=True)
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
            all_cities = await self.repository.get_all(join=True)
            all_cities_response = [to_dto(CityResponse, city) for city in all_cities]
            return all_cities_response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update(self, id: int, data: CityUpdateRequest) -> Optional[CityWithoutLandmarkResponse]:
        try:
            city_for_update = await self.repository.get_by("id", id, True)
            if not city_for_update:
                raise NoResultFound(f"City with id {id} does not exist.")
            await self.repository.update(city_for_update, data.__dict__)
            return to_dto(CityWithoutLandmarkResponse, city_for_update)
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
