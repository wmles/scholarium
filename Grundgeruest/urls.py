from django.conf.urls import url

from . import views
from Veranstaltungen import views as views_veranstaltungen

app_name = 'Grundgeruest'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^veranstaltungen/$', 
        views_veranstaltungen.ListeAlle.as_view(), 
        name='liste_alle'),
    url(r'^salon/$', 
        views_veranstaltungen.ListeArt.as_view(), 
        {'art': 'Salon'}, name='liste_salons'),
    url(r'^seminare/$', 
        views_veranstaltungen.ListeArt.as_view(), 
        {'art': 'Seminar'}, name='liste_seminare'),
    url(r'^(?P<slug>[\w-]+)/$', views.seite_rest, name='seite_rest'),
]
