# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
from fastapi import APIRouter, Depends
from core.controllers.facial_recognition_controller import FacialRecognitionController
from core.schemas.image_validate_schema import ImageValidateSchema, GetValidateFaceResponse
router = APIRouter()


@router.post("/")
def validate_face(images: ImageValidateSchema,
                  facial_recognition_controller:
                  FacialRecognitionController = Depends()) -> GetValidateFaceResponse:
    return facial_recognition_controller.validate_face(images)
