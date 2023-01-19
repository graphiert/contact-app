import re
from django.core.exceptions import ValidationError
from . import models

def exists_name(value):
  name_value = value.lower()
  data = models.Contact.objects.filter(name__iexact=name_value).exists()
  if data == True:
    raise ValidationError(f'{value} is already exists.')
