from django.contrib import admin
from .models import Cita_medica, Paciente
from .models import Doctor





# Register your models here.
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Cita_medica)