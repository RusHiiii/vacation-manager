from django.shortcuts import render, redirect
from django.contrib.auth import login as logged_in
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

def login(request):
  return render(request, 'registration/login.html')

def sign_up(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      logged_in(request, user)

      return redirect('/')
  else:
    form = UserCreationForm()

  return render(request, 'registration/signup.html', {'form': form})