from django.urls import path, include
from app.views import index


urlpatterns = [
    path('', index, name='home')
]