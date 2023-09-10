from django.urls import path 
from .views import *


urlpatterns = [
    path('login/',login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', loguot_view, name='logout'),  
    path('register/',register_view, name='register'),
]