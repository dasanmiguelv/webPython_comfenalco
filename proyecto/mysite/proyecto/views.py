from django.shortcuts import render
from django.http import HttpResponse

from .models import Game

def listar_juegos(request):    
    juegos = Game.objects.all()

    messaje = "Lista de juegos"
    for juego in juegos:
        messaje = messaje + "<br> {}".format(juego.fecha)

    return HttpResponse(messaje)

def index(request):
    juegos = Game.objects.all()

    # ejemplo con string:
    messaje = "Lista de jugadores"
    fechas_de_juegos = []
    for juego in juegos:
        messaje = messaje + "<br> {}".format(juego.fecha)        
        fechas_de_juegos.append(juego.fecha)

    contexto = {        
        "juegos": fechas_de_juegos
    }

    return render(request, 'index.html', contexto)