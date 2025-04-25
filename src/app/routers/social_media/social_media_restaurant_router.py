from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.restaurant.restaurant_social_media import RestaurantSocialMediaBaseResponse, \
    RestaurantSocialMediaPostRequest, RestaurantSocialMediaPutRequest
from src.app.dto.restaurant.restaurant_social_media_detail_response import RestaurantSocialMediaDetailResponse
from src.app.factory.factory import get_social_media_restaurant_service
from src.app.services.base_service import BaseService

social_media_restaurant_router = APIRouter(prefix="/social-medias/restaurants", tags=["social-medias"])


@social_media_restaurant_router.post("/", response_model=RestaurantSocialMediaBaseResponse,
                                     status_code=HTTP_201_CREATED)
async def create_social_media_restaurant(data: RestaurantSocialMediaPostRequest, social_media_restaurant_service: BaseService = Depends(
    get_social_media_restaurant_service())) -> RestaurantSocialMediaBaseResponse:
    return await social_media_restaurant_service.create(data, RestaurantSocialMediaBaseResponse)


@social_media_restaurant_router.get("/{_id}", response_model=RestaurantSocialMediaDetailResponse,
                                    status_code=HTTP_200_OK)
async def get_social_media_restaurant(_id: int, social_media_restaurant_service: BaseService = Depends(
    get_social_media_restaurant_service())) -> RestaurantSocialMediaDetailResponse:
    return await social_media_restaurant_service.get_by_id(_id, RestaurantSocialMediaDetailResponse)


@social_media_restaurant_router.put("/{_id}", response_model=RestaurantSocialMediaBaseResponse,
                                    status_code=HTTP_200_OK)
async def update_social_media_restaurant(_id: int, data_for_update: RestaurantSocialMediaPutRequest,
                                         social_media_restaurant_service: BaseService = Depends(
                                             get_social_media_restaurant_service())) -> RestaurantSocialMediaBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await social_media_restaurant_service.update(_id, data_for_update, RestaurantSocialMediaBaseResponse)


@social_media_restaurant_router.delete("/{_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_social_media_restaurant(_id: int, social_media_restaurant_service: BaseService = Depends(
    get_social_media_restaurant_service())) -> None:
    return await social_media_restaurant_service.delete_by_id(_id)
