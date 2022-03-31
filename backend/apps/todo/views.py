"""Todo's views."""

from django.db.models import Case, When
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """Todo's main model viewset."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.annotate(
        sort_order_state=Case(When(state=False, then=0), default=1),
        sort_order_false=Case(When(state=False, then=("create_date")), default=None),
        sort_order_true=Case(When(state=True, then=("update_date")), default=None),
    ).order_by(
        "sort_order_state",
        "-sort_order_false",
        "sort_order_true",
    )
