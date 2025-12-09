from ..models import People
from rest_framework import serializers
from .location import LocationNestedSerializer

class PeopleSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    locations = LocationNestedSerializer(many=True, read_only=True)
    
    class Meta:
        model = People
        fields = '__all__'
    
    def get_name(self, obj):
        return obj.get_name()
    
        
        