from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from holidays.forms import ParameterForm, HolidayRequestForm
from holidays.models import Parameter, Holiday
from holidays.models.enum import Month, Year
from datetime import datetime

@login_required
def home(request):
  year_query = request.GET.get('year', Year.CURRENT_YEAR)
  current_year = datetime.now().year

  # Define the target year (N or N + 1)
  target_year = current_year + 1 if year_query == Year.NEXT_YEAR else current_year

  # Récupèration des paramètres de l'utilisateur
  parameters = get_object_or_404(Parameter, user=request.user)

  # Filtre les vacances en fonction de la plage de mois
  holidays = Holiday.objects.filter(
    user=request.user,
    month_number__range=(0, 23)
  ).order_by('month_number')

  # Calcul des congés restant
  remaining_holidays = parameters.start_holiday_amount
  calculated_holidays = []

  for holiday in holidays:
    is_next_year = holiday.month_number >= 12

    if parameters.extra_holiday_month_accumulation:
      # Prise en compte des RTT N ou N + 1
      extra_holiday = parameters.extra_holiday_next_year if is_next_year else parameters.extra_holiday_current_year

      monthly_increment = (extra_holiday / 12) + parameters.holiday_per_month
    else:
      extra_holiday = (
        parameters.extra_holiday_current_year if holiday.month_number == 0
        else parameters.extra_holiday_next_year if holiday.month_number == 12
        else 0
      )

      monthly_increment = parameters.holiday_per_month + extra_holiday

    remaining_holidays += monthly_increment - holiday.used

    calculated_holidays.append({
      'month_number': holiday.month_number,
      'used': holiday.used,
      'cumulated': monthly_increment,
      'remaining': remaining_holidays
    })

  return render(request, 'holidays/home.html', {'parameters': parameters, 'calculated_holidays': calculated_holidays, 'target_year' : target_year, 'year_query': year_query})

@login_required
def parameters(request):
  # Récupèration du paramétrage de l'utilisateur courant
  parameter, created = Parameter.objects.get_or_create(user=request.user)

  if request.method == 'POST':
    form = ParameterForm(request.POST, instance=parameter)
    if form.is_valid():
      form.save()

      messages.success(request, 'Paramètrage mis à jour')
      return redirect('home')
  else:
    form = ParameterForm(instance=parameter)

  return render(request, 'holidays/parameters.html', {'form': form})

@login_required
def holiday_request(request):
  if request.method == "POST":
    form = HolidayRequestForm(request.POST)
    if form.is_valid():
      days = form.cleaned_data['days']
      month = int(form.cleaned_data['selected_month'])
      year = form.cleaned_data['selected_year']

      if year == Year.NEXT_YEAR:
        month = month + 12

      # Récupèration du mois correspondant à la demande
      month_holiday = get_object_or_404(Holiday, user=request.user, month_number=month - 1)

      month_holiday.used = days
      month_holiday.save()

      messages.success(request, 'Congés acceptés')
      return redirect('home')
  else:
    form = HolidayRequestForm()

  return render(request, 'holidays/holiday_request.html', {'form': form})