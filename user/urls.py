from django.urls import path

from .views import Register

urlpatterns = [
    path('cadastro/', Register.as_view(), name='register')
]