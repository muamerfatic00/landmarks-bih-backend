from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.landmark.landmark import LandmarkWithoutCityResponse


class CityBase(CamelModel):
    name: str
    description: str
    google_maps_url: Optional[str]


class CityResponse(CityBase):
    id: int
    image_url: str
    landmarks: Optional[list[LandmarkWithoutCityResponse]]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class CityRequest(CityBase):
    image_url: str


class CityUpdateRequest(CityBase):
    image_url: Optional[str]
