from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    country = models.CharField(max_length=32, verbose_name="Страна")
    year = models.IntegerField(verbose_name="Год выпуска")
    trailer_url = models.CharField(max_length=200, verbose_name="Ссылка на трейлер")
    producer = models.TextField(verbose_name="Режиссер")
    actors = models.TextField(verbose_name="Актеры")
    age_rate = models.IntegerField(verbose_name="Возрастной рейтинг")
    release_date = models.DateField(verbose_name="Дата премьеры")
    poster = models.ImageField(verbose_name="Постер")

    def __str__(self):
        return self.title


class Hall(models.Model):
    number = models.IntegerField(verbose_name="Номер зала")

    def __str__(self):
        return str(self.number)


class Seat(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
    row_number = models.IntegerField(verbose_name="Номер ряда")
    seat_number = models.IntegerField(verbose_name="Номер места")

    def __str__(self):
        return str(self.hall.number) + " зал " + str(self.row_number) + " ряд " + str(self.seat_number) + " место"


class Session(models.Model):
    date_time = models.DateTimeField(verbose_name="Дата и время сеанса")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, verbose_name="Зал")
    price = models.IntegerField(verbose_name="Стоимость")

    def __str__(self):
        return self.movie.title + " " + str(self.date_time)


class Booking(models.Model):
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, verbose_name="Сеанс", null=True)
    booking_id = models.CharField(max_length=30, verbose_name="Код брони")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Пользователь", null=True)
    seat = models.ForeignKey(Seat, on_delete=models.SET_NULL, verbose_name="Место", null=True)

    def __str__(self):
        return self.booking_id