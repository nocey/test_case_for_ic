
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, PersonViewSet, TaskStatsViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')
router.register(r'person', PersonViewSet, basename='person')
router.register(r'task_stats', TaskStatsViewSet, basename='task_stats')

urlpatterns = [
    path('', include(router.urls)),
]
