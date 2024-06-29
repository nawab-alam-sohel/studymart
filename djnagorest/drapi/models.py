from django.db import models

# Create your models here.
class Aiquest(models.Model):
    t_name = models.CharField(max_length=25)
    c_name = models.CharField(max_length=20)
    c_duration = models.IntegerField()
    seat = models.IntegerField()
    