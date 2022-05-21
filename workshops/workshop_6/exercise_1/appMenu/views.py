from django.shortcuts import render
from .models import Cita_medica, Paciente, Doctor

# Create your views here.

def index(request):    
    return render(request, 'index.html')



def list_citas(request):
    if request.method == 'POST':
        data = request.POST
        paciente_nombre = data.get('paciente_nombre')        
        doctor_nombre = data.get('doctor_nombre')
        ubicacion = data.get('ubicacion')
        fecha_cita = data.get('fecha_cita')
        
        print(paciente_nombre,doctor_nombre, ubicacion, fecha_cita )

        cita = Cita_medica()
        Cita_medica.paciente = paciente_nombre
        Cita_medica.doctor = doctor_nombre
        Cita_medica.ubicacion = ubicacion
        Cita_medica.fecha = fecha_cita



        cita.save()

    citas = Cita_medica.objects.all()  
    contexto = {"citas": citas}    
    return render(request, 'citas.html', contexto)