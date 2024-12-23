from django.test import TestCase
from .models import Flight, Airports, Passenger


# Create your tests here.

class FlightTestCase(TestCase):
    def setUp(self):
        a1 = Airports.objects.create(code="AAA", city="A")
        a2 = Airports.objects.create(code="BBB", city="B")

        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)

        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airports.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airports.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_invalid_flight_destination(self):
        a1 = Airports.objects.get(code="AAA")
        # a2=Airports.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())
