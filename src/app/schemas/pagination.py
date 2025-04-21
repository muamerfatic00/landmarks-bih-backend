from pydantic import BaseModel, Field
from typing_extensions import TypeVar

T = TypeVar("T")

MAX_RESULTS_PER_PAGE = 20


class PaginationParam(BaseModel):
    page: int = Field(default=1, ge=1, description="Requested page number")
    page_size: int = Field(
        default=10,
        ge=1,
        le=MAX_RESULTS_PER_PAGE,
        description="Requested number of items per page",
    )
