from django.urls import path
#from .views import IndexPageView
from .views import mapView


urlpatterns = [
    path('map/', mapView, name='map'),
    #path('register/', register, name='register'),
    # path('login/', login, name='login'),
    #path('<str:param>/', municipio, name='municipio'),
]