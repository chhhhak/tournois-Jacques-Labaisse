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

class Equipe(models.Model):
    name = models.CharField(max_length=200)
    trainer = models.CharField(max_length=200)
    players = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Poule(models.Model):
    tournament = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    poolId = models.IntegerField(default=0)
    teams = models.ManyToManyField(Equipe)

    def __str__(self):
        return self.teams.__str__()
    

class Match(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    team1 = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    goals1 = models.IntegerField(default=0)
    goals2 = models.IntegerField(default=0)
    pool = models.ForeignKey(Poule, on_delete=models.CASCADE)

    def __str__(self):
        strRep = '{} {}-{} {}'.format(self.team1.name, self.goal1, self.goal2, self.team2.name)
        return strRep
    