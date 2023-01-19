from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import models, forms, resource, utils

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def index(request):
  if request.POST:
    keyword = request.POST['searchbox']
    contacts = models.Contact.objects.filter(name__contains=keyword)
  else:
    contacts = models.Contact.objects.all()
  ctx = {
    'pagetitle': 'Home',
    'contacts': contacts,
  }
  
  return render(request, 'contact/index.html', ctx)

@login_required(login_url=settings.LOGIN_URL)
def add(request):
  if request.POST:
    form_data = forms.ContactForm(request.POST, request.FILES)
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
      
@login_required(login_url=settings.LOGIN_URL)
def edit(request, contact_id):
  if request.POST:
    contact = models.Contact.objects.get(id=contact_id)
    form_data = forms.ContactForm(request.POST, request.FILES, instance=contact)
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

@login_required(login_url=settings.LOGIN_URL)
def delete(request, contact_id):
  contact = models.Contact.objects.get(id=contact_id)
  contact.profile_picture.delete()
  contact.delete()
  
  return redirect('contact:index')
    

@login_required(login_url=settings.LOGIN_URL)
def export(request):
  contacts = resource.ContactResource()
  dataset = contacts.export()
  response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = 'attachment; filename=mycontact.xlsx'
  return response
