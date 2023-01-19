from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
  if request.POST:
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('contact:index')
    else:
      return redirect('signup')
  else:
    form = UserCreationForm()
    ctx = {
      'pagetitle': 'Sign Up',
      'form': form,
    }
    return render(request, 'registration/signup.html', ctx)