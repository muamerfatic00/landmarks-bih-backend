import math
from typing import Generic, Type, cast, Any

from fastapi_pagination import Page
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import TypeVar, Optional

from src.app.database import Base
from src.app.schemas.paginated import PaginationParam

ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, data: dict[str, Any]) -> Optional[ModelType]:
        if data is None:
            data = {}
        new_record = self.model(**data)
        self.session.add(new_record)
        try:
            await self.session.commit()
            await self.session.refresh(new_record)

        except Exception as e:
            await self.session.rollback()
            raise e
        return new_record

    async def get_by(self, field: str, value, unique=True) -> Optional[ModelType]:
        if not hasattr(self.model, field):
            raise ValueError(f'Field {field} is not defined')
        query = select(self.model).where(cast("ColumnElement[bool]", getattr(self.model, field) == value))
        result = await self.session.execute(query)
        return result.unique().scalar_one_or_none() if unique else result.scalar()

    async def get_all(self) -> Optional[list[ModelType]]:
        query = select(self.model)
        result = await self.session.execute(query)
        items = result.scalars().all()
        return items if items else None

    async def get_paginated(
            self,
            pagination_param: PaginationParam
    ) -> Page[ModelType]:
        page_size = pagination_param.page_size
        current_page = pagination_param.page

        query = select(func.count()).select_from(self.model)
        result = await self.session.execute(query)
        total_items = result.scalar_one()

        total_pages = math.ceil(total_items / page_size)
        offset = (current_page - 1) * page_size

        query = select(self.model).offset(offset).limit(page_size)
        result = await self.session.execute(query)
        items = result.scalars().all()

        return Page[ModelType](total=total_items, items=items, page=current_page, size=page_size, pages=total_pages)

    async def update(self, record_for_update, data_for_update: dict[str, Any]):
        for key, value in data_for_update.items():
            setattr(record_for_update, key, value)
        try:
            await self.session.commit()
            await self.session.refresh(record_for_update)
        except:
            await self.session.rollback()
            raise
        finally:
            await self.session.close()

    async def delete(self, record_for_delete: ModelType):
        try:
            await self.session.delete(record_for_delete)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        finally:
            await self.session.close()
