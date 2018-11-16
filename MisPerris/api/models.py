from django.db import models

# Create your models here.

class Mascota(models.Model):
    CodigoMascota=models.AutoField(primary_key=True)
    NombreMascota=models.CharField(max_length=20)
    RazaMascota=models.CharField(max_length=50)
    Descripcion=models.TextField(null=True, blank=True)
    EstadoMascota=models.CharField(max_length=50,default=True)  