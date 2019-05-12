from django.shortcuts import render
from .models import *
import datetime
import string
import random


def index(request):
    movies = Movie.objects.all().filter(release_date__lt=datetime.date.today())
    data = {"movies": movies}
    return render(request, "core/index.html", data)


def movie_view(request):
    movie_id = request.GET["movie_id"]
    movie = Movie.objects.filter(id=movie_id).first()
    data = {"movie": movie}
    return render(request, "core/movie.html", data)


def contact(request):
    return render(request, "core/contact.html")


def movies_soon(request):
    today = datetime.date.today()
    movies = Movie.objects.all().filter(release_date__gt=today)
    data ={"movies" : movies}
    return render(request, "core/movies_soon.html", data)


def movies_today(request):
    today = datetime.date.today()
    sessions = Session.objects.all().filter(date_time__date=today).order_by("date_time")
    data = {"sessions" : sessions}
    return render(request, "core/cinema_today.html", data)


def session_view(request):
    session_id = request.GET["session_id"]
    session = Session.objects.filter(id=session_id).first()
    seats = Seat.objects.all().filter(hall=session.hall)
    data = {"session" : session, "seats": seats}
    return render(request, "core/session.html", data)

def make_book(request):
    session_id = request.GET["session_id"]
    booking = Booking()
    booking.session_id = session_id

    letters = string.ascii_lowercase
    passwd = ''.join(random.choice(letters) for i in range(15))

    booking.booking_id = passwd
    booking.save()

    data ={"booking" : booking}
    return render(request, "core/booking_ok.html", data)

