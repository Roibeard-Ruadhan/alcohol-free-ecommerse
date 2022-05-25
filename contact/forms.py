from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Creates a contact form
    """
    class Meta:
        model = Contact

        fields = (
            'first_name',
            'email',
            'message',
        )
