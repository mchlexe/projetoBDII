from django.urls import path
#from .views import IndexPageView
from .views import index, municipio, register


urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    #path('<str:param>/', municipio, name='municipio'),
]