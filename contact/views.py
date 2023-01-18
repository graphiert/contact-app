from django.shortcuts import render

# Create your views here.

def index(request):
    ctx = {
        'pagetitle': 'Halaman Utama',
    }
    
    return render(request, 'contact/index.html', ctx)
