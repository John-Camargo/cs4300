"""
URL configuration for bookings app.

"""
from django.urls import path, include
# import viewsets from views.py
from bookings import views
# import Django router class
from rest_framework.routers import DefaultRouter


# create the router and register the Movie/Seat/Booking viewsets
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')
router.register(r'seats', views.SeatViewSet, basename='seat')
router.register(r'bookings', views.BookingViewSet, basename='booking')

# api urls will be determined automatically by the router
urlpatterns = [
    path('api/', include(router.urls)),
]
