from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.event.event_social_media import EventSocialMediaPostRequest, EventSocialMediaBaseResponse, \
    EventSocialMediaPutRequest
from src.app.dto.event.event_social_media_detail_response import EventSocialMediaDetailResponse
from src.app.factory.factory import get_social_media_event_service
from src.app.services.base_service import BaseService

social_media_event_router = APIRouter(prefix="/social-medias/events", tags=["social-medias"])


@social_media_event_router.post("/", response_model=EventSocialMediaBaseResponse, status_code=HTTP_201_CREATED)
async def create_event_social_media(data: EventSocialMediaPostRequest,
                                    social_media_event_service: BaseService = Depends(
                                        get_social_media_event_service())) -> EventSocialMediaBaseResponse:
    return await social_media_event_service.create(data, EventSocialMediaBaseResponse)


@social_media_event_router.get("/{_id}", response_model=EventSocialMediaDetailResponse, status_code=HTTP_200_OK)
async def get_event_social_media(_id: int, social_media_event_service: BaseService = Depends(
    get_social_media_event_service())) -> EventSocialMediaDetailResponse:
    return await social_media_event_service.get_by_id(_id, EventSocialMediaDetailResponse)


@social_media_event_router.put("/{_id}", response_model=EventSocialMediaBaseResponse, status_code=HTTP_200_OK)
async def update_event_social_media(_id: int, data_for_update: EventSocialMediaPutRequest,
                                    social_media_event_service: BaseService = Depends(
                                        get_social_media_event_service())) -> EventSocialMediaBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await social_media_event_service.update(_id, data_for_update, EventSocialMediaBaseResponse)


@social_media_event_router.delete("/{_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_event_social_media(_id: int,
                                    social_media_event_service: BaseService = Depends(
                                        get_social_media_event_service())) -> None:
    return await social_media_event_service.delete_by_id(_id)
