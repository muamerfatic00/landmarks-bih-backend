import math
from typing import Generic, Type, cast, Any

from fastapi_pagination import Page
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, noload
from typing_extensions import TypeVar, Optional

from src.app.database import Base
from src.app.schemas.pagination import PaginationParam

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    type_for_loading = "Literal['*']"
    type_for_where_clause = "ColumnElement[bool]"

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

    async def get_by(self, field: str, value, unique: bool = True, join: bool = False) -> Optional[ModelType]:
        if not hasattr(self.model, field):
            raise ValueError(f"Field {field} is not defined")

        if join:
            query = (select(self.model).options(selectinload(cast(self.type_for_loading, "*"))).where(
                cast(self.type_for_where_clause, getattr(self.model, field) == value)))
        else:
            query = select(self.model).options(noload(cast(self.type_for_loading, "*"))).where(
                cast(self.type_for_where_clause, getattr(self.model, field) == value))

        result = await self.session.execute(query)
        return result.unique().scalar_one_or_none() if unique else result.scalar()

    async def get_all(self, join: bool = False) -> Optional[list[ModelType]]:
        if join:
            query = select(self.model).options(selectinload(cast(self.type_for_loading, "*")))
        else:
            query = select(self.model).options(noload(cast(self.type_for_loading, "*")))
        result = await self.session.execute(query)
        items = result.scalars().all()
        return items if items else None

    async def get_paginated(
            self,
            pagination_param: PaginationParam, join: bool = False,
    ) -> Page[ModelType]:
        page_size = pagination_param.page_size
        current_page = pagination_param.page

        query_for_count = select(func.count()).select_from(self.model)
        count_result = await self.session.execute(query_for_count)
        total_items = count_result.scalar_one()

        total_pages = math.ceil(total_items / page_size)
        offset = (current_page - 1) * page_size

        if join:
            query_for_pagination = select(self.model).options(selectinload(cast(self.type_for_loading, "*"))).offset(
                offset).limit(page_size)
        else:
            query_for_pagination = select(self.model).options(noload(cast(self.type_for_loading, "*"))).offset(
                offset).limit(page_size)
        pagination_result = await self.session.execute(query_for_pagination)
        items = pagination_result.scalars().all()

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
