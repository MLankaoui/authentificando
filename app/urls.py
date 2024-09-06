from django.urls import path, include
from app.views import register_page, login_page, home_page, logout_user


urlpatterns = [
    path('', home_page, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout')
]