from rest_framework import viewsets
# import Movie, Seat, and Booking models
from bookings.models import Movie, Seat, Booking
# import serializers from serializers.py to get JSON data
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer


# Create your views here.

# viewset for CRUD operations on movies
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().order_by('title')


# viewset for seat availability and booking
class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all().order_by('seat_number')


# viewset for users to book seats and view their booking histroy
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    # used ChatGPT to clean up this queryset for testing
    queryset = Booking.objects.all().select_related('movie', 'seat').order_by("-booking_date")