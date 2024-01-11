from django.db import models

# Create your models here.


class Producto(models.Model):
    # Información básica
    nombre = models.CharField(max_length=255)
    categoría = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos", null=True)

    # Información detallada
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    temporada = models.CharField(max_length=20)
    ocasión = models.CharField(max_length=20)
    descripción = models.TextField()

    # Información de inventario
    stock = models.IntegerField()
    disponibilidad = models.BooleanField()
    fecha_creación = models.DateTimeField(auto_now_add=True)
    fecha_actualización = models.DateTimeField(auto_now=True)

    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        self.eliminado = True
        self.save()

    def __str__(self):
        return self.nombre
