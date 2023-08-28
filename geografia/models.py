from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    numero_habitantes = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'pais'

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    alcalde = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.pais.nombre} '
    
    class Meta:
        db_table = 'ciudad'