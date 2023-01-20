from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')
  
  def clean_email(self):
    email_value = self.cleaned_data.get('email')
    data = User.objects.filter(email__iexact=email_value).exists()
    if data == True:
      raise ValidationError('A user with that email already exists.')
  
  def save(self):
    user = super(UserCreationForm, self).save()
    user.email = self.cleaned_data.get('email')
    user.save()
    return user
