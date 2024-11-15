from django.contrib import admin
from .models import Airports,Flight,Passenger


# Register your models here.

class FlightAdmin(admin.ModelAdmin):
    list_display=["id","destination","origin"]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("flights",)

admin.site.register(Airports)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)