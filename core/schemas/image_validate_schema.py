# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
from pydantic import BaseModel


class ImageValidateSchema(BaseModel):
    reference_image: str
    image_to_compare: str


class GetValidateFaceResponse(BaseModel):
    is_valid: bool
    similarity: float
    message: str
