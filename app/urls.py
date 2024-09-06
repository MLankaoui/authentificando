from django.urls import path, include
from app.views import register_page


urlpatterns = [
    path('', register_page, name='register')
]