from django.db import models


class KlassChoices(models.TextChoices):
    FIRST = ("1", "1")
    SECOND = ("2", "2")
