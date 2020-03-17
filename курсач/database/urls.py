from django.urls import path
from . import views
from django.db import models


urlpatterns = [
    path('', views.home, name='home'),
    path('view', views.view, name='view'),
    path('allclub', views.allclub, name='allclub'),
    path('allcoach', views.allcoach, name='allcoach'),
    path('allconfederacy', views.allconfederacy, name='allconfederacy'),
    path('allmatch', views.allmatch, name='allmatch'),
    path('allplayer', views.allplayer, name='allplayer'),
    path('allsponsor', views.allsponsor, name='allsponsor'),
    path('accounts/register/', views.MyRegisterFormView.as_view(), name="register"),
    path('allclub/<int:pk>/', views.club, name='club'),
    path('allcoach/<int:pk>/', views.coach, name='coach'),
    path('allconfederacy/<int:pk>/', views.confederacy, name='confederacy'),
    path('allmatch/<int:pk>/', views.match, name='match'),
    path('allplayer/<int:pk>/', views.player, name='player'),
    path('allsponsor/<int:pk>/', views.sponsor, name='sponsor'),
    path('allclub/new/', views.club_new, name='club_new'),
    path('allcoach/new/', views.coach_new, name='coach_new'),
    path('allconfederacy/new/', views.confederacy_new, name='confederacy_new'),
    path('allmatch/new/', views.match_new, name='match_new'),
    path('allplayer/new/', views.player_new, name='player_new'),
    path('allsponsor/new/', views.sponsor_new, name='sponsor_new'),
    path('allclub/delete/<int:id>/', views.clubdelete, name='clubdelete'),
    path('allcoach/delete/<int:id>/', views.coachdelete, name='coachdelete'),
    path('allconfederacy/delete/<int:id>/', views.confederacydelete, name='confederacydelete'),
    path('allmatch/delete/<int:id>/', views.matchdelete, name='matchdelete'),
    path('allplayer/delete/<int:id>/', views.playerdelete, name='playerdelete'),
    path('allsponsor/delete/<int:id>/', views.sponsordelete, name='sponsordelete'),
    path('confederacyreservation/<int:id>/', views.confederacyreservation, name='confederacyreservation'),
]
