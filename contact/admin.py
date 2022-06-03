from django.contrib import admin
from .models import contact_message

# Register your models here.


class contactMessage(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'message',
    )


admin.site.register(contact_message, contactMessage)