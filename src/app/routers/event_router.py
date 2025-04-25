from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi_pagination import Page
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.app.dto.event.event import EventBaseResponse, EventPostRequest, EventDetailResponse, EventPutRequest
from src.app.factory.factory import get_event_service
from src.app.schemas.pagination import PaginationParam
from src.app.services.base_service import BaseService

event_router = APIRouter(prefix="/events", tags=["events"])


@event_router.post("", response_model=EventBaseResponse, status_code=HTTP_201_CREATED)
async def create_event(data: EventPostRequest,
                       event_service: BaseService = Depends(get_event_service())) -> EventBaseResponse:
    return await event_service.create(data, EventBaseResponse)


@event_router.get("/list", response_model=Page[EventDetailResponse], status_code=HTTP_200_OK)
async def get_paginated_events(page: int = Query(default=1), page_size: int = Query(default=10),
                               event_service: BaseService = Depends(get_event_service())) -> Page[EventDetailResponse]:
    pagination_param = PaginationParam(page=page, page_size=page_size)
    return await event_service.get_paginated(pagination_param, EventDetailResponse)


@event_router.get("/{_id}", response_model=EventDetailResponse, status_code=HTTP_200_OK)
async def get_event(_id: int, event_service: BaseService = Depends(get_event_service())) -> EventDetailResponse:
    return await event_service.get_by_id(_id, EventDetailResponse)


@event_router.get("", response_model=list[EventDetailResponse], status_code=HTTP_200_OK)
async def get_all_events(event_service: BaseService = Depends(get_event_service())) -> list[EventDetailResponse]:
    return await event_service.get_all(EventDetailResponse)


@event_router.put("/{_id}", response_model=EventBaseResponse, status_code=HTTP_200_OK)
async def update_event(_id: int, data_for_update: EventPutRequest,
                       event_service: BaseService = Depends(get_event_service())) -> EventBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await event_service.update(_id, data_for_update, EventBaseResponse)


@event_router.delete("/{_id}", response_model=None, status_code=HTTP_204_NO_CONTENT)
async def delete_event(_id: int, event_service: BaseService = Depends(get_event_service())) -> None:
    return await event_service.delete_by_id(_id)
