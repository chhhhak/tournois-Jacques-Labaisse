from django.urls import path
from . import views

app_name = "tournaments"
urlpatterns = [
    path('match/<int:id_match>', views.match, name='match'),
    path('nouveau_commentaire/match/<int:id_match>', views.commentaire, name='commentaire'),
    path('poule/<int:id_poule>', views.poule, name='poule'),
    path('tournois', views.tournois, name = 'tournois'),
    path('tournoi/<int:id_tournoi>', views.tournoi, name = 'tournoi')
]