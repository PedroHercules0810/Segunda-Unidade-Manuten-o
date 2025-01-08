from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from estacionamento.models import Cliente, Veiculo, Estacionamento

class ClienteTesteCase(TestCase):

    def setUp(self):

        self.cliente = Cliente.objects.create(
            nome="Marta Silva",
            cpf="12345678912",
            telefone=991234567
        )
    def test_cadastrar_cliente(self):

        url = "http://localhost:8000/clientes"
        data = {
            "nome": "Claudio Maia",
            "cpf": "12345671245",
            "telefone": 997654321
            }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTPS_201_CREATED)
        self.assertTrue(Cliente.objects.filter(nome="Claudio Maia").exists())

        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_409_CONFLICT)

    def test_listar_cliente(self):
        url = "http://localhost:8000/clientes"
        Cliente.objects.create(
            nome="Claudio Maia",
            cpf="12345671245",
            telefone= 997654321
            )

        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTPS_200_OK)
        self.assertEqual(response.data[0]['nome'],3)

    def test_atualizar_cliente(self):
        url = f"http://localhost:8000/clientes/{self.novo_cliente.id}/"
        data = {
            "nome": "Maria Maia",
            "cpf": "12348671245",
            "telefone": 997655321
                }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status>HTTPS_200_OK)

        def teste_delet_cliente(self):
            url = f"http://localhost:8000/clientes/{self.novo_cliente.id}/"
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(Cliente.objects.filter(id=self.novo_cliente.id).exists())

class veiculoTesteCase(TestCase):
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
    def test_cadastrar_veiculo(self):
        url = "http://localhost:8000/veiculos"
        data = {
            "cliente": self.cliente.id,
            "modelo": "Toyota Corolla",
            "placa": "ABC1244",
            "cor": "Cinza",
            "tipo": "Carro"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTPS_201_CREATED)
        self.assertTrue(Cliente.objects.filter(placa="ABC1244").exists())

        response = self.client.post(url,data)
        self.assertEqual(response.status_code,status.HTTP_409_CONFLICT)

    def test_listar_veiculos(self):
        url = "http://localhost:8000/veiculos"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['placa'], "ABC1234")
    
    def test_atualizar_veiculo(self):
        url = f"http://localhost:8000/veiculos/{self.novo_veiculo.id}/"
        data = {
            "cliente" :self.cliente,
            "modelo" :"Toyota Corolla" 
            "placa" : "ABC1244"
            "cor" : "cinza" 
            "tipo" : "carro"
                }

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status>HTTPS_200_OK)

    def teste_delet_veiculo(self):
            url = f"http://localhost:8000/veiculos/{self.novo_veiculo.id}/"
            response = self.client.delete(url)
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertFalse(Cliente.objects.filter(id=self.novo_veiculo.id).exists())

class EstacionamentoTestecase(TestCase):
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
        url = "http://localhost:8000/veiculos"
            data = {
            "cliente": self.cliente.id,
            "veiculos": self.veiculo.id,
            "horario_entrada": timezone.now()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Estacionamento.objects.filter(cliente=self.cliente).exists())

    