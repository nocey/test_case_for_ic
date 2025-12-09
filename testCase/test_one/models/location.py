from django.db import models
from .people import People

class Location(models.Model):   
    people = models.ForeignKey(People, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-datetime']
        # for better performance on queries filtering by people and datetime
        indexes = [
            models.Index(fields=['people', '-datetime']), 
            models.Index(fields=['datetime']),
        ]