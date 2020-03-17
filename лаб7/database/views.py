from django.shortcuts import render
from database.models import Sponsor, Confederacy, Club, Coach, Match, Player

def home(request):
    return render(request, 'database/home.html', {})

def view(request):
    return render(request, 'database/view.html', {})

def club(request):
    club=Club.objects.all()
    return render(request, 'database/club.html', {'clubs':club})

def coach(request):
    coach=Coach.objects.all()
    return render(request, 'database/coach.html', {'coachs':coach})

def confederacy(request):
    confederacy=Confederacy.objects.all()
    return render(request, 'database/confederacy.html', {'confederacys':confederacy})

def match(request):
    match=Match.objects.all()
    return render(request, 'database/match.html', {'matchs':match})

def player(request):
    player=Player.objects.all()
    return render(request, 'database/player.html', {'players':player})

def sponsor(request):
    sponsor = Sponsor.objects.all()
    return render(request, 'database/sponsor.html', {'sponsors':sponsor})
