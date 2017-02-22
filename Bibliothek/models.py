"""

"""

from django.db import models
from seite.models import Grundklasse

class Buch(Grundklasse):
    titel = models.CharField(
        max_length=40,
        null=True, blank=True)
    autor = models.CharField(
        max_length=40,
        null=True, blank=True)
    isbn = models.CharField(
        max_length=40,
        null=True, blank=True)
    adresse = models.CharField(
        max_length=40,
        null=True, blank=True)
    ausgabe = models.CharField(
        max_length=40,
        null=True, blank=True)
    herausgeber = models.CharField(
        max_length=40,
        null=True, blank=True)
    serie = models.CharField(
        max_length=40,
        null=True, blank=True)
    notiz = models.CharField(
        max_length=40,
        null=True, blank=True)
    jahr = models.CharField(
        max_length=4,
        null=True, blank=True)
    sprache = models.CharField(
        max_length=3,
        null=True, blank=True)
    stichworte = models.CharField(
        max_length=200,
        null=True, blank=True)

