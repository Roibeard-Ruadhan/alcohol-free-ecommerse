from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogComment, BlogPost


class BlogCommentForm(forms.ModelForm):
    """
    Creates a blog comment form
    """

    class Meta:
        model = BlogComment

        fields = ('subject', 'comment',)



class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'body_text',
            'image',
        )

    field_order = ['title', 'body_text', 'image']

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'admin-form'
        self.fields['title'].widget.attrs['placeholder'] = 'Blog Title'
        self.fields['body_text'].widget.attrs['placeholder'] = 'Blog Content'
