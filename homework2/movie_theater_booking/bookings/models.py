from django.db import models

# Create your models here.

# movie model with title, descriptions, release date, and duration fields
class Movie(models.Model):
    title = models.CharField(max_length = 40)
    descriptions = models.CharField(max_length = 200)
    release_date = models.DateField()
    duration = models.IntegerField()

# seat model with seat number and booking status
class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.CharField(max_length = 20)

# booking model with movie, seat, user, and booking date fields
class Booking(models.Model):
    movie = models.CharField(max_length = 40)
    seat = models.IntegerField()
    user = models.CharField(max_length = 50)
    booking_date = models.DateField()
