# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
from fastapi import Depends

from core.dependencies.dependencies import get_facial_recognition_service
from core.services.facial_recognition_service import FacialRecognitionService
from core.exceptions.exceptions import ServerErrorException, NotFoundException, BadRequestException


class FacialRecognitionController:
    def __init__(self, facial_recognition_service:
                 FacialRecognitionService = Depends(get_facial_recognition_service)):
        self.facial_recognition_service = facial_recognition_service

    def validate_face(self, images):
        try:
            result = self.facial_recognition_service.validate_face(images)
            return result

        except NotFoundException as error:
            print(error)
            raise error
        except BadRequestException as error:
            print(error)
            raise error
        except ServerErrorException as error:
            print(error)
            raise error
        except Exception as error:
            print(error)
            raise ServerErrorException from error
