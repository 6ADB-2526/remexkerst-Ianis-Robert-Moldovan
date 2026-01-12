from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict
import json
from .models import Speler, Match_punten


# Create your views here.

# een kleine test functie om te zien als het server juist werkt
def test(request):
    return HttpResponse("OK")

# speler toevoegen 
@csrf_exempt
def speler_toevoegen(request):
    data = json.loads(request.body)
    new_speler = Speler()
    new_speler.naam = data["naam"]
    new_speler.voornaam = data["voornaam"]
    new_speler.email = data["email"]
    new_speler.save()
    return HttpResponse("Speler is toegevoegd")

# 1 speler opvragen via id
def get_speler(request, id):    
    one_speler = Speler.objects.get(pk = id)
    one_speler_dict = model_to_dict(one_speler)
    return JsonResponse(one_speler_dict, safe=False)

# alle spelers terug geven
def get_all_spelers(request):
    alleSpelers = Speler.objects.all().values("id","naam","voornaam", "email")
    alleSpelers_lijst = list(alleSpelers)
    return JsonResponse(alleSpelers_lijst, safe=False)

# punten match toevoegen
@csrf_exempt
def match_punten_toevoegen(request):
    data = json.loads(request.body)
    nieuwe_match = Match_punten()
    nieuwe_match.nummerSpeler = data["nummerSpeler"]
    nieuwe_match.punten = data["punten"]
    nieuwe_match.matchCode = data["matchCode"]
    nieuwe_match.save()
    return HttpResponse("nieuwe match is toegevoegd")

# punten match terug geven
def get_all_matches(request):
    alleMatches = Match_punten.objects.all().values("nummerSpeler", "punten", "matchCode")
    alleMatches_lijst = list(alleMatches)
    return JsonResponse(alleMatches_lijst, safe=False)

# filter
# def matchpunten_resultaat(request):
#     spelerID = Speler.objects.filter().values()