"""
Production Utilities
"""
from django.core.files.storage import storages
from storages.backends.s3 import S3Storage
from horilla import settings


def generate_static_url(asset_path: str) -> str:
    """Generates a static URL based on the type of Django storage

    Args:
        asset_path: The path of the asset to fetch.

    Returns:
        The static URL path
    """
    staticstorage = storages.get("staticfiles")
    # If not specified or not a S3 storage, we are serving from DEBUG mode.
    if not isinstance(staticstorage, S3Storage):
        #static_url: str = getattr(settings, "STATIC_URL", lambda: None)
        static_url: str = getattr(settings, "STATIC_URL") if hasattr(settings, "STATIC_URL") else "static/"
        return f"/{static_url}{asset_path}"
    # Make S3 Path
    s3_url: str = staticstorage.url(asset_path)
    return s3_url
