from django.urls import path
from .views import mapView


urlpatterns = [
    path('map/', mapView, name='map'),
]