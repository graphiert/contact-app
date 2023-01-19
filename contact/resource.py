from import_export import resources, fields
from . import models

class ContactResource(resources.ModelResource):
  name = fields.Field(attribute='name', column_name='Name')
  phone_number = fields.Field(attribute='phone_number', column_name='Phone Number')
  
  class Meta:
    model = models.Contact
    fields = ('name', 'phone_number')