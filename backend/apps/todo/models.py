"""Todo's models."""

from django.db import models


class Todo(models.Model):
    """Todo's table."""

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField()

    def __str__(self) -> str:
        """Display the title and the state of the todo in the admin panel."""
        return f"{self.title} - {self.state}"
