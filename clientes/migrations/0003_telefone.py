# Generated by Django 3.0.3 on 2020-02-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200210_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=13)),
                ('descricao', models.CharField(max_length=80)),
            ],
        ),
    ]