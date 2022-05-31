from django.contrib import admin
from . models import SendMessage, Subscribers

# Register your models here.
admin.site.register(SendMessage)
admin.site.register(Subscribers)
