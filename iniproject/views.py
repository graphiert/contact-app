from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from . import forms

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
  error = None
  if request.POST:
    form = forms.SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, f"Successfully created { request.POST['username'] }!")
      return redirect('contact:index')
    else:
      messages.error(request, "Something went wrong...")
      error = form.errors
  form = forms.SignUpForm()
  ctx = {
      'pagetitle': 'Sign Up',
      'h1_data': 'Sign Up',
      'error': error,
      'form': form,
  }
  return render(request, 'registration/signup.html', ctx)