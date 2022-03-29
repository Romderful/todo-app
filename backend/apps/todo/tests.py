"""Todo's tests."""

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoViewsetTestCase(APITestCase):
    """Todo's tests."""

    def setUp(self):
        """Set up config.

        Create a task.
        """
        Todo.objects.create(
            id=1,
            title="Task 1",
            description="First task",
            state=True,
        )

        Todo.objects.create(
            id=2,
            title="Task 2",
            description="Second task",
            state=False,
        )

    def test_retrieve_todo_list(self):
        """Test that all the todos are correctly returned."""
        response = self.client.get("/api-v1/todos/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Todo with id 1
        self.assertEqual(response.data[0]["title"], "Task 1")
        self.assertEqual(response.data[0]["description"], "First task")
        self.assertEqual(response.data[0]["state"], True)
        # Todo with id 2
        self.assertEqual(response.data[1]["title"], "Task 2")
        self.assertEqual(response.data[1]["description"], "Second task")
        self.assertEqual(response.data[1]["state"], False)

    def test_retrieve_todo_detail(self):
        """Test that a specific todo's detail is correctly returned."""
        response = self.client.get("/api-v1/todos/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Task 1")
        self.assertEqual(response.data["description"], "First task")
        self.assertEqual(response.data["state"], True)
