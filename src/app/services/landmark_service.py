from typing import Optional

from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

from src.app.dto.landmark.landmark import LandmarkResponse
from src.app.repositories.landmark_repository import LandmarkRepository
from src.app.utils.dto_utils import to_dto


class LandmarkService:
    def __init__(self, repository: LandmarkRepository):
        self.repository = repository

    async def get_by_id(self, id: int) -> Optional[LandmarkResponse]:
        try:
            landmark = await self.repository.get_by("id", id, unique=True, join=True)
            if not landmark:
                raise NoResultFound(f"City with id {id} does not exist.")
            landmark_response = to_dto(LandmarkResponse, landmark)
            return landmark_response
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))

    async def get_all(self) -> Optional[list[LandmarkResponse]]:
        try:
            landmarks = await self.repository.get_all(join=True)
            if not landmarks:
                raise NoResultFound("No landmarks exists")
            landmarks_response = [to_dto(LandmarkResponse, landmark) for landmark in landmarks]
            return landmarks_response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
