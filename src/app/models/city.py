from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.app.database import Base


class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    image_url = Column(String)
    google_maps_url=Column(String)
    landmarks=relationship("Landmark", back_populates="city")

    def __str__(self):
        return (
            f"<City(id='{self.id}', name='{self.name}', description='{self.description}', image_url='{self.image_url}')>")

    def __repr__(self):
        return f"City({self.id},{self.name},{self.description},{self.image_url})"
