from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.

def index(request):
  contacts = models.Contact.objects.all()
  ctx = {
    'pagetitle': 'Home',
    'contacts': contacts,
  }
  
  return render(request, 'contact/index.html', ctx)

def add(request):
  if request.POST:
    form_data = forms.ContactForm(request.POST)
    if form_data.is_valid():
      form_data.save()
      return redirect('contact:index')
  else:
    form = forms.ContactForm()
    ctx = {
      'pagetitle': 'Add Contact',
      'form': form,
    }
    return render(request, 'contact/add.html', ctx)
      
