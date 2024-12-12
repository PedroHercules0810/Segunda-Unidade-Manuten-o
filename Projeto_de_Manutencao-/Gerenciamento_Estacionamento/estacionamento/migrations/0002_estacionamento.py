from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_entrada', models.DateTimeField(auto_now_add=True)),
                ('horario_saida', models.DateTimeField(null=True)),
                ('clienete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.cliente')),
                ('veiculos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamento.veiculo')),
            ],
        ),
    ]
