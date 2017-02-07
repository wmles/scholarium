"""
Die Modelle der Veranstaltungen

 - die ArtDerVeranstaltung speichert gemeinsame Attribute - überdenken, falls
   z.B. konkrete Anlässe andere Kosten haben sollen.
"""

from django.db import models
from seite.models import Grundklasse
from Produkte.models import KlasseMitProdukten
import random, string

class ArtDerVeranstaltung(Grundklasse):
    beschreibung = models.TextField(
        max_length=1200, 
        null=True, blank=True)    
    preis_praesenz = models.SmallIntegerField()
    preis_livestream = models.SmallIntegerField(null=True, blank=True)
    preis_aufzeichnung = models.SmallIntegerField(null=True, blank=True)
    max_teilnehmer = models.SmallIntegerField(null=True, blank=True)
    zeit_beginn = models.TimeField()
    zeit_ende = models.TimeField()
    class Meta:
        verbose_name_plural = "Arten der Veranstaltungen"
    
class Veranstaltung(KlasseMitProdukten):
    beschreibung = models.TextField(max_length=2000)
    datum = models.DateField()
    art_veranstaltung = models.ForeignKey(ArtDerVeranstaltung)
    class Meta:
        verbose_name_plural = "Veranstaltungen"
    @property
    def price(self):
        return self.art_veranstaltung.preis_praesenz
    
class Medium(KlasseMitProdukten):
    gehoert_zu = models.ForeignKey(Veranstaltung, null=True, blank=True)
    datei = models.FileField()
    # folgendes v.a. relevant wenn keine Veranstaltung verknüpft ist:
    typ = models.CharField(max_length=30, null=True, blank=True)
    beschreibung = models.TextField(max_length=2000, null=True, blank=True)
    datum = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Medien"
    
    def __str__(self):
        return '{}: {}'.format(self.bezeichnung, self.slug) 
        
    def save(self):
        self.beschreibung = self.beschreibung or self.gehoert_zu.beschreibung
        self.bezeichnung = self.bezeichnung or self.gehoert_zu.bezeichnung
        self.typ = self.typ or self.gehoert_zu.art_veranstaltung
        self.datum = self.datum or self.gehoert_zu.datum
        if not self.pk:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 12))
        super().save()
        
