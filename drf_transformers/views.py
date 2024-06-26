""" Microservice API endpoints """

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework.viewsets import GenericViewSet
from transformers import pipeline
from drf_transformers import serializers

# Phi 3 Mini 4K Instruct model from HuggingFaceHub
model = pipeline(task="chat-completion", model="microsoft/Phi-3-min-4k-instruct")


# Create your views here.
class MicroserviceViewSet(GenericViewSet):
    """API endpoints for microservice"""

    def get_serializer_class(self) -> None:
        """Return different serializers for different actions"""

        match self.action:
            case "chat_completion":
                self.serializer_class = serializers.ChatCompletionSerializer

            case "question_answering":
                self.serializer_class = serializers.QuestionAnsweringSerializer

            case "text_generation":
                self.serializer_class = serializers.PromptSerializer

            case _:
                self.serializer_class = serializers.TextSerializer

        return super().get_serializer_class()

    @action(["post"], detail=False, url_path="chat-completion")
    def chat_completion(self, request: Request) -> Response:
        """A method for completing conversations using a specified language model."""

        # Serializer
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(
                serializer.error_messages,
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"result": model(**serializer.validated_data)},
            status=status.HTTP_200_OK,
        )


class RootAPIView(APIRootView):
    """Root API View that provides links to actions."""

    # Methods to remove from response
    filters = [
        "basename",
        "description",
        "detail",
        "name",
        "suffix",
        *dir(GenericViewSet),
    ]

    # URL map
    urls = {
        "text": MicroserviceViewSet,
    }

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Return urls to extra actions"""

        return Response(
            {
                k: {
                    url.replace(
                        "_",
                        "-",
                    ): f"{request.scheme}://{request.get_host()}/{k}/{url.replace('_', '-')}"
                    for url in list(
                        filter(
                            lambda f: not f.startswith("_") and f not in self.filters,
                            dir(v),
                        )
                    )
                }
                for k, v in self.urls.items()
            }
        )
