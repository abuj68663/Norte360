from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('song', song, name="song"),
    path('base', base, name="base"),
    path('about', about, name="about"),
    path('promote', promote, name="promote"),
    path('crypto', crypto, name="crypto"),
    path('video', videos, name="video"),
    path('search', search, name="search"),
    path('post/<int:pk>/', post_details, name="post-details"),
]