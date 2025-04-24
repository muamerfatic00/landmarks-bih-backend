from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Query
from fastapi_pagination import Page
from pydantic import ValidationError
from starlette import status

from src.app.dto.landmark.landmark import LandmarkDetailResponse, LandmarkPutRequest, LandmarkPostRequest
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse
from src.app.factory.factory import get_base_service
from src.app.models import Landmark
from src.app.schemas.pagination import PaginationParam
from src.app.services.base_service import BaseService

landmark_router = APIRouter(prefix='/landmarks', tags=['landmark'])


@landmark_router.post('', response_model=LandmarkBaseResponse, status_code=status.HTTP_201_CREATED)
async def create_landmark(data: LandmarkPostRequest,
                          base_service: BaseService = Depends(get_base_service(Landmark))) -> LandmarkBaseResponse:
    return await base_service.create(data, LandmarkBaseResponse)


@landmark_router.get('/list', response_model=Page[LandmarkDetailResponse], status_code=status.HTTP_200_OK)
async def get_paginated_landmarks(page: int = Query(default=1), page_size: int = Query(default=10),
                                  base_service: BaseService = Depends(get_base_service(Landmark))) -> Page[
    LandmarkDetailResponse]:
    try:
        pagination = PaginationParam(page=page, page_size=page_size)
        return await base_service.get_paginated(pagination, LandmarkDetailResponse)
    except Exception as e:
        if isinstance(e, ValidationError):
            raise HTTPException(status_code=400, detail="Query params page and page_size must be greater than 0!")
        raise HTTPException(status_code=500, detail=str(e))


@landmark_router.get('/{_id}', response_model=LandmarkDetailResponse, status_code=status.HTTP_200_OK)
async def get_landmark_by_id(_id: int,
                             base_service: BaseService = Depends(get_base_service(Landmark))) -> LandmarkDetailResponse:
    return await base_service.get_by_id(_id, LandmarkDetailResponse)


@landmark_router.get('', response_model=list[LandmarkDetailResponse], status_code=status.HTTP_200_OK)
async def get_all_landmarks(base_service: BaseService = Depends(get_base_service(Landmark))) -> [
    list[LandmarkDetailResponse]]:
    return await base_service.get_all(LandmarkDetailResponse)


@landmark_router.put('/{_id}', response_model=LandmarkBaseResponse, status_code=status.HTTP_200_OK)
async def update_landmark(_id: int, data_for_update: LandmarkPutRequest, base_service: BaseService = Depends(
    get_base_service(Landmark))) -> LandmarkBaseResponse:
    if _id is not data_for_update.id:
        raise HTTPException(status_code=400, detail="Id from path variable and id form body request must be equal!")
    return await base_service.update(_id, data_for_update, LandmarkBaseResponse)


@landmark_router.delete('/{_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_landmark(_id: int, base_service: BaseService = Depends(get_base_service(Landmark))) -> None:
    await base_service.delete_by_id(_id)
