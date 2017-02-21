from django.conf.urls import url, include

from . import views
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from Produkte.models import Produkt
from accounts.views import BestellungenView as Bestellungen

app_name = 'Warenkorb'

urlpatterns = [
    url('^$',
        TemplateView.as_view(template_name='warenkorb/warenkorb.html'), 
        name='index'),
    url('^add$', 
        ListView.as_view(
            template_name='warenkorb/formular.html', 
            model=Produkt,
            context_object_name = 'produkte'),
        name='add_test',),
    url('^kaufen$', views.kaufen, name='kaufen'),
    url('^bestellungen$', Bestellungen.as_view(), name='bestellungen'),
    url('', include('easycart.urls')),
]
