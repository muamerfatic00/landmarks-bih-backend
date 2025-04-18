from fastapi import APIRouter, Depends
from icecream import ic

from src.app.dto.city import CityResponse, CityRequest
from src.app.factory.factory import get_city_service
from src.app.services.city_service import CityService

city_router = APIRouter(prefix='/cities', tags=['cities'])


@city_router.post('/', response_model=CityResponse)
async def create_city(data: CityRequest, city_service: CityService = Depends(get_city_service)) -> CityResponse:
    return await city_service.create(data)


@city_router.get('/{city_id}', response_model=CityResponse)
async def get_city(city_id: int, city_service: CityService = Depends(get_city_service)) -> CityResponse:
    return await city_service.get_by_id(city_id)
