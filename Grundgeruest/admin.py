from django.contrib import admin

# Register your models here.

from .models import *

class UnterpunktInline(admin.TabularInline):
    model = Unterpunkt
    fields = ('bezeichnung', 'slug')
    extra = 1

class HauptpunktAdmin(admin.ModelAdmin):
    inlines = [UnterpunktInline]

admin.site.register(Hauptpunkt, HauptpunktAdmin)
admin.site.register(Unterpunkt)


