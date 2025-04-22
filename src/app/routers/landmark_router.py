from fastapi import APIRouter
from fastapi.params import Depends

from src.app.dto.landmark.landmark import LandmarkResponse, LandmarkWithoutCityResponse
from src.app.factory.factory import get_base_service
from src.app.models import Landmark
from src.app.services.base_service import BaseService

landmark_router = APIRouter(prefix='/landmarks', tags=['landmark'])


@landmark_router.get('/{_id}', response_model=LandmarkResponse, status_code=200)
async def get_landmark_by_id(_id: int,
                             base_service: BaseService = Depends(get_base_service(Landmark))) -> LandmarkResponse:
    return await base_service.get_by_id(_id, LandmarkResponse)


@landmark_router.get('', response_model=LandmarkWithoutCityResponse, status_code=200)
async def get_all_landmarks(base_service: BaseService = Depends(get_base_service(Landmark))) -> [
    list[LandmarkWithoutCityResponse]]:
    return await base_service.get_all(LandmarkWithoutCityResponse)
