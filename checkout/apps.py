"""Imports"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """To config checkout"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
