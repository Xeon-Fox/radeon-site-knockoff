from django.db import models
from django.utils.translation import gettext_lazy as _

class Gpu(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название видеокарты"))
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    release_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='resources/')
    description = models.CharField(max_length=512)