"""importes necessários para criação de models"""
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    """Modelo de cliente"""
    nome = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, null=False)
    telefone = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.nome}"


class Veiculo(models.Model):
    """Modelo de veículo"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=100, unique=True)
    cor = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        # pylint: disable=no-member E1101
        cliente = Cliente.objects.get(id=self.cliente)
        return f'{cliente.nome}'


class Estacionamento(models.Model):
    """Modelo de estacionamento"""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculos = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField(blank=True, null=True)
    horario_saida = models.DateTimeField(null=True, blank=True)

    def liberar_vaga(self):
        """Método para liberar vaga"""
        if self.horario_saida is None:
            self.horario_saida = timezone.now()
            self.save()
            return "A vaga foi liberada com sucesso!"
        return "A vaga já foi liberada anteriormente."

    def __str__(self):
        # pylint: disable=no-member E1101
        self.cliente = Cliente.objects.get(id=self.cliente)
        if self.horario_saida:
            return f"Estacionamento para {self.cliente.nome} - Vaga liberada."
        return f"Estacionamento para {self.cliente.nome} - Ocupada."
