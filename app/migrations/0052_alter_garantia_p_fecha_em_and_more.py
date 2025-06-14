# Generated by Django 5.1.6 on 2025-05-15 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_alter_garantia_p_fecha_em_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garantia_p',
            name='fecha_em',
            field=models.DateField(default=datetime.date(2025, 5, 15), verbose_name='Fecha de Emision'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='fecha_entregado',
            field=models.DateField(default=datetime.date(2025, 5, 15), verbose_name='Fecha entregado'),
        ),
        migrations.AlterField(
            model_name='registro_ps',
            name='fecha_entregado',
            field=models.DateField(default=datetime.date(2025, 5, 15), verbose_name='Fecha entregado'),
        ),
    ]
