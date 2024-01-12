from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Talla(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        self.eliminado = True
        self.save()

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        self.eliminado = True
        self.save()

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        self.eliminado = True
        self.save()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # Información básica
    codigo_id = models.CharField(
        max_length=100, blank=False, db_column="codigo_id", unique=True
    )
    nombre = models.CharField(max_length=255, blank=False, db_column="nombre")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos", null=True)

    # Información detallada
    tallas = models.ManyToManyField(Talla)
    colores = models.ManyToManyField(Color)
    material = models.CharField(max_length=20)
    temporada = models.CharField(max_length=20)
    ocasión = models.CharField(max_length=20)
    descripción = models.TextField()

    # Información de inventario
    stock = models.IntegerField()
    disponibilidad = models.BooleanField()

    # seguimientos
    fecha_creación = models.DateTimeField(auto_now_add=True)
    fecha_actualización = models.DateTimeField(auto_now=True)
    creador = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="productos_creados"
    )
    modificador = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="productos_modificados"
    )

    eliminado = models.BooleanField(default=False)

    def soft_delete(self):
        self.eliminado = True
        self.save()

    def __str__(self):
        return self.nombre
