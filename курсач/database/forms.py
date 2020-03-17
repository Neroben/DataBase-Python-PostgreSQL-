from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.admin.widgets import AdminDateWidget

from .models import Sponsor, Player, Coach, Club, Match, Confederacy

class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ConfederacyForm(forms.ModelForm):
    class Meta:
        model = Confederacy
        fields = ('name',)
        labels = {
            'name': ('Название'),
        }

class SponsorForm(forms.ModelForm):

    class Meta:
        model = Sponsor
        fields = ('sponsor_id', 'name')
        labels = {
            'sponsor_id': ('ID Спонсора'),
            'name': ('Название'),
        }

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('player_id', 'club', 'name', 'lastname', 'efficiency')
        labels = {
            'player_id': ('ID Игрока'),
            'club': ('Клуб'),
            'name': ('Имя'),
            'lastname': ('Фамилия'),
            'efficiency': ('Эффективность'),
        }

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ('club', 'name', 'lastname')
        labels = {
            'club': ('Клуб'),
            'name': ('Имя'),
            'lastname': ('Фамилия'),
            }

class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = ('club_id', 'name', 'rating', 'confederacy', 'sponsor')
        labels = {
            'club_id': ('Клуб'),
            'name': ('Имя'),
            'rating': ('Рейтинг'),
            'confederacy': ('Лига'),
            'sponsor': ('Спонсор'),
            }


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ('match_id', 'playdata', 'count1', 'club_id1', 'count2', 'club_id2', 'sold')
        labels = {
            'match_id': ('ID Матча'),
            'playdata': ('Дата игры'),
            'count1': ('Счёт первой команды'),
            'club_id1': ('Первая команда'),
            'count2': ('Счёт второй команды'),
            'club_id2': ('Вторая команда'),
            'sold': ('Количество проданных билетов'),
        }
        #widgets = {
            #'playdata': DateInput(attrs={'type': 'date'}),
            #'playdata': forms.DateTimeInput(
        #    attrs={
        #        'type': 'date',
        #    })
        #}
