from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class EventSocialMediaBase(CamelModel):
    type: SocialMediaType
    url: str


class EventSocialMediaPostRequest(EventSocialMediaBase):
    event_id: int


class EventSocialMediaPutRequest(EventSocialMediaBase):
    id: int
    event_id: int


class EventSocialMediaBaseResponse(EventSocialMediaBase, TimestampDto):
    id: int
    event_id: int

    class Config:
        from_attributes = True
