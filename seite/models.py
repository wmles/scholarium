"""
Das Grundklasse-Modell, von dem die apps der Seite erben
"""

from django.db import models
from django.template.defaultfilters import slugify

class Grundklasse(models.Model):
    bezeichnung = models.CharField(max_length=30)
    slug = models.SlugField(
        max_length=30, 
        null=False, 
        blank=True)
    zeit_erstellt = models.DateTimeField(
        auto_now_add=True,
        editable=False)
    
    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.bezeichnung)
        super(Grundklasse, self).save()

    def __str__(self):
        return str(self.bezeichnung)

    class Meta:
        abstract = True
    
