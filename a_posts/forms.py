from django import forms
from django.forms import ModelForm
from .models import *


class postCreateFrom(ModelForm):
    class Meta:
        model= Post
        fields = ['url','body']
        labels={ 'body' : 'caption', }
        widgets={
            'title': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Enter the title ...','class':'p-4 text-black'}),
            'image': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Add the image URL ...','class':'p-4 text-black'}),
            'body': forms.Textarea(attrs={ 'rows': 3,'placeholder':'Add the caption ...','class':'p-4 text-black'}),
            'url': forms.Textarea(attrs={'rows': 1, 'placeholder':'Add the url ...','class':'p-4 text-black'})
        }
class postCreationFrom(ModelForm):
    class Meta:
        model= Post2
        fields = ['title','image','body']
        labels={ 'body' : 'caption', }
        widgets={
            'title': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Enter the title ...','class':'p-4 text-black'}),
            'body': forms.Textarea(attrs={ 'rows': 3,'placeholder':'Add the caption ...','class':'p-4 text-black'}),
            'url': forms.Textarea(attrs={'rows': 1, 'placeholder':'Add the url ...','class':'p-4 text-black'})
        }
        
        
        
class postEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {'body': 'caption',}
        widgets = {
             'body': forms.Textarea(attrs={ 'rows': 3,'class':'p-4 text-black'}),
        }
        