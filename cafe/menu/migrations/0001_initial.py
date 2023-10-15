# Generated by Django 4.2.6 on 2023-10-14 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('order', models.IntegerField(verbose_name='Orden de presentacion')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Alimento')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Costo')),
                ('previous_cost', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Costo')),
                ('recommended', models.BooleanField(default=False, verbose_name='Recomendado')),
                ('order', models.IntegerField(verbose_name='Orden de presentacion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='Menu')),
            ],
            options={
                'verbose_name': 'Alimento',
                'verbose_name_plural': 'Alimento',
                'ordering': ['order'],
            },
        ),
    ]