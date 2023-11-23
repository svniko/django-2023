from django import forms
from django.forms import ModelForm
from .models import Flight
class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields = ['origin','destination','duration']
        # fields = '__all__'



