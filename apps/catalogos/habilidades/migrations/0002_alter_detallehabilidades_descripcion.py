# Generated by Django 4.2 on 2024-11-09 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallehabilidades',
            name='Descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripcion'),
        ),
    ]