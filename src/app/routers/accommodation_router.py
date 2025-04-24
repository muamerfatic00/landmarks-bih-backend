from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.accommodation.accommodation import AccommodationDetailResponse, AccommodationPostRequest, \
    AccommodationPutRequest, AccommodationBaseResponse
from src.app.factory.factory import get_base_service
from src.app.models import Accommodation
from src.app.schemas.pagination import PaginationParam
from src.app.services.base_service import BaseService

accommodation_router = APIRouter(prefix="/accommodations", tags=["accommodations"])


@accommodation_router.post('', response_model=AccommodationBaseResponse, status_code=HTTP_201_CREATED)
async def create_accommodation(data: AccommodationPostRequest, base_service: BaseService = Depends(
    get_base_service(Accommodation))) -> AccommodationBaseResponse:
    return await base_service.create(data, AccommodationBaseResponse)


@accommodation_router.get('/list', response_model=Page[AccommodationDetailResponse], status_code=HTTP_200_OK)
async def get_paginated_accommodations(page: int = Query(default=1), page_size: int = Query(default=10),
                                       base_service: BaseService = Depends(get_base_service(Accommodation))) -> Page[
    AccommodationDetailResponse]:
    pagination_param = PaginationParam(page=page, page_size=page_size)
    return await base_service.get_paginated(pagination_param, AccommodationDetailResponse)


@accommodation_router.get('/{_id}', response_model=AccommodationDetailResponse, status_code=HTTP_200_OK)
async def get_accommodation(_id: int, base_service: BaseService = Depends(
    get_base_service(Accommodation))) -> AccommodationDetailResponse:
    return await base_service.get_by_id(_id, AccommodationDetailResponse)


@accommodation_router.get("", response_model=list[AccommodationDetailResponse], status_code=HTTP_200_OK)
async def get_all_accommodations(base_service: BaseService = Depends(get_base_service(Accommodation))) -> list[
    AccommodationDetailResponse]:
    return await base_service.get_all(AccommodationDetailResponse)


@accommodation_router.put("/{_id}", response_model=AccommodationBaseResponse, status_code=HTTP_200_OK)
async def update_accommodation(_id: int, data_for_update: AccommodationPutRequest, base_service: BaseService = Depends(
    get_base_service(Accommodation))) -> AccommodationBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await base_service.update(_id, data_for_update, AccommodationBaseResponse)


@accommodation_router.delete('/{_id}', response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_accommodation(_id: int, base_service: BaseService = Depends(get_base_service(Accommodation))) -> None:
    return await base_service.delete_by_id(_id)
