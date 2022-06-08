from django import forms
from django.core.exceptions import ValidationError
from .models import Reviews


class ReviewForm(forms.ModelForm):
    """ Review Form for products"""
    class Meta:
        model = Reviews
        fields = ['subject', 'review', 'rating']

    def clean_rating(self):
        data = self.cleaned_data['rating']
        if data < 1:
            raise ValidationError(('Please enter a rating between 1 and 5'))

        if data > 5:
            raise ValidationError(('Please enter a rating between 1 and 5'))

        return data
