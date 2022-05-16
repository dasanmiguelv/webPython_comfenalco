from django.contrib import admin
from .models import Cita_medica, Paciente, Doctor

class PacienteAdmin(admin.ModelAdmin):    
    search_fields = ['nombre', 'apellido']
    list_display = ['id', 'nombre', 'apellido', 'fecha_nacimiento']

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['nombre' , 'apellido']

class Cita_medicaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'doctor', 'ubicacion', 'fecha']
    list_filter = ['fecha']

# Register your models here.
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Cita_medica, Cita_medicaAdmin)