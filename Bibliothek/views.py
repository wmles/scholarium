from django.shortcuts import render
from django.http import HttpResponseRedirect
import re
from .models import Buch

attributnamen = {
    'author': 'autor',
    'isbn': 'isbn',
    'address': 'adresse',
    'edition': 'ausgabe',
    'publisher': 'herausgeber',
    'keywords': 'stichworte',
    'language': 'sprache',
    'note': 'notiz',
    'series': 'serie',
    'year': 'jahr'}

def aus_datei_einlesen(request, exlibris=''):
    f = open('buchliste', 'r')
    text = f.read()[6:-2]
    f.close()

    trennung = re.compile('\}\n\n(?P<name>[@, \w]*)\{')
    liste = trennung.sub('XXX', text).split('XXX')
    for buch in liste:
        zeilen = buch.split(',\n\t')
        teilsplit = re.compile(r'(\w+) = \{([^\}]+)\}')
        bezeichnung = zeilen[0]
        daten = dict(
            [tuple(teilsplit.sub(r'\1XXX\2', zeile).split('XXX')) 
            for zeile in zeilen][1:])
    
        buch = Buch.objects.create(bezeichnung=bezeichnung)
        buch.exlibris = exlibris
        for key in daten:
            if key in attributnamen:
                setattr(buch, attributnamen[key], daten[key])
        buch.save()
        
    return HttpResponseRedirect('/warenkorb/')
