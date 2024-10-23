from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model =GroupMessage
        fields = ['body']
        widgets = {
            "body": forms.TextInput(attrs={'placeholder':'Add messages .....','class':'p-4 text-black','maxlength':'300','autofocus':True}),
                }
        

class NewGroupChat(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']

        widgets = {
            "groupchat_name": forms.TextInput(attrs={'placeholder':'Add group name .....','class':'p-4 text-black','maxlength':'300','autofocus':True
                                                     }),
        }


class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            "groupchat_name": forms.TextInput(attrs={
                'placeholder':'Add group name .....',
                'class':'p-4 text-xl font-bold mb-4',
                'maxlength':'300',
            }),
        }
