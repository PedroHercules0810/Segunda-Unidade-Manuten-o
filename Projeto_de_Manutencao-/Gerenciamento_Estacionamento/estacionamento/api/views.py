"""importes necessarios para a criação das views"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotAuthenticated
from rest_framework import status
from estacionamento.api.serializers import ClienteSerializer
from estacionamento.api.serializers import VeiculoSerializer
from estacionamento.api.serializers import EstacionamentoSerializer
from estacionamento.models import Cliente, Veiculo, Estacionamento

ERROR = "permissão negada!"


class ClienteViewSet(ModelViewSet):
    """cria uma viewset para o model Cliente"""
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class VeiculoViewSet(ModelViewSet):
    """cria uma viewset para o model Veiculo"""
    serializer_class = VeiculoSerializer
    queryset = Veiculo.objects.all()


class EstacionamentoViewSet(ModelViewSet):
    """"cria uma viewset para o model Estacionamento"""
    serializer_class = EstacionamentoSerializer
    queryset = Estacionamento.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)

            data = response.data

            return Response(data, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(
                {"Erro": "Dados invalidos!"}, status=status.HTTP_409_CONFLICT
            )

        except KeyError:
            return Response(
                {"Erro": "Dado faltando/errado!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except PermissionError:
            return response(
                {"Erro": ERROR},
                status=status.HTTP_403_FORBIDDEN
             )

        except PermissionDenied:
            return response(
                {"Error": ERROR},
                status=status.HTTP_403_FORBIDDEN
            )

        except NotAuthenticated:
            return response(
                {"Error": "Não autenticado!"},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return response

        except ValueError:
            return Response(
                {"Erro": "Dados invalidos!"}, status=status.HTTP_409_CONFLICT
            )

        except KeyError:
            return Response(
                {"Erro": "Algum dado faltando ou errado!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        except PermissionError:
            return response(
                {"Erro": "Permissão negada!"},
                status=status.HTTP_403_FORBIDDEN
            )

        except PermissionDenied:
            return response(
                {"Error": "Permissão negada!"},
                status=status.HTTP_403_FORBIDDEN
            )

        except NotAuthenticated:
            return response(
                {"Error": "Não autenticado!"},
                status=status.HTTP_401_UNAUTHORIZED
            )
