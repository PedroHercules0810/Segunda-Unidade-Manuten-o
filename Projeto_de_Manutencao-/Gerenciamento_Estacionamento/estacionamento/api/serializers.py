from rest_framework import serializers
from estacionamento.models import Cliente, Veiculo, Estacionamento

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente  
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo  
        fields = '__all__'


class EstacionamentoSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Estacionamento
        fields = [
            'id', 'horario_entrada', 'horario_saida', 'valor_pagamento',
            'cliente', 'veiculos'
        ]

    def get_valor_pagamento(self, obj):
      
        if obj.horario_entrada and obj.horario_saida:
          
            duracao_em_minutos = (obj.horario_saida - obj.horario_entrada).total_seconds() / 60
            intervalos = round(duracao_em_minutos / 60) 
            return intervalos * 7  
        return 0

    def to_representation(self, instance):
        
        representation = super().to_representation(instance)

     
        if instance.horario_entrada and not instance.horario_saida:
            representation['horario_entrada'] = f"{instance.horario_entrada} - Vaga ocupada"
        if instance.horario_saida:
            representation['horario_saida'] = f"{instance.horario_saida} - Vaga liberada"

        return representation

    def validate(self, data):
       
        horario_entrada = data.get('horario_entrada')
        horario_saida = data.get('horario_saida')

        if horario_entrada and horario_saida:
            if horario_entrada >= horario_saida:
                raise serializers.ValidationError("O horário de saída deve ser posterior ao horário de entrada.")
        
        return data
