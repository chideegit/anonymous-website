from django import forms 
from .models import AnonMessage

class AddAnonMessageForm(forms.ModelForm):
    class Meta:
        model = AnonMessage
        fields = ['message']