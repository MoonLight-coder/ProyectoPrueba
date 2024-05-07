from django.db import models


# Create your models here.  
'''está comentado debido a que al hacer las migraciones a MySQL se genera un usuario por default'''
#class usuario(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    username = models.CharField(max_length=50)
#    password = models.CharField(max_length=32)

#    def __str__(self):
#        return self.id

class cliente(models.Model):
    cliente_id = models.BigAutoField(primary_key=True, default=0)
    nombre_empresa = models.CharField(max_length=50)
    rut = models.CharField(max_length=9)
    direccion = models.CharField(max_length=252)
    telefono = models.IntegerField()

    def __str__(self):
        return self.cliente_id
    
class modeloEstado(models.Model):
    estado_id = models.BigAutoField(primary_key=True, default=0)
    estado = models.CharField(max_length=20)

    def __str__(self):
        return self.estado_id

class modeloEtapa(models.Model):
    etapa_id = models.BigAutoField(primary_key=True, default=0)
    etapa = models.CharField(max_length=20)

    def __str__(self):
        return self.etapa_id

class modeloProspecto(models.Model):
    modelo_id = models.BigAutoField(primary_key=True, default=0)
    nombre = models.CharField(max_length=252)
    email = models.CharField(max_length=252)
    telefono = models.IntegerField()
    sexo = models.CharField(max_length=32)
    cliente_id = models.ForeignKey(cliente, on_delete=models.CASCADE, default=1)
    estado_id = models.ForeignKey(modeloEstado, on_delete=models.CASCADE)
    etapa_id = models.ForeignKey(modeloEtapa, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo_id