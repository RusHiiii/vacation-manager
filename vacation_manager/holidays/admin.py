from django.contrib import admin
from .models import Parameter, Holiday

class ParameterAdmin(admin.ModelAdmin):
  list_display = ("id", "start_holiday_amount", "extra_holiday_current_year", "extra_holiday_next_year", "holiday_per_month", "user")

class HolidayAdmin(admin.ModelAdmin):
  list_display = ("id", "user")

admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Holiday, HolidayAdmin)