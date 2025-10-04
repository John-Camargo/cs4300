"""
URL configuration for movie_theater_booking project.

"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- add this



# create admin url and include url patterns from bookings/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bookings.urls")),
    path('', RedirectView.as_view(pattern_name='movie-ui', permanent=False)),
]
