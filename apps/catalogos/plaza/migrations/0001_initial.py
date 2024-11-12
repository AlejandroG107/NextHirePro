# Generated by Django 4.2 on 2024-11-09 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cargo', '0001_initial'),
        ('empresa', '0001_initial'),
        ('area_plaza', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('ID_Plaza', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo', models.CharField(max_length=16, verbose_name='Código Plaza')),
                ('Salario', models.FloatField(verbose_name='Salario')),
                ('Descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('ID_AreaPLAZA', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_plaza.areaplaza', verbose_name='AreaPlaza')),
                ('ID_Cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cargo.cargo', verbose_name='Cargo')),
                ('ID_Empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresa.empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name_plural': 'Plazas',
            },
        ),
        migrations.CreateModel(
            name='DetallePlaza',
            fields=[
                ('ID_DetallePlaza', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('Id_Plaza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='detalles', to='plaza.plaza', verbose_name='Plaza')),
            ],
            options={
                'verbose_name_plural': 'Detalles de Plazas',
            },
        ),
    ]
