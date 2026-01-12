from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test), # het test functie
    path('add/', views.speler_toevoegen), # speler toevoegen 
    path('<int:id>/', views.get_speler),
    path('', views.get_all_spelers), # alle spelers opgeven
    path('update/', views.update_speler)
    # path('matchPunten/resultaat/<int:idSpeler>/<int:matchCode>/', views.resultaat), # resultaat opvragen speler match
    # path('punten/<int:idSpeler>/', views.totaalSpeler), #totaal punten speler
]