from rest_framework import viewsets
# import Movie, Seat, and Booking models
from bookings.models import Movie, Seat, Booking
# import serializers from serializers.py to get JSON data
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer

# added imports for DRF HTML actions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone

# Create your views here.

# viewset for CRUD operations on movies
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all().order_by('title')

    # ChatGPT generated additions to account for html actions
    # --- HTML "Now Playing" page (no auth/sessions) ---
    @action(detail=False, methods=["get"], renderer_classes=[TemplateHTMLRenderer], url_path="ui")
    def ui(self, request):
        movies = Movie.objects.all().order_by("title")
        return Response({"movies": movies}, template_name="bookings/movie_list.html")

    # --- Seat selection + booking for a single movie (GET page + POST submit) ---
    @action(detail=True, methods=["get", "post"], renderer_classes=[TemplateHTMLRenderer], url_path="book")
    def book(self, request, pk=None):
        movie = get_object_or_404(Movie, pk=pk)

        if request.method.lower() == "post":
            seat_id = request.data.get("seat_id")
            user_name = (request.data.get("user") or "").strip()

            if not seat_id:
                # Re-render seat page with an inline error (no messages framework needed)
                seats = Seat.objects.all().order_by("seat_number")
                return Response(
                    {
                        "selected_movie": movie,
                        "movies": Movie.objects.all().order_by("title"),
                        "seats": seats,
                        "form_error": "Please select a seat."
                    },
                    template_name="bookings/seat_booking.html",
                    status=status.HTTP_400_BAD_REQUEST,
                )

            seat = get_object_or_404(Seat, pk=seat_id)

            if seat.booked:
                seats = Seat.objects.all().order_by("seat_number")
                return Response(
                    {
                        "selected_movie": movie,
                        "movies": Movie.objects.all().order_by("title"),
                        "seats": seats,
                        "form_error": f"Seat {seat.seat_number} is already booked."
                    },
                    template_name="bookings/seat_booking.html",
                    status=status.HTTP_409_CONFLICT,
                )

            # Create booking
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=user_name or "Guest",
                booking_date=timezone.now().date(),
            )

            # Mark seat as booked globally (to match Seat model's boolean)
            seat.booked = True
            seat.save()

            # Redirect to booking history UI (DRF action)
            return redirect("booking-ui")

        # GET: render the seat grid for this movie (no sessions, no accounts)
        seats = Seat.objects.all().order_by("seat_number")
        return Response(
            {
                "selected_movie": movie,
                "movies": Movie.objects.all().order_by("title"),
                "seats": seats,
            },
            template_name="bookings/seat_booking.html",
        )


# viewset for seat availability and booking
class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all().order_by('seat_number')


# viewset for users to book seats and view their booking histroy
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    # used ChatGPT to clean up this queryset for testing
    queryset = Booking.objects.all().select_related('movie', 'seat').order_by("-booking_date")

    # --- HTML booking history (no sessions) ---
    @action(detail=False, methods=["get"], renderer_classes=[TemplateHTMLRenderer], url_path="ui")
    def ui(self, request):
        q = (request.GET.get("q") or "").strip()
        bookings = self.get_queryset()
        if q:
            bookings = bookings.filter(user__icontains=q)
        return Response({"bookings": bookings}, template_name="bookings/booking_history.html")