from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Tournoi

def tournois(request):
    tournament_list = get_list_or_404(Tournoi)
    return render(request, 'tournament/tournois.html', {'tournois': tournois})
