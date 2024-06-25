from django import forms
from django.forms import ModelForm
from .models import Info

# Form to enter info into database
class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ('name', 'item', 'deadline', 'borrow')

        labels = {
            'name': '',
            'item': '',
            'deadline': 'Enter a deadline',
            'borrow': 'Enter date when borrowed',
        }


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Name'}),
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter borrowed item '}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type':'date','placeholder':'Enter deadline to return'}),
            'borrow': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder':'Enter date when borrowed'}),
        }

       