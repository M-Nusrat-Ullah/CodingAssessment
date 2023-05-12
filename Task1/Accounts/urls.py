from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register, login

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
