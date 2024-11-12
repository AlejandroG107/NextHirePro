# Generated by Django 4.2 on 2024-11-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('ID_TipoEmpresa', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Empresas',
            },
        ),
    ]