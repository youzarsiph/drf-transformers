""" Serializers """

from rest_framework import serializers


# Create your serializers here.
class BaseSerializer(serializers.Serializer):
    """Serializer that provides model field for subclasses"""

    model = serializers.CharField(
        required=False,
        max_length=64,
        help_text="The model to use for inference. Can be a model ID hosted on the Hugging Face Hub or a URL to a deployed Inference Endpoint",
    )


class TextSerializer(BaseSerializer):
    """Serialize text input"""

    text = serializers.CharField(
        max_length=4096,
        help_text="Input text",
    )


class ChatCompletionSerializer(BaseSerializer):
    """Serialize chat completion input"""

    messages = serializers.JSONField(
        help_text="Messages represented as a JSON array, a list of dicts with role and content keys.",
    )


class QuestionAnsweringSerializer(TextSerializer):
    """Serializer question answering input"""

    question = serializers.CharField(
        max_length=256,
        help_text="Question text",
    )


class PromptSerializer(BaseSerializer):
    """Serializer for tasks that requires a prompt"""

    prompt = serializers.CharField(
        max_length=256,
        help_text="Prompt",
    )
