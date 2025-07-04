from sqlalchemy import Column, Enum as SqlEnum, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.enums.social_media_type import SocialMediaType
from src.app.models.timestamp import TimestampMixin


class AccommodationSocialMedia(Base, TimestampMixin):
    __tablename__ = "accommodations_social_medias"

    id = Column(Integer, primary_key=True)
    type = Column(SqlEnum(SocialMediaType), nullable=False)
    url = Column(String, nullable=False)
    accommodation_id = Column(Integer, ForeignKey("accommodations.id", ondelete="CASCADE"), nullable=False)

    # relationships
    accommodation = relationship("Accommodation", back_populates="social_medias")

    # constraints
    __table_args__ = (
        UniqueConstraint("accommodation_id", "type", name="accommodations_social_media_unique_constraint"),
    )

    def __str__(self):
        return f"<AccommodationSocialMedia(id={self.id}, type={self.type}, url={self.url}, accommodation_id={self.accommodation_id})>"

    def __repr__(self):
        return f"AccommodationSocialMedia(id={self.id},type={self.type},url={self.url},accommodation_id={self.accommodation_id})"
