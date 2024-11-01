from django import forms
from django.forms import ModelForm
from .models import *


class postCreateFrom(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['url','body']
        labels={ 'body' : 'caption',
                'tags':'Category'}
        widgets={
            'title': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Enter the title ...','class':'p-4 text-black'}),
            'image': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Add the image URL ...','class':'p-4 text-black'}),
            'body': forms.Textarea(attrs={ 'rows': 3,'placeholder':'Add the caption ...','class':'p-4 text-black'}),
            'url': forms.Textarea(attrs={'rows': 1, 'placeholder':'Add the url ...','class':'p-4 text-black'}),
             "tags": forms.CheckboxSelectMultiple(),
        }
class postCreationFrom(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['title','images','body']
        labels={ 'body' : 'caption',
                  'tags':'Category'}
        widgets={
            "tags": forms.CheckboxSelectMultiple(),
            'title': forms.Textarea(attrs={ 'rows': 1,'placeholder':'Enter the title ...','class':'p-4 text-black'}),
            'body': forms.Textarea(attrs={ 'rows': 3,'placeholder':'Add the caption ...','class':'p-4 text-black'}),
            'url': forms.Textarea(attrs={'rows': 1, 'placeholder':'Add the url ...','class':'p-4 text-black'})
        }
        
        
        
class postEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body',]
        labels = {'body': 'caption',
                    'tags':'Category'}
        widgets = {
             'body': forms.Textarea(attrs={ 'rows': 3,'class':'p-4 text-black'}),
               "tags": forms.CheckboxSelectMultiple(),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
             'body': forms.Textarea(attrs={'rows': 1,'placeholder':'Add comment ...' }),
        }
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
             'body': forms.Textarea(attrs={'rows': 1,'placeholder':'Add Reply ...','class':'text-sm' }),
        }
        