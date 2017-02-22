from django.conf.urls import url

from . import views, models
from django.views.generic.list import ListView

app_name = 'Veranstaltungen'

urlpatterns = [
    url(r'^$', 
        ListView.as_view(
            template_name='Bibliothek/liste_alle.html',
            model=models.Buch,
            context_object_name='buecher',
        ), 
        name='liste_alle'),
    url('^aus_datei_einlesen$', views.aus_datei_einlesen, name='einlesen'),
    ]

