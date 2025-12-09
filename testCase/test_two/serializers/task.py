from rest_framework import serializers
from ..models import Task
from .task_stats import TaskStatsSerializer
from django.db.models import Avg

class TaskSerializer(serializers.ModelSerializer):
    frequency = serializers.SerializerMethodField()
    
    stats = TaskStatsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description' , 'frequency', 'stats']
        depth = 1

    def get_frequency(self, obj):
        return obj.stats.aggregate(
            frequency=Avg('frequency')
        ).get('frequency') or 0