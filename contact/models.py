from django.db import models
from . import utils

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(blank=True)
    profile_picture = models.ImageField(upload_to=utils.pfp_handle, blank=True)
    
    def save(self, *args, **kwargs):
      try:
        this = Contact.objects.get(id=self.id)
        if this.profile_picture != self.profile_picture:
          this.profile_picture.delete(save=False)
      except:
        pass
      super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"
