# Generated by Django 4.2.6 on 2023-10-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='previous_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Costo Previo'),
        ),
    ]
