from django.contrib import admin

from .models import Commentaire, Equipe, Match, Poule, Tournoi

admin.site.register(Commentaire)
admin.site.register(Equipe)
admin.site.register(Poule)
admin.site.register(Match)
admin.site.register(Tournoi)
