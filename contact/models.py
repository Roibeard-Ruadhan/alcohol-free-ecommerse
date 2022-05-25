from django.db import models


class Contact(models.Model):
    """
    A model to create a contact message which includes
    the user, their email, the message
    & the date it's sent
    """

    class Meta:
        verbose_name_plural = 'Contact Messages'

    first_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.first_name