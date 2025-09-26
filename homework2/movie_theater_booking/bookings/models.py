from django.db import models

# Create your models here.

# movie model with title, descriptions, release date, and duration fields
class Movie(models.Model):
    title = models.CharField(max_length = 40)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# seat model with seat number and booking status
class Seat(models.Model):
    seat_number = models.PositiveIntegerField()
    booked = models.BooleanField(default = False)

    def __str__(self):
        return f"Seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"

# booking model with movie, seat, user, and booking date fields
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete = models.CASCADE)
    user = models.CharField(max_length = 50)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.user} booked {self.seat} for {self.movie}"
