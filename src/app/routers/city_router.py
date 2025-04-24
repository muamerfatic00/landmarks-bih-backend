from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from fastapi_pagination import Page
from pydantic import ValidationError
from starlette import status

from src.app.dto.city.city import CityDetailResponse, CityPostRequest, CityPutRequest
from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.factory.factory import get_city_service, get_base_service
from src.app.models import City
from src.app.schemas.pagination import PaginationParam
from src.app.services.base_service import BaseService
from src.app.services.city_service import CityService

city_router = APIRouter(prefix='/cities', tags=['cities'])


@city_router.post('', response_model=CityBaseResponse, status_code=status.HTTP_201_CREATED)
async def create_city(data: CityPostRequest,
                      city_service: CityService = Depends(get_city_service)) -> CityBaseResponse:
    return await city_service.create(data)


@city_router.get('/list', response_model=Page[CityDetailResponse], status_code=status.HTTP_200_OK)
async def get_paginated_cities(page: int = Query(default=1), page_size: int = Query(default=10),
                               base_service: BaseService = Depends(get_base_service(City))) -> Page[CityDetailResponse]:
    try:
        pagination = PaginationParam(page=page, page_size=page_size)
        return await base_service.get_paginated(pagination, CityDetailResponse)
    except Exception as e:
        if isinstance(e, ValidationError):
            raise HTTPException(status_code=400, detail="Query params page and page_size must be greater than 0!")
        raise HTTPException(status_code=500, detail=str(e))


@city_router.get('/{_id}', response_model=CityDetailResponse, status_code=status.HTTP_200_OK)
async def get_city(_id: int, base_service: BaseService = Depends(get_base_service(City))) -> CityDetailResponse:
    return await base_service.get_by_id(_id, CityDetailResponse)


@city_router.get("", response_model=list[CityDetailResponse], status_code=status.HTTP_200_OK)
async def get_all_cities(base_service: BaseService = Depends(get_base_service(City))) -> list[CityDetailResponse]:
    return await base_service.get_all(CityDetailResponse)


@city_router.put('/{_id}', response_model=CityBaseResponse, status_code=status.HTTP_200_OK)
async def update_city(_id: int, data_for_update: CityPutRequest,
                      base_service: BaseService = Depends(get_base_service(City))) -> CityBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await base_service.update(_id, data_for_update, CityBaseResponse)


@city_router.delete('/{_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_city(_id: int, base_service: BaseService = Depends(get_base_service(City))) -> None:
    await base_service.delete_by_id(_id)
