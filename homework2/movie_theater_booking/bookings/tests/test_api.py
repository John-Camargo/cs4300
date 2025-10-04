"""
This file is used for unit testing. Used ChatGPT to create 90% this file
"""

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import date
from bookings.models import Movie, Seat, Booking


class TestApiEndpoints(TestCase):
    def setUp(self):
        self.api = APIClient()
        # for the HTML-rendered actions
        self.web = Client()

        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Through a wormhole.",
            release_date=date(2014, 11, 7),
            duration=169,
        )
        self.seat = Seat.objects.create(seat_number=7, booked=False)

    # testing JSON from API and API endpoints

    def test_movies_list_json(self):
        # testing /api/movies/
        url = reverse("movie-list")
        r = self.api.get(url)
        # test response/status code and ensure JSON returned as list with proper values
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), list)
        self.assertIn(
            {"title", "description", "release_date", "duration"},
            [set(d.keys()) for d in r.json()]
        )

    def test_create_movie_json(self):
        url = reverse("movie-list")
        payload = {
            "title": "The Matrix",
            "description": "There is no spoon.",
            "release_date": "1999-03-31",
            "duration": 136,
        }
        r = self.api.post(url, payload, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertTrue(Movie.objects.filter(title="The Matrix").exists())

    def test_seats_list_json(self):
        # testing /api/seats/
        url = reverse("seat-list")           
        r = self.api.get(url)
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertIsInstance(body, list)
        self.assertIn("seat_number", body[0])

    def test_create_booking_json(self):
        # testing /api/bookings/
        url = reverse("booking-list")        
        today = date.today().isoformat()
        payload = {
            "movie": self.movie.pk,
            "seat": self.seat.pk,
            "user": "Bob",
            "booking_date": today,
        }
        r = self.api.post(url, payload, format="json")
        self.assertEqual(r.status_code, 201)
        self.assertTrue(Booking.objects.filter(user="Bob").exists())
        # Note: API create does NOT flip seat.booked; only the HTML action does.
        self.seat.refresh_from_db()
        self.assertFalse(self.seat.booked)

    # HTML actions (from TemplateHTMLRenderer)

    def test_movie_ui_html(self):
        # testing /api/movies/ui/
        url = reverse("movie-ui")            
        r = self.web.get(url, HTTP_ACCEPT="text/html")
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "bookings/movie_list.html")
        self.assertIn("movies", r.context)

    def test_movie_book_get_html(self):
        # testing /api/movies/<id>/book/
        url = reverse("movie-book", kwargs={"pk": self.movie.pk})  
        r = self.web.get(url, HTTP_ACCEPT="text/html")
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "bookings/seat_booking.html")
        self.assertEqual(r.context["selected_movie"].pk, self.movie.pk)

    def test_movie_book_post_creates_booking_and_redirects(self):
        url = reverse("movie-book", kwargs={"pk": self.movie.pk})
        r = self.web.post(url, {"seat_id": self.seat.pk, "user": "John"})
        # HTML action redirects to booking-ui on success
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, reverse("booking-ui"))
        # Booking created
        self.assertTrue(Booking.objects.filter(user="John", movie=self.movie, seat=self.seat).exists())
        # Seat flipped to booked by the HTML action
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booked)

    def test_booking_ui_html_and_filter(self):
        # seed two bookings
        Booking.objects.create(movie=self.movie, seat=self.seat, user="Zoe", booking_date=date.today())
        another_seat = Seat.objects.create(seat_number=8, booked=False)
        Booking.objects.create(movie=self.movie, seat=another_seat, user="Max", booking_date=date.today())

        # /api/bookings/ui/
        url = reverse("booking-ui")  
        r = self.web.get(url + "?q=Zoe", HTTP_ACCEPT="text/html")
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, "bookings/booking_history.html")
        # Ensure only Zoe appears in filtered context
        ctx_users = {b.user for b in r.context["bookings"]}
        self.assertEqual(ctx_users, {"Zoe"})

