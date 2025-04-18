from fastapi_camelcase import CamelModel


class CityResponse(CamelModel):
    id: int
    name: str
    description: str
    image_url: str

    model_config = {
        "from_attributes": True
    }

class CityRequest(CamelModel):
    name: str
    description: str
    image_url: str
