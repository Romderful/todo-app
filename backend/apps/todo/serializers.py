"""Todo's serializers."""

from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Todo's serializer."""

    class Meta:
        """Meta class."""

        model = Todo
        fields = "__all__"
