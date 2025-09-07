from django.db import models
from django.conf import settings

class Parameter(models.Model):
  start_holiday_amount = models.fields.FloatField(default=0)
  extra_holiday_current_year = models.fields.FloatField(default=0)
  extra_holiday_next_year = models.fields.FloatField(default=0)
  extra_holiday_month_accumulation = models.BooleanField(default=False)
  holiday_per_month = models.fields.FloatField(default=0)

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
