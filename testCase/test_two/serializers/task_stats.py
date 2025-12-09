from ..models import TaskStats
from rest_framework import serializers
from django.db.models import Sum

class TaskStatsSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    
    class Meta:
        model = TaskStats
        read_only_fields = ['id', 'last_updated']
        fields =  read_only_fields + [ 'frequency', 'completed', 'task', 'person']
        depth = 1
        
    def get_completed(self, obj):
        return obj.frequency == 100 or False
    
class TaskStatsNestedSerializer(TaskStatsSerializer):
    class Meta(TaskStatsSerializer.Meta):
        depth = 0