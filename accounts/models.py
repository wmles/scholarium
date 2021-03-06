from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.core.validators import RegexValidator

from Produkte.models import Produkt

class ScholariumProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')
    stufe_choices = [(0, 'Interessent'),
        (1, 'Gast'),
        (2, 'Teilnehmer'),
        (3, 'Scholar'),
        (4, 'Partner'),
        (5, 'Beirat'),
        (6, 'Patron')]
    stufe = models.IntegerField(
        choices=stufe_choices,
        default=0)
    anrede = models.CharField(
        max_length=4,
        choices=[('Herr', 'Herr'), ('Frau', 'Frau')],
        default='Herr')
    tel = models.CharField(
        max_length=20,
        null=True, blank=True)
    firma = models.CharField(
        max_length=30,
        null=True, blank=True)
    strasse = models.CharField(
        max_length=30,
        null=True, blank=True)
    plz = models.CharField(
        max_length = 5,
        validators=[RegexValidator('^[0-9]+$')],
        null=True, blank=True)
    ort = models.CharField(
        max_length=30,
        null=True, blank=True)
    land = models.CharField(
        max_length=30,
        null=True, blank=True)    
    guthaben = models.IntegerField(default=0)
    kaeufe = models.ManyToManyField(
        Produkt, 
        through='Kauf', 
        editable=False)

class Kauf(models.Model):
    nutzer = models.ForeignKey(
        'ScholariumProfile', 
        on_delete=models.SET_NULL, 
        null=True)
    produkt = models.ForeignKey(
        Produkt, 
        on_delete=models.SET_NULL,
        null=True)
    menge = models.SmallIntegerField(blank=True, default=1)
    zeit = models.DateTimeField(
        auto_now_add=True,
        editable=False)
    # falls was schief geht, wird das guthaben gecached:
    guthaben_davor = models.SmallIntegerField(editable=False)

    def __str__(self):
        return 'Kauf von {}, {}: {}'.format(
            self.nutzer.user.__str__(),
            self.zeit.strftime('%x, %H:%M'),
            self.produkt.__str__())

    class Meta():
        verbose_name_plural = 'Käufe'


from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

@receiver(pre_save, sender=User)
def user_nutzername_fuellen(sender, instance, *args, **kwargs):
    instance.username = slugify(instance.email)
