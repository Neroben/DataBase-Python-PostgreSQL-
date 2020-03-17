from django.shortcuts import render, get_object_or_404
from database.models import Sponsor, Confederacy, Club, Coach, Match, Player

from django.shortcuts import redirect

from database.reservation import csv_writer

from .forms import ConfederacyForm, ClubForm, PlayerForm, CoachForm, MatchForm, SponsorForm

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Вариант регистрации на базе класса FormView
class MyRegisterFormView(FormView):
    # Укажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

def home(request):
    return render(request, 'database/home.html', {})

def view(request):
    return render(request, 'database/view.html', {})

def allclub(request):
    club=Club.objects.all()
    return render(request, 'database/allclub.html', {'clubs':club})

def allcoach(request):
    coach=Coach.objects.all()
    return render(request, 'database/allcoach.html', {'coachs':coach})

def allconfederacy(request):
    confederacy=Confederacy.objects.all()
    return render(request, 'database/allconfederacy.html', {'confederacys':confederacy})

def allmatch(request):
    match=Match.objects.all()
    return render(request, 'database/allmatch.html', {'matchs':match})

def allplayer(request):
    player=Player.objects.all()
    return render(request, 'database/allplayer.html', {'players':player})

def allsponsor(request):
    sponsor = Sponsor.objects.all()
    return render(request, 'database/allsponsor.html', {'sponsors':sponsor})

def club(request, pk):
    club = get_object_or_404(Club, club_id=pk)
    return render(request, 'database/club.html', {'club':club})

def coach(request, pk):
    coach = get_object_or_404(Coach, coach_id=pk)
    return render(request, 'database/coach.html', {'coach':coach})

def confederacy(request, pk):
    confederacy = get_object_or_404(Confederacy, confederacy_id=pk)
    return render(request, 'database/confederacy.html', {'confederacy':confederacy})

def match(request, pk):
    match = get_object_or_404(Match, match_id=pk)
    return render(request, 'database/match.html', {'match':match})

def player(request, pk):
    player = get_object_or_404(Player, player_id=pk)
    return render(request, 'database/player.html', {'player':player})

def sponsor(request, pk):
    sponsor = get_object_or_404(Sponsor, sponsor_id=pk)
    return render(request, 'database/sponsor.html', {'sponsor':sponsor})

def club_new(request):
    if request.method == "POST":
        form = ClubForm(request.POST)
        if form.is_valid():
            error=''
            flag=False
            if (form.cleaned_data.get('rating') < 0):
                error = 'Отрицательное значение рейтинга'
                flag=True
            if flag:
                return render(request, 'register/club_edit.html', {'error':error, 'form':form})
            post = form.save(commit=False)
            post.save()
            return redirect('club', pk=post.pk)
    else:
        form = ClubForm()
    return render(request, 'register/club_edit.html', {'form': form})

def coach_new(request):
    if request.method == "POST":

        form = CoachForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()
            return redirect('coach', pk=post.pk)
    else:
        form = CoachForm()
    return render(request, 'register/coach_edit.html', {'form': form})

def confederacy_new(request):
    if request.method == "POST":
        form = ConfederacyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('confederacy', pk=post.pk)
    else:
        form = ConfederacyForm()
    return render(request, 'register/confederacy_edit.html', {'form': form})

def match_new(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            error1 = ''
            error2 = ''
            error3 = ''
            flag = False
            if(form.cleaned_data.get('count1') < 0):
                error1="Отрицательное значение счёта первой команды"
                flag = True
            if(form.cleaned_data.get('count2') < 0):
                error2="Отрицательное значение счёта второй команды"
                flag = True
            if(form.cleaned_data.get('sold') < 0):
                error3="Отрицательное значение продаж"
                flag = True
            if(flag):
                return render(request, 'register/match_edit.html', {'error1':error1,'error2':error2,'error3':error3, 'form':form})
            post = form.save(commit=False)
            post.save()
            return redirect('match', pk=post.pk)
    else:
        form = MatchForm()
    return render(request, 'register/match_edit.html', {'form': form})

def player_new(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            error=''
            flag=False
            if (form.cleaned_data.get('efficiency') < 0):
                error = 'Отрицательное значение эффективности'
                flag=True
            if(form.cleaned_data.get('club') == 0):
                error += '<br /> Не выбран клуб'
                flag=True
            if flag:
                return render(request, 'register/player_edit.html', {'form': form, 'error':error})
            post = form.save(commit=False)
            post.save()
            return redirect('player', pk=post.pk)
    else:
        form = PlayerForm()
    return render(request, 'register/player_edit.html', {'form': form})

def sponsor_new(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('sponsor', pk=post.pk)
    else:
        form = SponsorForm()
    return render(request, 'register/sponsor_edit.html', {'form': form})

def clubdelete(request, id):
    obj = get_object_or_404(Club, club_id=id)
    obj.delete()
    return redirect('allclub')

def sponsordelete(request, id):
    obj = get_object_or_404(Sponsor, sponsor_id=id)
    obj.delete()
    return redirect('allsponsor')

def confederacydelete(request, id):
    obj = get_object_or_404(Confederacy, confederacy_id=id)
    obj.delete()
    return redirect('allconfederacy')

def matchdelete(request, id):
    obj = get_object_or_404(Match, match_id=id)
    obj.delete()
    return redirect('allmatch')

def coachdelete(request, id):
    obj = get_object_or_404(Coach, coach_id=id)
    obj.delete()
    return redirect('allcoach')

def playerdelete(request, id):
    obj = get_object_or_404(Player, player_id=id)
    obj.delete()
    return redirect('allplayer')


def confederacyreservation(request, id):
    obj = get_object_or_404(Confederacy, confederacy_id=id)
    clubs = Club.objects.filter(confederacy = id)
    data = []
    for club in clubs:
        path=Match.objects.filter(club_id1 = club.club_id)

        for p in path:
            #data.append(p.playdata)
            match = []
            match.append(p.club_id1.name)
            match.append(p.count1)
            match.append(p.club_id2.name)
            match.append(p.count2)
            data.append(match)
        path=Match.objects.filter(club_id2 = club.club_id)
        for p in path:
            #data.append(p.playdata)
            match = []
            match.append(p.club_id1.name)
            match.append(p.count1)
            match.append(p.club_id2.name)
            match.append(p.count2)
            data.append(match)
    csv_writer(data, obj.name + '.csv')
    confederacy=Confederacy.objects.all()
    return render(request, 'database/allconfederacy.html', {'confederacys':confederacy, 'reserv':obj.name + ' зарезервировано'})
