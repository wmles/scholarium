"""
Die Modelle für Menüpunkte

 - eingegeben wird eine slug (absolut, bezüglich /) und eine nummer, die die
   Reihenfolge im Menü bestimmt
 - was wird an das Template übergeben? Vielleicht lieber eine Liste für jede 
   Nutzerkategorie erstellen? Dann fällt nummer weg. 
"""

from django.db import models
from seite.models import Grundklasse

class Menuepunkt(Grundklasse):
    sichtbar_ab = models.IntegerField(
        blank=True, 
        default=0)
    nummer = models.IntegerField(default=1)
    class Meta:
        abstract = True
        ordering = ['nummer']

class Hauptpunkt(Menuepunkt):
    pass
    
class Unterpunkt(Menuepunkt):
    gehoert_zu = models.ForeignKey(Hauptpunkt)
    def __str__(self):
        return "{} - {}".format(
            self.gehoert_zu.bezeichnung,
            self.bezeichnung)
            
