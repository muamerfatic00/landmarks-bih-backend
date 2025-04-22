from typing import Optional, Type

from fastapi import HTTPException
from fastapi_pagination import Page
from pydantic import BaseModel
from sqlalchemy.exc import NoResultFound, IntegrityError
from typing_extensions import TypeVar

from src.app.repositories.base_repository import BaseRepository
from src.app.schemas.pagination import PaginationParam
from src.app.utils.dto_utils import to_dto

ResponseModel = TypeVar('ResponseModel', bound=BaseModel)
RequestModel = TypeVar('RequestModel', bound=BaseModel)


class BaseService:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def create(self, data: RequestModel, response_model: Type[ResponseModel]) -> Optional[ResponseModel]:
        try:
            created_record = await self.repository.create(data.__dict__)
            return to_dto(response_model, created_record)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def get_all(self, response_model: Type[ResponseModel]) -> Optional[list[ResponseModel]]:
        try:
            list_of_records = await self.repository.get_all(join=True)
            response = [to_dto(response_model, record) for record in list_of_records]
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_by_id(self, _id: int, response_model: Type[ResponseModel]) -> Optional[ResponseModel]:
        try:
            record = await self.repository.get_by("id", _id, unique=True, join=True)
            if not record:
                raise NoResultFound(f"Record with id {_id} does not exist.")
            return to_dto(response_model, record)
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))

    async def get_paginated(self, pagination_param: PaginationParam, response_model: Type[ResponseModel]) -> Page:
        try:
            paginated_list = await self.repository.get_paginated(pagination_param, join=True)
            paginated_list.items = [to_dto(response_model, item) for item in paginated_list.items]
            return paginated_list
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update(self, _id: int, data: RequestModel, response_model: Type[ResponseModel]) -> Optional[
        ResponseModel]:
        try:
            record_for_update = await self.repository.get_by("id", _id, unique=True)
            if not record_for_update:
                raise NoResultFound(f"Record with id {_id} does not exist.")
            await self.repository.update(record_for_update, data.__dict__)
            return to_dto(response_model, record_for_update)
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            if isinstance(e, IntegrityError):
                raise HTTPException(status_code=400, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_by_id(self, _id: int) -> None:
        try:
            record_for_delete = await self.repository.get_by("id", _id, unique=True)
            if not record_for_delete:
                raise NoResultFound(f"Record with id {_id} does not exist.")
            await self.repository.delete(record_for_delete)
        except Exception as e:
            if isinstance(e, NoResultFound):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=500, detail=str(e))
