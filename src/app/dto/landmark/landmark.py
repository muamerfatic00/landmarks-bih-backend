from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_without_landmark import CityWithoutLandmarkResponse


class LandmarkBase(CamelModel):
    name: str
    description: str


class LandmarkResponse(LandmarkBase):
    id: int
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]
    city: Optional[CityWithoutLandmarkResponse]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class LandmarkWithoutCityResponse(LandmarkBase):
    id: int
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]

    class Config:
        from_attributes = True
