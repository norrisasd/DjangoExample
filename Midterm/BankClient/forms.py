from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields=('name','address','birthdate','mobile_number')