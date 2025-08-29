from django.shortcuts import render, redirect
from django.contrib.auth import login as logged_in
from django.urls import reverse_lazy
from holidays.models import Parameter, Holiday
from django.contrib.auth.forms import UserCreationForm

def login(request):
  return render(request, 'registration/login.html')

def sign_up(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      logged_in(request, user)

      # Initilization des mois de congés
      for month_value in range(0, 24):
        holiday = Holiday(month_number=month_value, user=user)
        holiday.save()

      # Initilization des paramètres
      parameter = Parameter(user=user)
      parameter.save()

      return redirect('home')
  else:
    form = UserCreationForm()

  return render(request, 'registration/signup.html', {'form': form})