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
      
def edit(request, contact_id):
  if request.POST:
    contact = models.Contact.objects.get(id=contact_id)
    form_data = forms.ContactForm(request.POST, instance=contact)
    if form_data.is_valid():
      form_data.save()
      return redirect('contact:index')
  else:
    contact = models.Contact.objects.get(id=contact_id)
    form = forms.ContactForm(instance=contact)
    ctx = {
      'pagetitle': 'Add Contact',
      'contact': contact,
      'form': form,
    }
    return render(request, 'contact/edit.html', ctx)

def delete(request, contact_id):
  contact = models.Contact.objects.get(id=contact_id)
  contact.delete()
  
  return redirect('contact:index')
    
