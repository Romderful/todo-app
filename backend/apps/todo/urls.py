"""Todo's urls."""


from rest_framework.routers import SimpleRouter
from .views import TodoViewSet


router = SimpleRouter()
router.register("", TodoViewSet, basename="todo-list")

urlpatterns = router.urls
