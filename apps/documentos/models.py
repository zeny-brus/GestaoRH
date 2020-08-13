from django.db import models
from apps.colaboradores.models import Colaborador

# Create your models here.
class Documentos(models.Model):
    descricao = models.CharField(max_length=100)
    pertencente = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.descricao