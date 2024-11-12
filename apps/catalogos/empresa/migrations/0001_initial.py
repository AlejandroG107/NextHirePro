# Generated by Django 4.2 on 2024-11-09 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
        ('tipo_empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('ID_Empresa', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo', models.CharField(max_length=50, unique=True, verbose_name='Código')),
                ('Nombre_Empresa', models.CharField(max_length=100, verbose_name='Nombre Empresa')),
                ('Direccion', models.CharField(max_length=200, verbose_name='Dirección')),
                ('Telefono', models.CharField(max_length=16, verbose_name='Teléfono')),
                ('Correo', models.CharField(max_length=100, verbose_name='Correo Electrónico')),
                ('ID_Municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='municipio.municipio', verbose_name='Municipio')),
                ('ID_TipoEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tipo_empresa.tipoempresa', verbose_name='Tipo Empresa')),
            ],
            options={
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]