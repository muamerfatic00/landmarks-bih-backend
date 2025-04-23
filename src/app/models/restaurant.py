from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.models.timestamp import TimestampMixin


class Restaurant(Base, TimestampMixin):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    image_url = Column(String)
    google_maps_url = Column(String)
    contact_number = Column(String)
    mail = Column(String)
    menu_url = Column(String)
    city_id = Column(Integer, ForeignKey('cities.id'))
    landmark_id = Column(Integer, ForeignKey('landmarks.id'))

    # relationships
    city = relationship('City', back_populates='restaurants')
    landmark = relationship('Landmark', back_populates='restaurants')
    social_medias = relationship('RestaurantSocialMedia', back_populates='restaurant')

    def __str__(self):
        return (f"<Restaurant(id={self.id}, name={self.name}, description={self.description}, "
                f"image_url={self.image_url}, google_maps_url={self.google_maps_url}, "
                f"contact_number={self.contact_number}, mail={self.mail}, city_id={self.city_id}, "
                f"landmark_id={self.landmark_id}, social_medias={self.social_medias})>")

    def __repr__(self):
        return (f"Restaurant(id={self.id},name={self.name},description={self.description},"
                f"image_url={self.image_url},google_maps_url={self.google_maps_url},"
                f"contact_number={self.contact_number},mail={self.mail},city_id={self.city_id},"
                f"landmark_id={self.landmark_id})")
