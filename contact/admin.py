from django.contrib import admin
from . import models

# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
    search_fields = ['name']

admin.site.register(models.Contact, AdminContact)

