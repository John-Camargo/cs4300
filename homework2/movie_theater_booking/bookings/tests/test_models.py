"""
This file is used for unit testing. Was guided by ChatGPT to create test class and test data
"""

from django.test import TestCase
from datetime import date
from bookings.models import Movie, Seat, Booking


# test class which ChatGPT helped me create, makes test data and tells Django what/how to test
class TestModelStr(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.movie = Movie.objects.create(
            title="Inception",
            description="Dreams within dreams.",
            release_date=date(2010, 7, 16),
            duration=148,
        )
        cls.seat = Seat.objects.create(seat_number=1, booked=False)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Inception")

    def test_seat_str_available(self):
        self.assertEqual(str(self.seat), "Seat 1 - Available")

    def test_seat_str_booked(self):
        self.seat.booked = True
        self.seat.save()
        self.assertEqual(str(self.seat), "Seat 1 - Booked")

    def test_booking_str(self):
        b = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user="John",
            booking_date=date.today(),
        )
        # __str__ uses the current seat state; our seat is available here
        self.assertEqual(str(b), "John booked Seat 1 - Available for Inception")
