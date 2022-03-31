"""Todo's models."""

from django.db import models


class Todo(models.Model):
    """Todo's table."""

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    state = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Display the title and the state of the todo in the admin panel."""
        return f"{self.title} - {self.state}"
