from django import forms
from . models import Subscribers, SendMessage


class SubscibersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email', ]


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'