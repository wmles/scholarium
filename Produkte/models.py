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
    zu_buechlein = models.ForeignKey(
        "Scholien.Buechlein", 
        null=True, blank=True, 
        on_delete=models.SET_NULL)
    zu_buch = models.ForeignKey(
        "Bibliothek.Buch", 
        null=True, blank=True, 
        on_delete=models.SET_NULL)
    preis = models.SmallIntegerField(blank=True, null=True)
    
    # vielleicht ist das Quatsch, weil gedoppelt mit zu_xy-Attribut
    art_choices = [('Teilnahme', )*2,
        ('Livestream', )*2,
        ('Videoaufzeichnung', )*2,
        ('Audioaufzeichnung', )*2, ]
    art_produkt = models.CharField(
        max_length=25,
        choices=art_choices,
        default='')
    
    @property
    def get_preis(self):
        if self.preis: # Achtung Preis=0 kommt nicht in diesen Ast
            print('eigener')
            return self.preis
        elif self.zu_veranstaltung:
            print('von veranstaltung')
            return self.zu_veranstaltung.get_preis()
        elif self.zu_medium:
            print('von medium')
            return self.zu_medium.get_preis()
        else:
            return 888
    
    def __str__(self):
        if self.zu_veranstaltung:
            return 'Teilnahme an {}'.format(self.zu_veranstaltung)
        elif self.zu_medium:
            return 'Medium zu {}'.format(self.zu_medium)
    
    class Meta:
        verbose_name_plural = 'Produkte'
    
class KlasseMitProdukten(Grundklasse):
    def erstelle_produkt(self):
        attribut_name = 'zu_'+self.__class__.__name__.lower()
        p = Produkt(bezeichnung=self.bezeichnung)
        p.__setattr__(attribut_name, self)
        p.save()
        return None
    
    def save(self):
        if not self.id:
            super().save()
            self.erstelle_produkt()
        else:
            super().save()
    
    class Meta:
        abstract = True
    
