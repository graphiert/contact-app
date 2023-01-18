from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    contacts = models.Contact.objects.all()
    ctx = {
        'pagetitle': 'Halaman Utama',
        'contacts': contacts,
    }
    
    return render(request, 'contact/index.html', ctx)
