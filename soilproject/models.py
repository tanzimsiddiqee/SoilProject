from django.db import models

class Students(models.Model):
    ID = models.IntegerField()
    Name = models.TextField()
    ImagePath = models.TextField()
    class Meta:
       managed = False
       db_table = 'Students'