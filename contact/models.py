from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.name}"
