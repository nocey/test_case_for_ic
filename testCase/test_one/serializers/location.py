from rest_framework import serializers
from ..models import Location

class LocationSerializer(serializers.ModelSerializer):
    people_full_name = serializers.SerializerMethodField('get_full_name')
    
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'datetime', 'people_full_name']
        
    def get_full_name(self, obj):
        return obj.people.get_name()
    
class LocationNestedSerializer(LocationSerializer):
    class Meta(LocationSerializer.Meta):
        fields = ['id', 'latitude', 'longitude', 'datetime']