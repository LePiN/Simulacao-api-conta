from django.db import models
from datetime import datetime


class Conta(models.Model):
    numero_conta = models.IntegerField()
    numero_agencia = models.IntegerField()
    nome_titular = models.CharField(max_length=100)
    saldo = models.FloatField(default=0)
    data_criacao_conta = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.numero_conta}/{self.numero_agencia} - {self.nome_titular}'


class Movimentacao(models.Model):
    OPCOES_MOVIMENTACAO = (('D', 'DEBITO'), ('C', 'CREDITO'))
    conta = models.ForeignKey('Conta', on_delete=models.CASCADE, related_name='movimentacao')
    tipo_movimentacao = models.CharField(max_length=1, choices=OPCOES_MOVIMENTACAO, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    descricao = models.CharField(max_length=144, null=False, blank=False)
    data_ocorrencia = models.DateTimeField(default=datetime.now, blank=False, null=False)
