from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils import timezone

from .forms import CommentForm
from .models import Commentaire, Equipe, Match, Poule, Tournoi

def poule(request, id_poule):
    pool = get_object_or_404(Poule, pk=id_poule)
    # pool = sorted(pool.teams.all(), key = lambda team: team.compute_points(), reverse=True)
    # pool = pool.teams.all().order_by('compute_points')
    return render(request, 'tournaments/poule.html', {'pool': pool})

def tournois(request):
    tournament_list = get_list_or_404(Tournoi)
    return render(request, 'tournaments/tournois.html', {'tournament_list': tournament_list})

def tournoi(request, id_tournoi):
    tournament = get_object_or_404(Tournoi, pk=id_tournoi)
    return render(request, 'tournaments/tournoi.html', {'tournament': tournament})

def match(request, id_match):
    match = get_object_or_404(Match, pk=id_match)
    return render(request, 'tournaments/match.html', {'match': match} )


def commentaire(request, id_match):
    match = get_object_or_404(Match, pk=id_match)
    user = request.user
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            print("lesgo")
            comment_obj = comment_form.save(commit=False)
            comment_obj.author = request.user
            comment_obj.date = timezone.now()
            comment_obj.match = match
            comment_obj.save()
            return render(request, 'tournaments/match.html', {'match':match, "comment_form":CommentForm(initial={"author": user.username, "match":match, "date": timezone.now(), "text": ""})})
        
        else:
            print(comment_form.errors.as_data())
            return render(request, 'tournaments/comment_form.html', {'match':match} )   

    else:
        print("get")
        
        comment_form = CommentForm({'author': user.username, 'match':match, 'date': timezone.now(), 'text': " Qu'avez vous pensé de ce match?"})
        # comment_form = CommentForm()
        print(comment_form.errors)
        print(comment_form.is_bound)
        print(comment_form.is_valid())
        return render(request, 'tournaments/comment_form.html', {"match":match, "comment_form":comment_form} )   

def home(request):
    
    return render(request, 'tournaments/home.html',)