""" Microservice URLConf """

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_transformers.views import MicroserviceViewSet, RootAPIView

# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("", MicroserviceViewSet, "ms")

# Customize API root view
router.APIRootView = RootAPIView

urlpatterns = [
    path("", include(router.urls)),
]
