# Generated by Django 5.0.4 on 2024-04-26 00:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoqueADS', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='categoria',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='estoqueADS.categoria'),
            preserve_default=False,
        ),
    ]
