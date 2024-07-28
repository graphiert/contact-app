from django.db import models
from . import utils

# Create your models here.
class Contact(models.Model):
    # Create field
    name = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=6)
    profile_picture = models.ImageField(upload_to=utils.pfp_handle, blank=True)
    
    def save(self, *args, **kwargs):
      # Check data from id
      try:
        this = Contact.objects.get(id=self.id)
        # If the image data not same with the image, delete image (pfp changed)
        if this.profile_picture != self.profile_picture:
          this.profile_picture.delete(save=False)
      except:
        pass
      super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"
