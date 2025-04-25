from fastapi import APIRouter
from fastapi.params import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.restaurant.restaurant_social_media import RestaurantSocialMediaBaseResponse, \
    RestaurantSocialMediaPostRequest
from src.app.dto.restaurant.restaurant_social_media_detail_response import RestaurantSocialMediaDetailResponse
from src.app.factory.factory import get_base_service
from src.app.models import RestaurantSocialMedia
from src.app.services.base_service import BaseService

social_media_restaurant_router = APIRouter(prefix="/social-medias/restaurants", tags=["social-medias"])


@social_media_restaurant_router.post("/", response_model=RestaurantSocialMediaBaseResponse,
                                     status_code=HTTP_201_CREATED)
async def create_social_media_restaurant(data: RestaurantSocialMediaPostRequest, base_service: BaseService = Depends(
    get_base_service(RestaurantSocialMedia))) -> RestaurantSocialMediaBaseResponse:
    return await base_service.create(data, RestaurantSocialMediaBaseResponse)


@social_media_restaurant_router.get("/{_id}", response_model=RestaurantSocialMediaDetailResponse,
                                    status_code=HTTP_200_OK)
async def get_social_media_restaurant(_id: int, base_service: BaseService = Depends(
    get_base_service(RestaurantSocialMedia))) -> RestaurantSocialMediaDetailResponse:
    return await base_service.get_by_id(_id, RestaurantSocialMediaDetailResponse)


@social_media_restaurant_router.put("/{_id}", response_model=RestaurantSocialMediaBaseResponse,
                                    status_code=HTTP_200_OK)
async def update_social_media_restaurant(_id: int, data_for_update: RestaurantSocialMediaPostRequest,
                                         base_service: BaseService = Depends(get_base_service(
                                             RestaurantSocialMedia))) -> RestaurantSocialMediaBaseResponse:
    return await base_service.update(_id, data_for_update, RestaurantSocialMediaBaseResponse)


@social_media_restaurant_router.delete("/{_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_social_media_restaurant(_id: int, base_service: BaseService = Depends(
    get_base_service(RestaurantSocialMedia))) -> None:
    return await base_service.delete_by_id(_id)
