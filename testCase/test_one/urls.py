
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, PeopleViewSet

router = DefaultRouter()
router.register(r'location', LocationViewSet, basename='location')
router.register(r'people', PeopleViewSet, basename='people')

urlpatterns = [
    path('', include(router.urls)),
]
