from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from apps.mycountry.models import *

class User(AbstractUser):
    tel = PhoneNumberField(
        null = True, 
        blank=True, 
        verbose_name = 'Tel', 
        help_text = 'Internatinal format: +229XXXXXXXX')
    
class MyAddress(models.Model):
    
    user = models.ForeignKey(User, verbose_name="Propriétaire", on_delete=models.CASCADE)
    adresse = models.ForeignKey(Adresse, verbose_name="Adresse", on_delete=models.CASCADE)
    precision = models.TextField(verbose_name="Precision", null = True, blank = True)
    
    class Meta:
        verbose_name ="Address"
        verbose_name_plural = "Address"

    def __str__(self):
        return str(self.user)