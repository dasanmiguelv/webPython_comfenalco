from django.db import models

# Create your models here.
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "{} {} - {}".format(self.nombre, self.apellido, self.fecha_nacimiento)


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)    

class Cita_medica(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=200)
    fecha = models.DateField()

    def __str__(self):
        return "{} {} - {} - {}".format(self.paciente, self.doctor, self.ubicacion, self.fecha)