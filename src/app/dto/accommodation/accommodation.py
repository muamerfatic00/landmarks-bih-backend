from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.accommodation.accommodation_social_media import AccommodationSocialMediaBaseResponse
from src.app.dto.city.city_base_response import CityBaseResponse
from src.app.dto.landmark.landmark_base_response import LandmarkBaseResponse
from src.app.dto.timestamp import TimestampDto


class AccommodationBase(CamelModel):
    name: str
    description: Optional[str]
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]


class AccommodationPostRequest(AccommodationBase):
    city_id: Optional[int]
    landmark_id: Optional[int]


class AccommodationPutRequest(AccommodationBase):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]


class AccommodationBaseResponse(AccommodationBase, TimestampDto):
    id: int
    city_id: Optional[int]
    landmark_id: Optional[int]

    class Config:
        from_attributes = True


class AccommodationDetailResponse(AccommodationBase, TimestampDto):
    id: int
    city: Optional[CityBaseResponse]
    landmark: Optional[LandmarkBaseResponse]
    social_medias:Optional[list[AccommodationSocialMediaBaseResponse]]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
