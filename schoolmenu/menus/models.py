from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Menu(TimeStampedModel):

    class DayCycle(models.TextChoices):
        MONDAY_ODD = "monday_odd", "Monday Odd Menu 1"
        TUESDAY_ODD = "tuesday_odd", "Tuesday Odd Menu 1"
        WEDNESDAY_ODD = "wednesday_odd", "Wednesday Odd Menu 1"
        THURSDAY_ODD = "thursday_odd", "Thursday Odd Menu 1"
        FRIDAY_ODD = "friday_odd", "Friday Odd Menu 1"
        MONDAY_EVEN = "monday_even", "Monday Even Menu 2"
        TUESDAY_EVEN = "tuesday_even", "Tuesday Even Menu 2"
        WEDNESDAY_EVEN = "wednesday_even", "Wednesday Even Menu 2"
        THURSDAY_EVEN = "thursday_even", "Thursday Even Menu 2"
        FRIDAY_EVEN = "friday_even", "Friday Even Menu 2"
        UNSPECIFIED = "unspecified", "Unspecified"

    day = models.CharField("Chosen Day", max_length=100,
                           choices=DayCycle.choices,
                           default=DayCycle.UNSPECIFIED)
    title = models.CharField("Title of menu", max_length=255)
    slug = AutoSlugField("Title address", unique=True, always_update=False,
                         populate_from="day")
    description = models.TextField("Description", blank=True)
    active = models.BooleanField("Active", default=False)
    image = models.ImageField("Image of the meal", upload_to='uploads/',
                              blank=True)
    celery = models.BooleanField("Celery", default=False)
    wheat = models.BooleanField("Wheat", default=False)
    crustaceans = models.BooleanField("Crustaceans", default=False)
    eggs = models.BooleanField("Eggs", default=False)
    fish = models.BooleanField("Fish", default=False)
    milk = models.BooleanField("Milk", default=False)
    lupin = models.BooleanField("Lupin", default=False)
    molluscs = models.BooleanField("Molluscs", default=False)
    mustard = models.BooleanField("Mustard", default=False)
    peanuts = models.BooleanField("Peanuts", default=False)
    sesame = models.BooleanField("Sesame", default=False)
    soybeans = models.BooleanField("Soybeans", default=False)
    sulphur_dioxide = models.BooleanField("Sulphur Dioxide and Sulphites",
                                          default=False)
    nuts = models.BooleanField("Nuts", default=False)

    def __str__(self):
        return self.title
