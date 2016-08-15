from django import forms
from .models import Vehiculo
from .models import Cliente
from .models import ReservacionDetalle

class FormularioVehiculo(forms.ModelForm):
	class Meta:
		model=Vehiculo
		fields=["matricula","marca","tipo","modelo","anio","color","imagen","precio","estado","idAgencia","idGarage"]

class FormularioVehiculoN(forms.ModelForm):
	class Meta:
		model=Vehiculo
		fields=["matricula","marca","tipo","modelo","anio","color","imagen","precio","estado","idAgencia","idGarage"]

class FormularioPersona(forms.ModelForm):
	class Meta:
		model=Cliente
		fields=["cedula","nombre","apellido","telefono","direccion"]

class FormularioReservacionDetalle(forms.ModelForm):
	class Meta:
		model=ReservacionDetalle
		fields=["fecha_inicio","fecha_final"]