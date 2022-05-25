from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """ Create BlogForm class for Admin """

    class Meta:
        """ Update Class Meta Data """
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'blog_title': 'e.g Now that is a Mojito',
            'blog_content': 'e.g Fresh mint leaves with crushed ice',
            'author': 'Joe Bloggs',
            'image': 'Image Upload',
            'date_created': '25th of September 2022'
        }
        self.fields['blog_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder