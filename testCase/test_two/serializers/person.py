from ..models import Person
from rest_framework import serializers
from .task_stats import TaskStatsNestedSerializer
from django.db.models import Sum

class PersonSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    
    task_stats = TaskStatsNestedSerializer(many=True, read_only=True)
    
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'completed', 'task_stats']
        depth = 0
        
    def get_completed(self, obj):
        return obj.task_stats.aggregate(completed=Sum('frequency')).get('completed') == 100 or False