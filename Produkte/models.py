"""
Die Zusammenfassung aller Produkte

"""

from django.db import models
from seite.models import Grundklasse

class Produkt(Grundklasse):
    pass
    
class ProduktVorlage(Grundklasse):
    def erstelle_produkt(self):
        return None
    
    class Meta:
        abstract = True
    
