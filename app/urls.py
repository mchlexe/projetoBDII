from django.urls import path
from .views import mapView, profile


urlpatterns = [
    path('map/', mapView, name='map'),
    path('profile/', profile, name='profile'),
]