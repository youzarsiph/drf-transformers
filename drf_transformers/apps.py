""" Microservice AppConf """

from django.apps import AppConfig


# Create your AppConf here.
class DrfTransformersConfig(AppConfig):
    """App configuration for microservice"""

    name = "drf_transformers"
    default_auto_field = "django.db.models.BigAutoField"
