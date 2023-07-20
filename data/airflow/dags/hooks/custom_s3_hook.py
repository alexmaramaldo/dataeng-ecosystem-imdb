import boto3
import os

from airflow.hooks.base import BaseHook
from airflow.models import Variable
from requests.models import Response


class CustomS3Hook(BaseHook):
    def __init__(self, bucket: str, **kwargs) -> None:
        super().__init__()
        self.bucket = bucket
        if Variable.get('AWS_ENDPOINT') == 'null':
            self.client = boto3.client('s3',
               aws_access_key_id=Variable.get('AWS_ACCESS_KEY_ID'),
               aws_secret_access_key=Variable.get('AWS_SECRET_ACCESS_KEY'),
               aws_session_token=None,
               config=boto3.session.Config(signature_version='s3v4'),
               verify=False,
               region_name=Variable.get('AWS_DEFAULT_REGION')
               )

        else:
            self.client = boto3.client('s3',
               aws_access_key_id=Variable.get('AWS_ACCESS_KEY_ID'),
               aws_secret_access_key=Variable.get('AWS_SECRET_ACCESS_KEY'),
               aws_session_token=None,
               endpoint_url=Variable.get('AWS_ENDPOINT'),
               config=boto3.session.Config(signature_version='s3v4'),
               verify=False,
               region_name=Variable.get('AWS_DEFAULT_REGION')
               )


    def put_object(self, key: str, buffer):
        print("XXXXXXXXXXXXXXXXX")
        print(self.bucket, Variable.get('AWS_ENDPOINT'), Variable.get('AWS_DEFAULT_REGION'), Variable.get('AWS_ACCESS_KEY_ID'), Variable.get('AWS_SECRET_ACCESS_KEY'))
        print("XXXXXXXXXXXXXXXXX")
        self.client.put_object(Body=buffer, Bucket=self.bucket, Key=f"{key}")


    def get_object(self, key: str):
        response = self.client.get_object(Bucket=self.bucket, Key=key)
        return response.get("Body")
