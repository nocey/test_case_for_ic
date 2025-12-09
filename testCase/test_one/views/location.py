from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Location
from django.utils import timezone
from ..serializers import LocationSerializer
from datetime import timedelta

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        now = timezone.now()
        # we need twelve hours ago from now
        twelve_hours_ago = now - timedelta(hours=12)
        
        serializer = self.get_serializer(self.get_queryset()
                                         .filter(datetime__gte=twelve_hours_ago)
                                         .order_by('people', '-datetime')
                                         .select_related('people')
                                         .distinct('people'), many=True)
        
        # if you want to different approach or better performance you can use below code 
        
        # use redis or caching mechanism to store recent locations
        # recent_locations = cache.get('recent_locations')
        # if not recent_locations:
        #     recent_locations = Location.objects.filter(
        #         datetime__gte=twelve_hours_ago
        #     ).select_related('people')
        #     cache.set('recent_locations', recent_locations, timeout=300)  # cache for 5 minutes
        # serializer = LocationSerializer(recent_locations, many=True)
        
        # We can use external databases for calculating recent locations as well (e.g., time-series databases, NoSQL databases)       
        
        return Response(serializer.data, status=status.HTTP_200_OK)