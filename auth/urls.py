from django.urls import path, include
from auth.views import index


urlpatterns = [
    path('', index, name='home')
]