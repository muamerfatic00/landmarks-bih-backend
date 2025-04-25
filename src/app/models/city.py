from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.models.timestamp import TimestampMixin


class City(Base, TimestampMixin):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)
    image_url = Column(String)
    google_maps_url = Column(String)

    # Relationships
    landmarks = relationship("Landmark", back_populates="city")
    accommodations = relationship("Accommodation", back_populates="city")
    events = relationship("Event", back_populates="city")
    restaurants = relationship("Restaurant", back_populates="city")

    def __str__(self):
        return (
            f"<City(id={self.id}, name={self.name}, description={self.description}, image_url={self.image_url}, "
            f"google_maps_url={self.google_maps_url}, landmarks={self.landmarks}, accommodations={self.accommodations}, "
            f"events={self.events}, restaurants={self.restaurants}>)>")

    def __repr__(self):
        return (f"City(id={self.id},name={self.name},description={self.description},"
                f"image_url={self.image_url},google_maps_url={self.google_maps_url})")
