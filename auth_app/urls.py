from django.urls import path
from .views import register, login, refresh_token, update

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('refresh-token/', refresh_token, name='refresh-token'),
    path('update/', update, name='update')
]