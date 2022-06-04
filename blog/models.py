from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """
    A model for blog posts which includes the user who created it,
    the blog title, an image, the blog text and when it was created.
    """

    class Meta:
        ordering = ['-created_on']

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    body_text = models.TextField(default=None, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


# Blog Comments model
class BlogComment(models.Model):
    """
    A model for blog comments on blog posts which includes the user who is
    commenting, the blog post they are commenting on, the comment itself
    and the date the comment is made"
    """

    class Meta:
        ordering = ['-created_on']

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                                  related_name='comments')
    subject = models.CharField(max_length=100, blank=True)                              
    comment = models.TextField(max_length=1000, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"Comment on {self.blog_post.title} by {self.user}"


class EditComment(models.Model):
    """ This model is for the product review and rating """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    comment = models.TextField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
