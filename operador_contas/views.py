from rest_framework import generics
from operador_contas.models import Conta, Movimentacao
from operador_contas.serializers import ContaSerializer, MovimentacaoSerializer


class Contas(generics.ListCreateAPIView):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer


class Movimentacoes(generics.ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer

    def validar_movimentacao(self):
        conta = self.request.query_params.get('conta')
        tipo_movimentacao = self.request.query_params.get('tipo_movimentacao')
        valor = self.request.query_params.get('valor')
        if (tipo_movimentacao == 'D') and ((conta.saldo - valor) < 0):
            raise exceptions.PermissionDenied
