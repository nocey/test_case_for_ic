from rest_framework import viewsets
from ..models import TaskStats
from ..serializers import TaskStatsSerializer

class TaskStatsViewSet(viewsets.ModelViewSet):
    queryset = TaskStats.objects.all()
    serializer_class = TaskStatsSerializer
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related('task', 'person')