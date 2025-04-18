from sqlalchemy import Column, Integer, String

from src.app.database import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    image_url = Column(String)
