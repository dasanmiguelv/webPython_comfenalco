from django.shortcuts import render, redirect
from .models import Cita_medica, Paciente, Doctor
from django.contrib import messages

# Create your views here.

def index(request):    
    return render(request, 'index.html')

def list_pacientes(request):
    pacientes = Paciente.objects.all()  
    contexto = {"pacientes": pacientes}    
    return render(request, 'pacientes.html', contexto)

#Views the doctors

def list_doctor(request):   
    doctores = Doctor.objects.all()      
    return render(request, 'doctores.html', {"doctores":doctores})

def registrar_doctor(request):
    nombre = request.POST['nombreDr']
    apellido = request.POST['apellidoDr']

    doctor = Doctor.objects.create(nombre=nombre, apellido=apellido)
    return (redirect('/list_doctores'))    

def eliminar_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return (redirect('/list_doctores'))    

#View the doctors

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