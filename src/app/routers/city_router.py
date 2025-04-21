from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from fastapi_pagination import Page
from pydantic import ValidationError
from starlette import status

from src.app.dto.city import CityResponse, CityRequest, CityUpdateRequest
from src.app.factory.factory import get_city_service
from src.app.models import City
from src.app.schemas.pagination import PaginationParam
from src.app.services.city_service import CityService

city_router = APIRouter(prefix='/cities', tags=['cities'])


@city_router.post('', response_model=CityResponse, status_code=status.HTTP_201_CREATED)
async def create_city(data: CityRequest, city_service: CityService = Depends(get_city_service)) -> City:
    return await city_service.create(data)


@city_router.get("/list", response_model=Page[CityResponse], status_code=status.HTTP_200_OK, )
async def get_paginated_cities(page: int = Query(default=1), page_size: int = Query(default=10),
                               city_service: CityService = Depends(get_city_service)):
    try:
        pagination = PaginationParam(page=page, page_size=page_size)
        return await city_service.get_paginated(pagination)
    except Exception as e:
        if isinstance(e, ValidationError):
            raise HTTPException(status_code=400, detail="Query params page and page_size must be greater than 0!")
        raise HTTPException(status_code=500, detail=str(e))


@city_router.get('/{city_id}', response_model=CityResponse, status_code=status.HTTP_200_OK)
async def get_city(city_id: int, city_service: CityService = Depends(get_city_service)) -> CityResponse:
    return await city_service.get_by_id(city_id)


@city_router.get("", response_model=list[CityResponse], status_code=status.HTTP_200_OK)
async def get_all_cities(city_service: CityService = Depends(get_city_service)) -> list[CityResponse]:
    return await city_service.get_all()


@city_router.put("/{city_id}", response_model=CityResponse, status_code=status.HTTP_200_OK)
async def update_city(city_id: int, data_for_update: CityUpdateRequest,
                      city_service: CityService = Depends(get_city_service)):
    return await city_service.update(city_id, data_for_update)


@city_router.delete('/{city_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(city_id: int, city_service: CityService = Depends(get_city_service)):
    await city_service.delete(city_id)
