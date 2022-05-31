from django.contrib import admin
from .models import Contact_message


class ContactAdmin(admin.ModelAdmin):
    """
    Setup Contact section as viewed in Admin Panel
    """

    list_display = (
        'name',
        'email',
        'message',
        'date',
    )

    readonly_fields = (
        'name',
        'email',
        'message',
        'date',
    )

    search_fields = (
        'message',
        'name',
    )

    ordering = ['-date']


admin.site.register(Contact_message, ContactAdmin)