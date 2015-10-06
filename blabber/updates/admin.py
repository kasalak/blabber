from django.contrib import admin
from .models import Status, Favorite

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'text']

# Register your models here.
admin.site.register(Status, StatusAdmin)
admin.site.register(Favorite)
