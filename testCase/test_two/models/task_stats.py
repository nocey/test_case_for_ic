from django.db import models
from .task import Task
from .person import Person


class TaskStats(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='stats')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='task_stats')
    frequency = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'TaskStats: {self.person} - {self.task} ({self.frequency})'
    
    class Meta:
        unique_together = ('person', 'task')
        ordering = ['frequency']