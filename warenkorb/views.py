from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

from easycart import BaseCart, BaseItem
from Produkte.models import Produkt
from accounts.models import Kauf


class Ware(BaseItem):
    PRICE_ATTR = 'get_preis'

class Warenkorb(BaseCart):
    item_class = Ware
    def get_queryset(self, pks):
        return Produkt.objects.filter(pk__in=pks)

def kaufen(request):
    warenkorb = Warenkorb(request)
    nutzer = request.user.my_profile
    if nutzer.guthaben < warenkorb.count_total_price():
        return HttpResponse('Guthaben reicht nicht aus!') # das schöner machen!
    
    waren = warenkorb.list_items()
    for ware in waren:
        guthaben = nutzer.guthaben
        kauf = Kauf.objects.create(
            nutzer=nutzer,
            produkt_id=ware.obj.pk,
            menge=ware.quantity,
            guthaben_davor=guthaben)
        nutzer.guthaben = guthaben - ware.total
        nutzer.save()
        warenkorb.remove(ware.obj.pk)
        
    return warenkorb.encode()
