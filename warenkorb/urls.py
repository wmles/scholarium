from django.conf.urls import url, include

from . import views
from django.views.generic.base import TemplateView

app_name = 'Warenkorb'

urlpatterns = [
    url('^$', 
        TemplateView.as_view(template_name='warenkorb/warenkorb.html'), 
        name='warenkorb'),
    url('^add$', 
        TemplateView.as_view(template_name='warenkorb/formular.html'), 
        name='add_test'),    
    url('', include('easycart.urls')),
]
