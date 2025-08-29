from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Holiday(models.Model):
  month_number = models.IntegerField(
    default=1,
    validators=[
      MaxValueValidator(23),
      MinValueValidator(0)
    ]
  )

  used = models.FloatField(default=0)

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)