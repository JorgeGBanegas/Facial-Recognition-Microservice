import os

from dotenv import load_dotenv
from pydantic import BaseSettings


class AwsSettings(BaseSettings):
    load_dotenv()
    check_expiration: bool = True
    jwt_header_prefix: str = "Bearer"
    jwt_header_name: str = "Authorization"
    region: str = os.getenv("AWS_REGION")
    region_2: str = os.getenv("AWS_REGION_2")
    face_collection_name: str = os.getenv("AWS_FACE_COLLECTION_NAME")
    bucket: str = os.getenv("AWS_BUCKET")
    aws_credentials: dict = {
        "aws_access_key_id": os.getenv("AWS_ACCESS_KEY_ID"),
        "aws_access_key_secret": os.getenv("AWS_SECRET_ACCESS_KEY"),
    }

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
