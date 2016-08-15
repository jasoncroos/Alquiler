from __future__ import unicode_literals

from django.db import models

class Agencia(models.Model):
	nombre=models.CharField(max_length=50)
	direccion=models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Cliente(models.Model):
	cedula=models.CharField(max_length=10)
	nombre=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	telefono=models.CharField(max_length=10)
	direccion=models.CharField(max_length=50)

	def __str__(self):
		return self.cedula

class Garage(models.Model):
	codigo=models.CharField(max_length=20)
	cat_max_autos=models.IntegerField()

	def __str__(self):
		return self.codigo

class Vehiculo(models.Model):
	t_p=(
		("Chevrolet", "Chevrolet"),
		("Toyota", "Toyota"),
		("Hyundai", "Hyundai"),
		)

	t_q=(
		("Auto", "Auto"),
		("Camioneta", "Camioneta"),
		)

	t_r=(
		("Disponible", "Disponible"),
		("Ocupado", "Ocupado"),
		)
	
	matricula=models.CharField(max_length=20)
	marca=models.CharField(max_length=50,choices=t_p)
	tipo=models.CharField(max_length=50,choices=t_q)
	modelo=models.CharField(max_length=50)
	anio=models.IntegerField()
	color=models.CharField(max_length=20)
	imagen=models.ImageField(upload_to='photos', blank=True, null=True)
	precio=models.DecimalField(max_digits=20,decimal_places=2)
	estado=models.CharField(max_length=20,choices=t_r)
	idAgencia=models.ForeignKey(Agencia)
	idGarage=models.ForeignKey(Garage)


	def __str__(self):
		return self.matricula

class Reservacion(models.Model):
	precio=models.DecimalField(max_digits=100,decimal_places=2)
	idCliente=models.ForeignKey(Cliente)

class ReservacionDetalle(models.Model):
	fecha_inicio=models.CharField(max_length=30)
	fecha_final=models.CharField(max_length=30)
	idCliente=models.ForeignKey(Cliente)
