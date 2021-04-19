from django.urls import path
#from .views import IndexPageView
from .views import index, municipio


urlpatterns = [
    path('', index, name='index'),
    path('<str:param>/', municipio, name='municipio'),
]