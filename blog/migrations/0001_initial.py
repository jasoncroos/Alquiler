# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-07 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('cat_max_autos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=100)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ReservacionDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.CharField(max_length=30)),
                ('fecha_final', models.CharField(max_length=30)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('marca', models.CharField(choices=[('Chevrolet', 'Chevrolet'), ('Toyota', 'Toyota'), ('Hyundai', 'Hyundai')], max_length=50)),
                ('tipo', models.CharField(choices=[('Auto', 'Auto'), ('Camioneta', 'Camioneta')], max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='photos')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado')], max_length=20)),
                ('idAgencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Agencia')),
                ('idGarage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Garage')),
            ],
        ),
    ]
