from typing import Optional

from fastapi_camelcase import CamelModel

from src.app.dto.city.city_without_landmark import CityWithoutLandmarkResponse


class LandmarkBase(CamelModel):
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]


class LandmarkCreateRequest(LandmarkBase):
    city_id: Optional[int]


class LandmarkUpdateRequest(LandmarkBase):
    city_id: Optional[int]

    class Config:
        from_attributes = True


class LandmarkResponse(LandmarkBase):
    id: int
    city: Optional[CityWithoutLandmarkResponse]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class LandmarkPostResponse(LandmarkCreateRequest):
    class Config:
        from_attributes = True


class LandmarkWithoutCityResponse(LandmarkBase):
    id: int

    class Config:
        from_attributes = True
