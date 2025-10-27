# restaurant/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class Booking(models.Model):
    name = models.CharField(max_length=255)
    # int(6) in SQL ≈ up to 6 digits; use validators (no max_length for IntegerField)
    no_of_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999)]
    )
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} @ {self.booking_date:%Y-%m-%d %H:%M}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # decimal(10,2)
    # int(5) in SQL ≈ up to 5 digits
    inventory = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99999)]
    )

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
