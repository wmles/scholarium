from django.shortcuts import render

# Create your views here.

from easycart import BaseCart
from Veranstaltungen.models import Veranstaltung


class Warenkorb(BaseCart):

    def get_queryset(self, pks):
        return Veranstaltung.objects.filter(pk__in=pks)
