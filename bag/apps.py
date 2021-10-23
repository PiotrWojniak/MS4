"""App configuration"""
from django.apps import AppConfig


class BagConfig(AppConfig):
    """Default config for Bag"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
