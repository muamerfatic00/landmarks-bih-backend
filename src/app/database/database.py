from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@v-b-database:5432/v-b'

engine = create_async_engine(
    DATABASE_URL, pool_size=100, max_overflow=0, pool_pre_ping=False
)

session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    session = session_maker()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
