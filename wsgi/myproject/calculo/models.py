from django.db import models

class Ispt(models.Model):
    fecha_fin = models.CharField(max_length=10)
    fecha_ini = models.CharField(max_length=10)
    tipo = models.CharField(max_length=10)
    linferior = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    superior = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    bruto = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    cuota = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    excedente = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subsidio = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

class Regla(models.Model):
    tipo = models.CharField(max_length=2)
    concepto = models.CharField(max_length=3)
    variable = models.CharField(max_length=25)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    descripcion = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    jerarquias = models.CharField(max_length=100)
    niveles = models.CharField(max_length=100)
    nombramientos = models.CharField(max_length=100)
    grupos = models.CharField(max_length=100)
    tipo_calculo = models.CharField(max_length=25)
    codigo_salida = models.CharField(max_length=5)

class Constante(models.Model):
    constante = models.CharField(max_length=25)
    valor = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
