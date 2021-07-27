from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('report/', TimeStat.as_view()),
    path('favorite/', Favorite.as_view())
]
