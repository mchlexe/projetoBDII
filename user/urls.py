from django.urls import path

from .views import Register, index, profile

urlpatterns = [
    path('cadastro/', Register.as_view(), name='register'),
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
]