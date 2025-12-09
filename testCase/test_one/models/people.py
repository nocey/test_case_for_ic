from django.db import models
from rest_framework import serializers

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['first_name', 'last_name']
        
    def get_name(self):
        return f'{self.first_name} {self.last_name}'