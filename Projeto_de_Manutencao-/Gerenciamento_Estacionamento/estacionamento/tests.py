from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from estacionamento.models import Cliente, Veiculo, Estacionamento


class ClienteTesteCase(TestCase):
    def setUp(self):
        self.novo_cliente = Cliente.objects.create(
            nome="Marta Silva",
            CPF="12345678912",
            telefone=991234567
        )

    def test_cadastrar_cliente(self):
        url = "http://localhost:8000/cliente"
        data = {
            "nome": "Claudio Maia",
            "CPF": "12345671245",
            "telefone": 997654321
        }
        response = self.client.post(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Cliente.objects.filter(nome="Claudio Maia").exists())

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_listar_cliente(self):
        url = "http://localhost:8000/cliente"
        Cliente.objects.create(
            nome="Claudio Maia",
            CPF="12345671245",
            telefone=997654321
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_atualizar_cliente(self):
        url = f"http://localhost:8000/cliente/{self.novo_cliente.id}/"
        data = {
            "nome": "Maria Maia",
            "CPF": "12348671245",
            "telefone": 997655321
        }
        response = self.client.put(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_cliente(self):
        url = f"http://localhost:8000/cliente/{self.novo_cliente.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Cliente.objects.filter(id=self.novo_cliente.id).exists())


class VeiculoTesteCase(TestCase):

    def setUp(self):
        self.novo_cliente = Cliente.objects.create(
            nome="Marta Silva",
            CPF="12345678912",
            telefone=991234567
        )
        self.novo_veiculo = Veiculo.objects.create(
            cliente=self.novo_cliente,
            modelo="Toyota Corolla",
            placa="ABC1234",
            cor="Preto",
            tipo="Carro"
        )

    def test_cadastrar_veiculo(self):
        url = "http://localhost:8000/veiculos"
        data = {
            "cliente": self.novo_cliente.id,
            "modelo": "Toyota Corolla",
            "placa": "ABC1244",
            "cor": "Cinza",
            "tipo": "Carro"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Veiculo.objects.filter(placa="ABC1244").exists())

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)

    def test_listar_veiculos(self):
        url = "http://localhost:8000/veiculos"
        Veiculo.objects.create(
            cliente=self.novo_cliente,
            modelo="Toyota Corolla",
            placa="ABC1234",
            cor="Preto",
            tipo="Carro"
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['placa'], "ABC1234")

    def test_atualizar_veiculo(self):
        url = f"http://localhost:8000/veiculo/{self.novo_veiculo.id}/"
        data = {
            "cliente": self.novo_cliente.id,
            "modelo": "Toyota Corolla",
            "placa": "ABC2244",
            "cor": "Cinza",
            "tipo": "Carro"
        }
        response = self.client.put(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deletar_veiculo(self):
        url = f"http://localhost:8000/veiculo/{self.novo_veiculo.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Veiculo.objects.filter(id=self.novo_veiculo.id).exists())


class EstacionamentoTesteCase(TestCase):

    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="Marta Silva",
            CPF="12345678912",
            telefone=991234567
        )
        self.veiculo = Veiculo.objects.create(
            cliente=self.cliente,
            modelo="Toyota Corolla",
            placa="ABC1234",
            cor="Preto",
            tipo="Carro"
        )
        self.estacionamento = Estacionamento.objects.create(
            cliente=self.cliente,
            veiculos=self.veiculo,
            horario_entrada=timezone.now()
        )

    def test_criar_estacionamento(self):
        url = "http://localhost:8000/estacionamento"
        data = {
            "cliente": self.cliente.id,
            "veiculos": self.veiculo.id,
            "horario_entrada": timezone.now()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Estacionamento.objects.filter(cliente=self.cliente).exists())
