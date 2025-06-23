"""Verify that S3 environment required for django is valid.

Key parameters we are looking to verify

Credentials:
AWS_S3_ACCESS_KEY_ID
AWS_S3_REGION_NAME
AWS_S3_SECRET_ACCESS_KEY

Bucket:
AWS_STORAGE_BUCKET_NAME
AWS_LOCATION
AWS_S3_ENDPOINT_URL
"""

import os
from typing import Any

import boto3
import boto3.session
import pytest

bucket_name: str = os.environ["AWS_STORAGE_BUCKET_NAME"]
ssl_verify: bool = bool(os.environ.get("SSL_VERIFY", "True") == "True")


@pytest.fixture()
def boto3_s3_client() -> Any:
    """Get boto3 client"""
    session = boto3.session.Session(
        aws_access_key_id=os.environ["AWS_S3_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_S3_SECRET_ACCESS_KEY"],
        region_name=os.environ["AWS_S3_REGION_NAME"],
    )
    s3 = session.client(
        service_name="s3",
        endpoint_url=os.environ["AWS_S3_ENDPOINT_URL"],
        verify=ssl_verify,
    )

    return s3


def test_can_list_objects(boto3_s3_client) -> None:
    """Test able to list objects"""
    resp = boto3_s3_client.list_objects_v2(
        Bucket=bucket_name,
    )


def test_can_put_one_object(boto3_s3_client) -> None:
    """Test able to list objects"""
    resp = boto3_s3_client.put_object(
        Bucket=bucket_name, Body=b"abcdef", Key="verify_s3.txt"
    )


def test_can_get_one_object(boto3_s3_client) -> None:
    """Test able to list objects"""
    resp = boto3_s3_client.get_object(Bucket=bucket_name, Key="verify_s3.txt")
