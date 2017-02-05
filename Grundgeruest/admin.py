from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Hauptpunkt)
admin.site.register(Unterpunkt)

