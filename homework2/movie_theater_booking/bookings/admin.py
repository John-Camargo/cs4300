# bookings/admin.py
from django.contrib import admin
from .models import Movie, Seat, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "release_date", "duration")
    search_fields = ("title", "description")
    list_filter = ("release_date",)

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat_number", "booked")
    list_filter = ("booked",)
    search_fields = ("seat_number",)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "movie", "seat", "booking_date")
    list_filter = ("booking_date", "movie")
    search_fields = ("user",)
