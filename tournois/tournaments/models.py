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
    
    def compute_points(self):
        totalPoints = 0
        for match in self.team1.all():
            totalPoints += match.test_match_to_points()[0]
        for match in self.team2.all():
            totalPoints += match.test_match_to_points()[1]

        return totalPoints

    def compute_scored_goals(self):
        scored_goals = 0
        for match in self.team1.all():
            if match.goals1 is not None:
                scored_goals += match.goals1
        for match in self.team2.all():
            if match.goals2 is not None:
                scored_goals += match.goals2
        return scored_goals

    def compute_conceded_goals(self):
        conceded_goals = 0
        for match in self.team1.all():
            if match.goals2 is not None:
                conceded_goals += match.goals2
        for match in self.team2.all():
            if match.goals1 is not None:
                conceded_goals += match.goals1
        return conceded_goals
    
    def goal_diff(self):
        return self.compute_scored_goals() - self.compute_conceded_goals()



class Poule(models.Model):
    tournament = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    poolId = models.IntegerField(default=0)
    teams = models.ManyToManyField(Equipe)

    def __str__(self):
        return self.teams.__str__()
    
    

    

    


"""
    établir les matchs : déclencher la fonction manuellement sur la 
    page de la pool, boutton disponible uniquement pour l'admin

"""    

class Match(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    team1 = models.ForeignKey(Equipe, related_name="team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Equipe, related_name="team2", on_delete=models.CASCADE)
    goals1 = models.IntegerField(null=True, blank=True)
    goals2 = models.IntegerField(null=True, blank=True)
    pool = models.ForeignKey(Poule, on_delete=models.CASCADE)

    def __str__(self):
        if self.goals1 == None:
            strRep = '{} - {}'.format(self.team1.name, self.team2.name)
        else:
            strRep = '{} {}-{} {}'.format(self.team1.name, self.goals1, self.goals2, self.team2.name)
        return strRep

    """
        This method computes the points to attribute to the teams
        participating in a match regarding the score.
    """
    def test_match_to_points(match):
        winner_points = 3 
        loser_points = 0
        draw_points = 1

        if (match.goals1 == None or match.goals2 == None):
                return 0, 0

        if match.goals1 > match.goals2:
            return winner_points, loser_points
        
        if match.goals1 < match.goals2:
            return loser_points, winner_points
        
        else:
            return draw_points, draw_points
    