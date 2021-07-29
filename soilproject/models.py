from django.db import models

class Soils(models.Model):
    Id = models.IntegerField()
    Sample = models.TextField()
    Sand = models.TextField()
    Silt = models.TextField()
    Clay = models.TextField()
    Type = models.TextField()
    ImagePath = models.TextField()
    class Meta:
       managed = False
       db_table = 'Soil'