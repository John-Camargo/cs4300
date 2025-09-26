"""
URL configuration for movie_theater_booking project.

"""
from django.contrib import admin
from django.urls import path, include


# create admin url and include url patterns from bookings/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bookings.urls")),
]
