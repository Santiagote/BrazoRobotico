from django.db import models
class Registro(models.Model):
    usuario = models.CharField(max_length=100)
    accion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.usuario} - {self.accion} "
# Create your models here.
