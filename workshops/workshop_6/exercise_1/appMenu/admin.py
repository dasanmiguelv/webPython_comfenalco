from django.contrib import admin
from .models import Cita_medica, Paciente
from .models import Doctor

class PacienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class Cita_medicaAdmin(admin.ModelAdmin):
    list_filter = ['fecha']

# Register your models here.
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Cita_medica, Cita_medicaAdmin)