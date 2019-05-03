from django.contrib import admin

from .models import *

admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(Booking)