from django.db import models
from products.models import Product
from django.contrib.auth.models import User



class Reviews(models.Model):
    """ This is for the product reviews and ratings """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.subject
