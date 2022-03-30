"""Todo's views."""

from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Categories model viewset."""

    queryset = Todo.objects.all().order_by("state")
    serializer_class = TodoSerializer
