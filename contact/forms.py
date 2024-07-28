from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
  # For Gender radio-button
  GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('askme', 'Ask Me'),
  )
  
  # Create radio-button
  gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
  
  # Generate forms from model
  class Meta:
    model = models.Contact
    fields = '__all__'
  
  # Check if inserted is numbers
  def clean_phone_number(self):
    # Get phone number
    try:
      phone_number = self.cleaned_data.get('phone_number')
      int(phone_number)
      return phone_number
    # Return error if not numbers
    except ValueError:
      raise ValidationError('Can only contain numbers.')
  
  # Check if there is a same name
  # def clean_name(self):
  #   # Get name
  #   name = self.cleaned_data.get('name')
  #   name_value = name.lower()
  #   # Check name that same from form that inputed by user
  #   data = models.Contact.objects.filter(name__iexact=name_value)
  #   # If data edited, let name same (exclude the name so there isn't have any data)
  #   if self.instance:
  #     data = data.exclude(pk=self.instance.pk)
  #   else:
  #     data = data
  #   # If data exist, show an error, else continue the logic
  #   if data.exists() == True:
  #     raise ValidationError(f'{name} is already exists.')
  #   else:
  #     return name

