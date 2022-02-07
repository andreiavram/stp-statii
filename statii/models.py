from django.db import models

# Create your models here.
class Statie(models.Model):
    nume = models.CharField(max_length=255)
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.nume
