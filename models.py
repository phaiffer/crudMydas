from django.db import models

# Create your models here.

class Pais(models.Model):
    id = models.AutoField('Id_pais', primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    sigla = models.CharField(max_length=3, null=False, blank=False)

def __str__(self):
    return self.id.nome

class Estado(models.Model):
    nome_estado = models.CharField(max_length=50, null=False, blank=False)
    sigla_estado = models.CharField(max_length=3, null=False, blank=False)
    id_estado = models.ForeignKey(Pais, models.DO_NOTHING,'Id_pais', primary_key=True)



def __str__(self):
    return self.nome


