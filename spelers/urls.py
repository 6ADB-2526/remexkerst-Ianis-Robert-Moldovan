from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test), # het test functie
    path('add/', views.speler_toevoegen), # speler toevoegen 
    path('<int:id>/', views.get_speler), # get 1 speler op basis van id
    path('', views.get_all_spelers), # alle spelers opgeven
    path('addMatch/', views.match_punten_toevoegen), # een match toevoegen 
    path('matches/', views.get_all_matches), # het stuurt alle data van de matches terug
    # path('matchPunten/resultaat/<int:idSpeler>/<int:matchCode>/', views.resultaat), # resultaat opvragen speler match
]