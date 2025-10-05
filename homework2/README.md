# Movie Theater Booking App using Django and the Django REST Framework
A lightweight movie seat-booking app built with Django and Django REST Framework (DRF).
It serves both JSON APIs and HTML pages (via DRF’s TemplateHTMLRenderer) without any user auth/sessions. Bookings store a simple name string.

# Features
- Movies, Seats, and Bookings CRUD operations (API)
- HTML Pages:
    - Movie List
    - Seat booking page per movie
    - Booking history with optional filter
- Viewsets and HTML actions for different pages
- Boostrap UI (templates)
