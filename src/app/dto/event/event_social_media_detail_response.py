from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.event.event import EventBaseResponse
from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class EventSocialMediaDetailResponse(CamelModel, TimestampDto):
    id: int
    type: SocialMediaType
    url: str
    event: Optional[EventBaseResponse]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
