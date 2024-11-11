from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User





class InboxMessagesForm(ModelForm):
    class Meta:
        model = InboxMessage
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control','column':1, 'placeholder': 'Add Message... ','rows': 4,}),
        }
            
        
    