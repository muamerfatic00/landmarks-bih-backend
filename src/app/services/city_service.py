from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from src.app.dto.city.city import CityPostRequest
from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.repositories.city_repository import CityRepository
from src.app.utils.dto_utils import to_dto


class CityService:
    def __init__(self, repository: CityRepository):
        self.repository = repository

    async def create(self, data: CityPostRequest) -> Optional[CityBaseResponse]:
        try:
            created_city = await self.repository.create(data.__dict__)
            return to_dto(CityBaseResponse, created_city)
        except Exception as e:
            if isinstance(e, IntegrityError):
                raise HTTPException(status_code=409, detail=f"City with name {data.name} already exists.")
            raise HTTPException(status_code=422, detail="Invalid city format")
