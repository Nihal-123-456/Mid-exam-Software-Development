from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('detail/<int:id>/', detailpost.as_view(), name='details'),
    path('buycar/<int:id>/', buycar.as_view(), name='buycar'),
]