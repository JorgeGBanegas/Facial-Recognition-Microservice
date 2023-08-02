# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, custom_message=None):
        if custom_message is None:
            custom_message = "No se encontro el recurso"

        detail = {
            "error": "Not Found",
            "message": custom_message
        }
        super().__init__(status_code=404, detail=detail)


class ServerErrorException(HTTPException):
    def __init__(self, custom_message=None):
        if custom_message is None:
            custom_message = "Error en el servidor, por favor intentelo de nuevo"
        detail = {
            "error": "Server Error",
            "message": custom_message
        }
        super().__init__(status_code=500, detail=detail)


class BadRequestException(HTTPException):
    class BadRequestException(HTTPException):
        def __init__(self, custom_message=None):
            if custom_message is None:
                custom_message = "Parametros incorrectos, por favor verifique \
                    la documentacion de la API"
            detail = {
                "error": "Bad Request",
                "message": custom_message
            }
            super().__init__(status_code=400, detail=detail)
