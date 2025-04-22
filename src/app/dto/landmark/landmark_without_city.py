from typing import Optional

from src.app.dto.landmark.landmark import LandmarkBase


class LandmarkWithoutCityResponse(LandmarkBase):
    id: int
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]

    class Config:
        from_attributes = True
