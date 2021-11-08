from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('register/', create_user, name='register'),
    path('api/clients/create/', create_profile, name='create_profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
