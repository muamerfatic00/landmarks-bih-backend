from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.accommodation.accommodation import AccommodationBaseResponse
from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class AccommodationSocialMediaDetailResponse(CamelModel, TimestampDto):
    id: int
    type: SocialMediaType
    url: str
    accommodation: Optional[AccommodationBaseResponse]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
