from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Poule, Tournoi

def poule(request, id_poule):
    pool = get_object_or_404(Poule, pk=id_poule)
    return render(request, 'tournois/poule.html', {'pool': pool})

def tournois(request):
    tournament_list = get_list_or_404(Tournoi)
    return render(request, 'tournois/tournois.html', {'tournament_list': tournament_list})

def tournoi(request, id_tournoi):
    tournament = get_object_or_404(Tournoi, pk=id_tournoi)
    return render(request, 'tournois/tournoi.html', {'tournament': tournament})