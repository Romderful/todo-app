"""Apps."""

from django.apps import AppConfig


class TodoConfig(AppConfig):
    """Todo's app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.todo"
