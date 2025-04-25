from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.accommodation.accommodation_social_media import AccommodationSocialMediaBaseResponse
from src.app.dto.establishment.establishment import EstablishmentBaseCommon, EstablishmentDetailCommon
from src.app.dto.timestamp import TimestampDto


class AccommodationBase(CamelModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class AccommodationPostRequest(AccommodationBase, EstablishmentBaseCommon):
    pass


class AccommodationPutRequest(AccommodationBase, EstablishmentBaseCommon):
    id: int


class AccommodationBaseResponse(AccommodationBase, EstablishmentBaseCommon, TimestampDto):
    id: int


class AccommodationDetailResponse(AccommodationBase, EstablishmentDetailCommon, TimestampDto):
    id: int
    social_medias: Optional[list[AccommodationSocialMediaBaseResponse]]
