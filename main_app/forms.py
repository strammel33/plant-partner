from django.forms import ModelForm
from .models import Caring

class CaringForm(ModelForm):
  class Meta:
    model = Caring
    fields = ['date', 'care']