# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-few-public-methods
import os
import base64
import io
import boto3
from core.settings.aws_settings import AwsSettings
from core.exceptions.exceptions import NotFoundException, BadRequestException
from core.schemas.image_validate_schema import GetValidateFaceResponse


class FacialRecognitionService:

    def __init__(self):
        self.aws_settings = AwsSettings()
        self.rekognition_client = boto3.client(
            'rekognition', region_name=self.aws_settings.region,
            aws_access_key_id=self.aws_settings.aws_credentials["aws_access_key_id"],
            aws_secret_access_key=self.aws_settings.aws_credentials["aws_access_key_secret"])

    def get_image_from_s3(self, image_name):
        try:
            s3_client = boto3.client(
                's3', region_name=self.aws_settings.region_2,
                aws_access_key_id=self.aws_settings.aws_credentials["aws_access_key_id"],
                aws_secret_access_key=self.aws_settings.aws_credentials["aws_access_key_secret"])

            image = s3_client.get_object(
                Bucket=self.aws_settings.bucket, Key=image_name)

            image = io.BytesIO(image['Body'].read())

            return image
        except s3_client.exceptions.NoSuchKey as error:
            raise NotFoundException(
                'Lo siento no se encontro la imagen de referencia') from error

    def validate_face(self, images):
        try:
            reference_image = os.path.basename(images.reference_image)
            imageb64 = base64.b64decode(images.image_to_compare)
            image_to_compare = io.BytesIO(imageb64)

            image_s3 = self.get_image_from_s3(reference_image)

            response = self.rekognition_client.compare_faces(
                SourceImage={
                    'Bytes': image_s3.read()
                },
                TargetImage={
                    'Bytes': image_to_compare.read()
                },
                SimilarityThreshold=85
            )
            if len(response['FaceMatches']) == 0:
                return GetValidateFaceResponse(
                    is_valid=False,
                    similarity=0,
                    message='Lo siento no se reconocio tu rostro'
                )
            return GetValidateFaceResponse(
                is_valid=response['FaceMatches'][0]['Similarity'] >= 85,
                similarity=response['FaceMatches'][0]['Similarity'],
                message='Se reconocio tu rostro con exito'
            )
        except self.rekognition_client.exceptions.InvalidParameterException as error:
            raise BadRequestException(
                'No se encontro ninguna cara en la imagen') from error
