from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class venta(models.Model):
    id_venta = models.CharField(primary_key=True,max_length=6)
    fecha = models.DateField(verbose_name="fecha de compra", null=False, blank= False)
    cantidad = models.CharField(max_length=45)
    id_cliente = models.CharField(max_length=45)
    id_producto = models.CharField(max_length=45)
    precio = models.CharField(max_length=100)
    total = models.CharField(max_length=15)

    def __str__(self):
        return self.fecha
    