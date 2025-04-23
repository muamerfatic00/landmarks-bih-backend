from sqlalchemy import Column, Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.models.social_media_type import SocialMediaType
from src.app.models.timestamp import TimestampMixin


class RestaurantSocialMedia(Base, TimestampMixin):
    __tablename__ = 'restaurants_social_medias'

    id = Column(Integer, primary_key=True)
    type = Column(SqlEnum(SocialMediaType), nullable=False)
    url = Column(String, nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id", ondelete='CASCADE'), nullable=False)

    # relationships
    restaurant = relationship("Restaurant", back_populates="social_medias")

    def __str__(self):
        return f"<RestaurantSocialMedia(id={self.id}, type={self.type}, url={self.url}, restaurant_id={self.restaurant_id})>"

    def __repr__(self):
        return f"RestaurantSocialMedia(id={self.id},type={self.type},url={self.url},restaurant_id={self.restaurant_id})"
