from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status

from src.app.dto.landmark.landmark import LandmarkResponse, LandmarkWithoutCityResponse
from src.app.factory.factory import get_base_service
from src.app.models import Landmark
from src.app.services.base_service import BaseService

landmark_router = APIRouter(prefix='/landmarks', tags=['landmark'])


@landmark_router.get('/{_id}', response_model=LandmarkResponse, status_code=status.HTTP_200_OK)
async def get_landmark_by_id(_id: int,
                             base_service: BaseService = Depends(get_base_service(Landmark))) -> LandmarkResponse:
    return await base_service.get_by_id(_id, LandmarkResponse)


@landmark_router.get('', response_model=LandmarkWithoutCityResponse, status_code=status.HTTP_200_OK)
async def get_all_landmarks(base_service: BaseService = Depends(get_base_service(Landmark))) -> [
    list[LandmarkWithoutCityResponse]]:
    return await base_service.get_all(LandmarkWithoutCityResponse)


@landmark_router.delete('/{_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_landmark(_id: int, base_service: BaseService = Depends(get_base_service(Landmark))) -> None:
    await base_service.delete_by_id(_id)
