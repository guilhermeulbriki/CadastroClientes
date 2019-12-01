# Generated by Django 2.2.6 on 2019-10-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=350, verbose_name='Endereço')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=255, verbose_name='CPF')),
            ],
        ),
    ]
