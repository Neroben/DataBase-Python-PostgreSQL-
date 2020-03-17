from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view', views.view, name='view'),
    path('club', views.club, name='club'),
    path('coach', views.coach, name='coach'),
    path('confederacy', views.confederacy, name='confederacy'),
    path('match', views.match, name='match'),
    path('player', views.player, name='player'),
    path('sponsor', views.sponsor, name='sponsor'),
]
