""" Microservice URLConf """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_transformers.views import MicroserviceViewSet

# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("", MicroserviceViewSet, "ms")

urlpatterns = [
    path("", include(router.urls)),
]
