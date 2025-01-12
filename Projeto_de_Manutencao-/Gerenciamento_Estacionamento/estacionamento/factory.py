import random
from faker import Faker
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from estacionamento.models import Cliente, Veiculo, Estacionamento

fake = Faker('pt_BR')


class ClienteFactory:

    def create(self):
        novo_cliente = User.objects.create_user(
            username=fake.unique.userName(),
            nome=fake.name(),
            CPF=fake.unique.cpf().replace("-", "").replace(".", ""),
            telefone=fake.random_number(digits=11, fix_len=True)
        )
        return novo_cliente


class VeiculoFactory:

    def create(self, cliente=None):
        if not cliente:
            cliente = ClienteFactory.create()

        novo_veiculo = Veiculo.objects.create(
            cliente=cliente,
            modelo=fake.word().capitalize() + " " + fake.word().capitalize(),
            placa=fake.unique.license_plate(),
            cor=fake.color_name(),
            tipo=fake.random_element(elements=["Carro", "Moto", "Caminhão"])
        )
        return novo_veiculo


class EstacionamentoFactory:

    def create(self):
        cliente = ClienteFactory.create()
        veiculo = VeiculoFactory.create(cliente=cliente)

        horario_entrada = fake.date_time_between(start_date="-2d", end_date="now", tzinfo=timezone.utc)
        horario_saida = (
            horario_entrada + timedelta(hours=random.randint(1, 5))
            if random.choice([True, False])
            else None
        )

        estacionamento = Estacionamento.objects.create(
            cliente=cliente,
            veiculos=veiculo,
            horario_entrada=horario_entrada,
            horario_saida=horario_saida
        )
        return estacionamento

    def create_multiple(self, num):
        for _ in range(num):
            EstacionamentoFactory.create()