from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView

from .models import *
from Grundgeruest.views import erstelle_liste_menue

class ListeAlle(ListView):
    """ Stellt Liste aller Veranstaltungen dar
    """
    template_name = 'Veranstaltungen/liste_alle.html'
    context_object_name = 'veranstaltungen'
    paginate_by = 2
    model = Veranstaltung    
            
    def get_context_data(self, **kwargs):
        context = super(ListeAlle, self).get_context_data(**kwargs)
        context['liste_menue'] = erstelle_liste_menue()
        return context

class ListeArt(ListeAlle):
    """ Stellt Liste der Seminare oder Salons dar
    """
    template_name = 'Veranstaltungen/liste_art.html'
    paginate_by = 2
    def get_queryset(self, **kwargs):
        art_name = self.kwargs['art']
        art = get_object_or_404(ArtDerVeranstaltung, bezeichnung=art_name)
        return Veranstaltung.objects.filter(
            art_veranstaltung=art)
    
