from django.urls import path, include
from app.views import register_page, login_page


urlpatterns = [
    path('', register_page, name='register'),
    path('login/', login_page, name='login')
]