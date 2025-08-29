from django import forms
from django.db import models
from holidays.models import Parameter
from holidays.models.enum import Year, Month

class HolidayRequestForm(forms.Form):
  days = forms.FloatField(max_value=30, label="Nombre de jours")
  selected_year = forms.ChoiceField(choices=Year.choices, label="Année", initial=Year.CURRENT_YEAR)
  selected_month = forms.ChoiceField(choices=Month.choices, label="Mois", initial=Month.JAN)