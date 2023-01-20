from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
  class Meta:
    model = models.Contact
    fields = '__all__'
    
  def clean_name(self):
    name = self.cleaned_data.get('name')
    name_value = name.lower()
    data = models.Contact.objects.filter(name__iexact=name_value).exists()
    if data == True:
      raise ValidationError(f'{name} is already exists.')
