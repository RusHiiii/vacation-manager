from django import forms
from holidays.models import Parameter

class ParameterForm(forms.ModelForm):
  start_holiday_amount = forms.FloatField(max_value=100, label="Solde initial de congés")
  extra_holiday_current_year = forms.FloatField(min_value=0, max_value=20, label="Congés supplémentaires cette année")
  extra_holiday_next_year = forms.FloatField(min_value=0, max_value=20, label="Congés supplémentaires l'année prochaine")
  holiday_per_month = forms.FloatField(min_value=0, max_value=6, label="Congés acquis par mois")

  class Meta:
    model = Parameter
    exclude = ['user']