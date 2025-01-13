from estacionamento.models import Estacionamento

class EstacionamentoService:

    def create(self, data):
        novo_estacionamento = Estacionamento.objects.create(
            cliente = data['cliente'],
            veiculos = data['veiculos'],
            horario_entrada = data['horario_entrada'],
            horario_saida = data['horario_Saida']
        )
        
        return novo_estacionamento