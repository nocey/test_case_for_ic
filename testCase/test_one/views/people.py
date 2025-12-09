from ..models import People,Location
from ..serializers import PeopleSerializer,LocationNestedSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    @action(detail=True, methods=['get'])
    def recent_locations(self, request, pk=None):
        locations = Location.objects.filter(people=pk)
        location_serializer = LocationNestedSerializer(locations, many=True)
        
        # if you want to different approach or better performance you can use below code 
        
        # redis use case
        # locations = cache.get(f'recent_locations:people:{pk}')
        # if not recent_locations:
        #     locations = Location.objects.filter(
        #         datetime__gte=twelve_hours_ago
        #     ).select_related('people')
        #     cache.set('recent_locations', recent_locations, timeout=300)  # cache for 5 minutes
        
        
        return Response(location_serializer.data)