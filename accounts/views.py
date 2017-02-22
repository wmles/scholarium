from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from accounts.models import Kauf

class BestellungenView(ListView):
    template_name = 'warenkorb/bestellungen.html'
    context_object_name = 'bestellungen'
    def get_queryset(self):
        nutzer = self.request.user.my_profile
        return Kauf.objects.filter(nutzer=nutzer)
        
