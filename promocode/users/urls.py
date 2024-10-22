from django.urls import path
from .views import criar_cliente, login_cliente, logout_user

app_name = 'users'

urlpatterns = [
    path('register/', criar_cliente, name='register_user'),
    path('login/', login_cliente, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]
