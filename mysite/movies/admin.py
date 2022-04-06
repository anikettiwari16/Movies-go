from django.contrib import admin
from .models import Movie,Theater,City,Booking
# Register your models here.

admin.site.register(Movie)
admin.site.register(Booking)
admin.site.register(Theater)
admin.site.register(City)