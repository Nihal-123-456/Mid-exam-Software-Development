from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('login/',user_login.as_view(),name='login'),
    path('register/',register.as_view(),name='register'),
    path('profile/',profile,name='profile'),
    path('logout/',user_logout.as_view(),name='logout'),
    path('edit/',user_edit, name='edit'),
    path('change_pass/',change_pass, name='change_pass'),
]
