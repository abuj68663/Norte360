from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('video/', video, name="video"),
    path('post<int:pk>/', post_details, name="video-details"),
]