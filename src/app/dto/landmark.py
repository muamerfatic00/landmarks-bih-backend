from typing import Optional

from fastapi_camelcase import CamelModel


class LandmarkBase(CamelModel):
    name: str
    description: str


class LandmarkResponse(LandmarkBase):
    id: int
    image_url: Optional[str]
    google_maps_url: Optional[str]
    contact_number: Optional[str]
    mail: Optional[str]

    class Config:
        from_attributes = True
