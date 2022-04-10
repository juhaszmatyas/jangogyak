from django.db import models


# Create your models here.


class Diak(models.Model):
    oktatasi_azonosito = models.CharField(max_length=30)    
    nev = models.CharField(max_length=30)
    felvettek_e = models.BooleanField()

    class Meta:
        verbose_name = "Diak"
        verbose_name_plural = "Diakok"