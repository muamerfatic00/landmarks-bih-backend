from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.restaurant.restaurant import RestaurantBaseResponse, RestaurantPostRequest, RestaurantDetailResponse, \
    RestaurantPutRequest
from src.app.factory.factory import get_restaurant_service
from src.app.schemas.pagination import PaginationParam
from src.app.services.base_service import BaseService

reastaurant_router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@reastaurant_router.post("", response_model=RestaurantBaseResponse, status_code=HTTP_201_CREATED)
async def create_restaurant(data: RestaurantPostRequest,
                            restaurant_service: BaseService = Depends(
                                get_restaurant_service())) -> RestaurantBaseResponse:
    return await restaurant_service.create(data, RestaurantBaseResponse)


@reastaurant_router.get("/list", response_model=Page[RestaurantDetailResponse], status_code=HTTP_200_OK)
async def get_paginated_restaurants(page: int = Query(default=1), page_size: int = Query(default=10),
                                    restaurant_service: BaseService = Depends(get_restaurant_service())) -> Page[
    RestaurantDetailResponse]:
    pagination_param = PaginationParam(page=page, page_size=page_size)
    return await restaurant_service.get_paginated(pagination_param, RestaurantDetailResponse)


@reastaurant_router.get("/{_id}", response_model=RestaurantDetailResponse, status_code=HTTP_200_OK)
async def get_restaurant(_id: int, restaurant_service: BaseService = Depends(
    get_restaurant_service())) -> RestaurantDetailResponse:
    return await restaurant_service.get_by_id(_id, RestaurantDetailResponse)


@reastaurant_router.get("", response_model=list[RestaurantDetailResponse], status_code=HTTP_200_OK)
async def get_all_restaurants(restaurant_service: BaseService = Depends(get_restaurant_service())) -> list[
    RestaurantDetailResponse]:
    return await restaurant_service.get_all(RestaurantDetailResponse)


@reastaurant_router.put("/{_id}", response_model=RestaurantBaseResponse, status_code=HTTP_200_OK)
async def update_restaurant(_id: int, data_for_update: RestaurantPutRequest,
                            restaurant_service: BaseService = Depends(
                                get_restaurant_service())) -> RestaurantBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await restaurant_service.update(_id, data_for_update, RestaurantBaseResponse)


@reastaurant_router.delete("/{_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_restaurant(_id: int, restaurant_service: BaseService = Depends(get_restaurant_service())) -> None:
    return await restaurant_service.delete_by_id(_id)
