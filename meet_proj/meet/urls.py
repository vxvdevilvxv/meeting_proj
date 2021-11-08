from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('api/clients/create/', create_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('userprofile/', profile_page_view, name='profile')
]
