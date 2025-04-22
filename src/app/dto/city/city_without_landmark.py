from typing import Optional

from fastapi_camelcase import CamelModel


class CityWithoutLandmarkResponse(CamelModel):
    id: int
    name: str
    description: str
    image_url: Optional[str]
    google_maps_url: Optional[str]

    class Config:
        from_attributes = True
