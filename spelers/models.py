from django.db import models

# Create your models here.
class Speler(models.Model):
    naam = models.CharField(max_length=25)
    voornaam = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)

class Match_punten(models.Model):
    nummerSpeler = models.IntegerField()
    punten = models.IntegerField()
    matchCode = models.IntegerField()