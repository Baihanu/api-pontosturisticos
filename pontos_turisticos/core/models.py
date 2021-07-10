from django.db import models
from pontos_turisticos.atracoes.models import Recurso
from pontos_turisticos.comentarios.models import Comentario
from pontos_turisticos.avaliacoes.models import Avaliacao
from pontos_turisticos.endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recurso = models.ManyToManyField(Recurso)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
