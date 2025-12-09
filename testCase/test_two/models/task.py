from django.db import models
from .person import Person

class Task (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']