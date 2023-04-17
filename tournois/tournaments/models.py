import datetime

from django.db import models
from django.utils import timezone

class Tournoi(models.Model):
    name = models.CharField(max_length=200)
    beg_date = models.DateTimeField('Date began', default=timezone.now, null=True)
    end_date = models.DateTimeField('Date ended', default=timezone.now, null=True)
    location = models.CharField(max_length=200, blank=True, default='')
    nbPool = models.IntegerField(default=0)
    nbTeampPool = models.IntegerField(default=0)

    def __str__(self):
        return self.name 
