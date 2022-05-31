from django import forms
from .models import Contact_message


class ContactForm(forms.ModelForm):
    """
    Creates a contact form
    """
    class Meta:
        model = Contact_message

        fields = (
            'name',
            'email',
            'message',
        )
