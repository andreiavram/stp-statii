from django.contrib import admin

# Register your models here.
from statii.models import Statie

class StatieAdmin(admin.ModelAdmin):
    list_display = ["nume", "long", "lat"]

admin.site.register(Statie, StatieAdmin)
