from django.shortcuts import render
from .models import Cita_medica, Paciente, Doctor

# Create your views here.

def index(request):    
    return render(request, 'index.html')

def list_citas(request):
    citas = Cita_medica.objects.all()  
    contexto = {"citas": citas}    
    return render(request, 'citas.html', contexto)