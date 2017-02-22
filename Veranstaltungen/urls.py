from django.conf.urls import url

from . import views
from django.views.generic.detail import DetailView
from Veranstaltungen.models import Veranstaltung

app_name = 'Veranstaltungen'

veranstaltungen_urls = [
    url(r'^$', 
        views.ListeAlle.as_view(), 
        name='liste_alle'),
    url(r'^(?P<slug>[-\w]+)/$', 
        DetailView.as_view(
            template_name='Veranstaltungen/detail.html',
            model=Veranstaltung), 
        name='veranstaltung_detail'),
    ]

salons_urls = [
    url(r'^$', 
        views.ListeAlle.as_view(), 
        {'art': 'Salon'}, name='liste_salons'),
    ]

seminare_urls = [
    url(r'^$', 
        views.ListeAlle.as_view(), 
        {'art': 'Seminar'}, name='liste_seminare'),
    ]

