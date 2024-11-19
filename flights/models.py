from django.db import models


# Create your models here.


class Airports(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def is_valid_flight(self):
        return self.origin != self.destination or self.duration >= 100

    def __str__(self) -> str:
        return f"{self.id} {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self) -> str:
        return f"{self.first} {self.last}"
