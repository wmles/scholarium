from django.shortcuts import render

# Create your views here.

from easycart import BaseCart, BaseItem
from Produkte.models import Produkt


class Ware(BaseItem):
    PRICE_ATTR = 'get_preis'

class Warenkorb(BaseCart):
    item_class = Ware
    def get_queryset(self, pks):
        return Produkt.objects.filter(pk__in=pks)
        
    
