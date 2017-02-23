# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from .models import *

def erstelle_liste_menue(profil=None):
    hauptpunkte = Hauptpunkt.objects.all()
    liste_punkte = []
    for punkt in hauptpunkte:
        unterpunkte = punkt.unterpunkt_set.all
        liste_punkte.append((punkt, unterpunkte))
    return liste_punkte

class ListeMitMenue(ListView):
    def get_context_data(self, **kwargs):
        liste_menue = erstelle_liste_menue(self.request.user.my_profile)
        context = super(ListeMitMenue, self).get_context_data(**kwargs)
        context['liste_menue'] = liste_menue
        return context        

class DetailMitMenue(DetailView):
    def get_context_data(self, **kwargs):
        liste_menue = erstelle_liste_menue(self.request.user)
        context = super(DetailMitMenue, self).get_context_data(**kwargs)
        context['liste_menue'] = liste_menue
        return context        
    
def index(request):
    liste_menue = erstelle_liste_menue()
    
    return render(
        request, 
        'base.html', 
        {'liste_menue': liste_menue})
    
def seite_rest(request, slug):
    punkte = (Hauptpunkt.objects.filter(slug=slug) or 
              Unterpunkt.objects.filter(slug=slug))
    if not punkte: 
        raise Http404
    liste_menue = erstelle_liste_menue()
    return render(
        request, 
        'Grundgeruest/seite_test.html', 
        {'punkt': punkte[0], 'liste_menue': liste_menue})

