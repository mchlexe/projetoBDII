from django.urls import path

from .views import Register, index

urlpatterns = [
    path('cadastro/', Register.as_view(), name='register'),
    path('', index, name='index')
]