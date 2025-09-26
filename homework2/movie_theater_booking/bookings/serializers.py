from rest_framework import serializers
from bookings.models import Movie, Seat, Booking

# create a serializer for the movie model which returns data from a movie in JSON format
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'duration']

# create a serializer for the seat model which returns seat data in JSON format
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['seat_number', 'booked']

# create a serializer for the booking model which returns booking data in JSON format
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['movie', 'seat', 'user', 'booking_date']