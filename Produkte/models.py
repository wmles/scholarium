"""
Die Zusammenfassung aller Produkte

"""

from django.db import models
from seite.models import Grundklasse

class Produkt(Grundklasse):
    zu_veranstaltung = models.ForeignKey(
        "Veranstaltungen.Veranstaltung", 
        null=True, blank=True, 
        on_delete=models.SET_NULL)
    zu_medium = models.ForeignKey(
        "Veranstaltungen.Medium", 
        null=True, blank=True, 
        on_delete=models.SET_NULL)
    preis = models.SmallIntegerField(blank=True)
    
    @property
    def get_preis(self):
        if self.preis:
            return self.preis
        elif self.zu_veranstaltung:
            return self.zu_veranstaltung.price
        elif self.zu_medium:
            return 999
    
class KlasseMitProdukten(Grundklasse):
    def erstelle_produkt(self):
        attribut_name = 'zu_'+self.__class__.__name__.lower()
        p = Produkt(bezeichnung=self.bezeichnung)
        p.__setattr__(attribut_name, self)
        p.save()
        return None
    
    def save(self):
        self.erstelle_produkt()
    
    class Meta:
        abstract = True
    
