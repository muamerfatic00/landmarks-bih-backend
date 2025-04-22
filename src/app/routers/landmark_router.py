from fastapi import APIRouter
from fastapi.params import Depends

from src.app.dto.landmark.landmark import LandmarkResponse
from src.app.factory.factory import get_landmark_service
from src.app.services.landmark_service import LandmarkService

landmark_router = APIRouter(prefix='/landmarks', tags=['landmark'])


@landmark_router.get('/{landmark_id}', response_model=LandmarkResponse, status_code=200)
async def get_landmark_by_id(landmark_id: int,
                             landmark_service: LandmarkService = Depends(get_landmark_service)) -> LandmarkResponse:
    return await landmark_service.get_by_id(landmark_id)

@landmark_router.get('',response_model=list[LandmarkResponse],status_code=200)
async def get_all_landmarks(landmark_service:LandmarkService=Depends(get_landmark_service)) -> list[LandmarkResponse]:
    return await landmark_service.get_all()