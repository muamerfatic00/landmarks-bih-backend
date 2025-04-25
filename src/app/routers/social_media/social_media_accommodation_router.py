
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.accommodation.accommodation_social_media import AccommodationSocialMediaBaseResponse, \
    AccommodationSocialMediaPostRequest, AccommodationSocialMediaPutRequest
from src.app.dto.accommodation.accommodation_social_media_detail_response import AccommodationSocialMediaDetailResponse
from src.app.factory.factory import get_social_media_accommodation_service
from src.app.services.base_service import BaseService

social_media_accommodation_router = APIRouter(prefix="/social-medias/accommodations", tags=["social-medias"])


@social_media_accommodation_router.post("", response_model=AccommodationSocialMediaBaseResponse,
                                        status_code=HTTP_201_CREATED)
async def create_accommodation_social_media(data: AccommodationSocialMediaPostRequest,
                                            social_media_accommodation_service: BaseService = Depends(
                                                get_social_media_accommodation_service())) -> AccommodationSocialMediaBaseResponse:
    return await social_media_accommodation_service.create(data, AccommodationSocialMediaBaseResponse)


@social_media_accommodation_router.get("/{_id}", response_model=AccommodationSocialMediaDetailResponse,
                                       status_code=HTTP_200_OK)
async def get_accommodation_social_media(_id: int, social_media_accommodation_service: BaseService = Depends(
    get_social_media_accommodation_service())) -> AccommodationSocialMediaDetailResponse:
    return await social_media_accommodation_service.get_by_id(_id, AccommodationSocialMediaDetailResponse)


@social_media_accommodation_router.put("/{_id}", response_model=AccommodationSocialMediaBaseResponse,
                                       status_code=HTTP_200_OK)
async def update_accommodation_social_media(_id: int, data_for_update: AccommodationSocialMediaPutRequest,
                                            social_media_accommodation_service: BaseService = Depends(
                                                get_social_media_accommodation_service())) -> AccommodationSocialMediaBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await social_media_accommodation_service.update(_id, data_for_update, AccommodationSocialMediaBaseResponse)


@social_media_accommodation_router.delete("/{_id}",
                                          status_code=HTTP_204_NO_CONTENT)
async def delete_accommodation_social_media(_id: int,
                                            social_media_accommodation_service: BaseService = Depends(
                                                get_social_media_accommodation_service())) -> None:
    await social_media_accommodation_service.delete_by_id(_id)
