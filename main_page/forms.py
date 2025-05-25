from django import forms
from django.forms import ModelForm
from .models import Info, Item



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('name', 'item', 'deadline', 'borrow')

        labels = {
            'name': 'Enter your name',
            'item': 'Select an item',
            'deadline': 'Enter a deadline',
            'borrow': 'Enter date when borrowed',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Name'}),
            'item': forms.Select(attrs={'class': 'form-control item-select'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'borrow': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'quantity', 'remarks']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }