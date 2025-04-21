from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.app.database import Base


class Landmark(Base):
    __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String)
    google_maps_url = Column(String)
    contact_number = Column(String)
    mail = Column(String)
    city_id = Column(ForeignKey('cities.id'))

    # Relationships
    city = relationship('City', back_populates='landmarks')

    def __str__(self):
        return (
            f"<Landmark(id={self.id}, name={self.name}, description={self.description}), image_url={self.image_url},"
            f" google_maps_url={self.google_maps_url}, contact_number={self.contact_number}, mail={self.mail})>")

    def __repr__(self):
        return (
            f"Landmark({self.id}, {self.name}, {self.description}, {self.image_url},"
            f" {self.google_maps_url}, {self.contact_number}, {self.mail})")
