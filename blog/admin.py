from django.contrib import admin
from .models import Agencia
from .models import Cliente
from .models import Garage
from .models import Vehiculo
from .models import Reservacion
from .models import ReservacionDetalle

class AdminAgencia(admin.ModelAdmin):
	list_display=["__str__","nombre","direccion"]
	class Meta:
		model=Agencia
admin.site.register(Agencia,AdminAgencia)

class AdminCliente(admin.ModelAdmin):
	list_display=["__str__","cedula","nombre","apellido","telefono","direccion"]
	class Meta:
		model=Cliente
admin.site.register(Cliente,AdminCliente)

class AdminGarage(admin.ModelAdmin):
	list_display=["__str__","codigo","cat_max_autos"]
	class Meta:
		model=Garage
admin.site.register(Garage,AdminGarage)

class AdminVehiculo(admin.ModelAdmin):
	list_display=["__str__","matricula","marca","tipo","modelo","anio","color","imagen","precio","estado","idAgencia","idGarage"]
	class Meta:
		model=Vehiculo
admin.site.register(Vehiculo,AdminVehiculo)

class AdminReservacionDetalle(admin.ModelAdmin):
	list_display=["fecha_inicio","fecha_final"]
	class Meta:
		model=ReservacionDetalle
admin.site.register(ReservacionDetalle,AdminReservacionDetalle)

