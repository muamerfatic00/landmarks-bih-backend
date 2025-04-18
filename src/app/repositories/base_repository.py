from typing import Generic, Type, cast, Any

from icecream import ic
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing_extensions import TypeVar, Optional

from src.app.database import Base

ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, data:dict[str,Any]) -> Optional[ModelType]:
        if data is None:
            data = {}

        new_record = self.model(**data)
        self.session.add(new_record)
        try:
            # await self.session.flush()
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
        print('get by')
        print('+++')
        return result.unique().scalar_one_or_none() if unique else result.scalar()
