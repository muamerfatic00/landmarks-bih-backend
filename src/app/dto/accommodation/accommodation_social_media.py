from fastapi_camelcase import CamelModel

from src.app.dto.timestamp import TimestampDto
from src.app.enums.social_media_type import SocialMediaType


class AccommodationSocialMediaBase(CamelModel):
    type: SocialMediaType
    url: str
    accommodation_id: int


class AccommodationSocialMediaPostRequest(AccommodationSocialMediaBase):
    pass


class AccommodationSocialMediaPutRequest(AccommodationSocialMediaBase):
    id: int


class AccommodationSocialMediaBaseResponse(AccommodationSocialMediaBase, TimestampDto):
    id: int

    class Config:
        from_attributes = True
