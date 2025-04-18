from operator import iconcat
from typing import Optional

from fastapi import HTTPException
from icecream import ic
from sqlalchemy.exc import IntegrityError

from src.app.dto.city import CityResponse, CityRequest
from src.app.models import City
from src.app.repositories.city_repository import CityRepository
from src.app.utils.dto_utils import to_dto


class CityService:
    def __init__(self, repository: CityRepository):
        self.repository = repository

    async def create(self, data: CityRequest) -> Optional[City]:
        try:
            ret= await self.repository.create(data.__dict__)
            ic(ret)
            return ret
            # city = await self.repository.create(data.__dict__)
        # ic(city)
        # city_response = to_dto(CityResponse, city)
        # ic(city_response)
        # return city_response

        except Exception as e:
            if isinstance(e,IntegrityError):
                raise HTTPException(status_code=409, detail=f"City with name {data.name} already exists.")
            raise HTTPException(status_code=422, detail="Invalid city format")

    async def get_by_id(self, id: int) -> Optional[CityResponse]:
        try:
            print('idem')
            city = await self.repository.get_by("id", id, True)
            if not city:
                print('heres')
                print(city)
                raise HTTPException(status_code=404, detail="City not found")
            city_response = to_dto(CityResponse, city)
            print('+')
            print(city_response)
            return city_response
        except Exception:
            print('++')
            raise
