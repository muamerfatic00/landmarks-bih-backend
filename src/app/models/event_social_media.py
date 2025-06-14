from sqlalchemy import Column, Enum as SqlEnum, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.app.database import Base
from src.app.enums.social_media_type import SocialMediaType
from src.app.models.timestamp import TimestampMixin


class EventSocialMedia(Base, TimestampMixin):
    __tablename__ = "events_social_medias"

    id = Column(Integer, primary_key=True)
    type = Column(SqlEnum(SocialMediaType), nullable=False)
    url = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey("events.id", ondelete="CASCADE"), nullable=False)

    # relationships
    event = relationship("Event", back_populates="social_medias")

    # constraints
    __table_args__ = (
        UniqueConstraint("event_id", "type", name="events_social_media_unique_constraint"),
    )

    def __str__(self):
        return f"<EventSocialMedia(id={self.id}, type={self.type}, url={self.url}, event_id={self.event_id})>"

    def __repr__(self):
        return f"EventSocialMedia(id={self.id},type={self.type},url={self.url},event_id={self.event_id})"
