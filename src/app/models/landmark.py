from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.models.timestamp import TimestampMixin


class Landmark(Base, TimestampMixin):
    __tablename__ = 'landmarks'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image_url = Column(String)
    google_maps_url = Column(String)
    contact_number = Column(String)
    mail = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))

    # Relationships
    city = relationship('City', back_populates='landmarks')
    accommodations = relationship('Accommodation', back_populates='landmark')
    events = relationship('Event', back_populates='landmark')
    restaurants = relationship('Restaurant', back_populates='landmark')

    def __str__(self):
        return (
            f"<Landmark(id={self.id}, name={self.name}, description={self.description}), image_url={self.image_url}, "
            f"google_maps_url={self.google_maps_url}, contact_number={self.contact_number}, mail={self.mail}, "
            f"city_id={self.city_id}, accommodations={self.accommodations}, events={self.events}, restaurants={self.restaurants})>")

    def __repr__(self):
        return (
            f"Landmark(id={self.id},name={self.name},description={self.description},image_url={self.image_url},"
            f"google_maps_url={self.google_maps_url},contact_number={self.contact_number},mail={self.mail},"
            f"city_id={self.city_id})")
