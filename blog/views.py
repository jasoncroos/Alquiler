from django.shortcuts import render,redirect
from .forms import FormularioVehiculo
from .forms import FormularioVehiculoN
from .forms import FormularioPersona
from .forms import FormularioReservacionDetalle
from .models import Vehiculo
from .models import Cliente

from django.http import HttpResponseRedirect,HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib.auth import login,authenticate,logout

from django.contrib.auth.decorators import login_required

def listarvehiculos(request):
	vehiculos=Vehiculo.objects.all()
	v=Vehiculo()
	context={
		'vehiculos':vehiculos,
	}
	return render(request,"listarvehiculos.html",context) 

def mensaje1(request):
	return render(request,"mensaje1.html",{})

def iniciosesion(request):
	if not request.user.is_anonymous():
		return redirect(listarvehiculos)
	if request.method=='POST':
		finicio=AuthenticationForm(request.POST)
		if finicio.is_valid:
			username=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=username, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return redirect(listarvehiculos)
				else:
					return HttpResponseRedirect("/blog/iniciosesion/");
			else:
				return HttpResponseRedirect("/blog/mensaje/");
	else:
		finicio=AuthenticationForm()
		return render_to_response('login.html',{'finicio':finicio},context_instance=RequestContext(request))

def crearusuario (request):
	fp=FormularioPersona(request.POST or None)
	if request.method == 'POST':
		 finicio=UserCreationForm(request.POST)
		 if finicio.is_valid():
		 	if fp.is_valid():
			 	datos=fp.cleaned_data
				p=Cliente()
				p.cedula=datos.get("cedula")
				p.nombre=datos.get("nombre")
				p.apellido=datos.get("apellido")
				p.telefono=datos.get("telefono")
				p.direccion=datos.get("direccion")
				p.save()

		 	finicio.save()
		 	return redirect(iniciosesion)
		 else:
		 	return HttpResponseRedirect("/blog/mensaje1/");
	else:
		finicio=UserCreationForm()
	return render_to_response('nuevousuario.html',{'finicio':finicio,'fp':fp},context_instance=RequestContext(request))

def cerrarsesion(request):
	logout(request)
	return redirect(iniciosesion)

def mensaje(request):
	return render(request,"mensaje.html",{})

def registrarvehiculo(request):
	fv=FormularioVehiculo(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if fv.is_valid():
			datos=fv.cleaned_data
			v=Vehiculo()
			v.matricula=datos.get("matricula")
			v.marca=datos.get("marca")
			v.tipo=datos.get("tipo")
			v.modelo=datos.get("modelo")
			v.anio=datos.get("anio")
			v.color=datos.get("color")
			v.imagen=datos.get("imagen")
			v.precio=datos.get("precio")
			v.estado=datos.get("estado")
			v.idAgencia=datos.get("idAgencia")
			v.idGarage=datos.get("idGarage")
			if v.save() != True:
				return redirect(listarvehiculos)
	context={
		'fv':fv,
	}
	return render(request,"registrarvehiculo.html",context)

def modificar (request):
	fv=FormularioVehiculoN(request.POST or None, request.FILES or None)
	matricula=request.GET['matricula']
	m=Vehiculo.objects.get(matricula=matricula)
	fv.fields["matricula"].initial=m.matricula
	fv.fields["marca"].initial=m.marca
	fv.fields["tipo"].initial=m.tipo
	fv.fields["modelo"].initial=m.modelo
	fv.fields["anio"].initial=m.anio
	fv.fields["color"].initial=m.color
	fv.fields["imagen"].initial=m.imagen
	fv.fields["precio"].initial=m.precio
	fv.fields["estado"].initial=m.estado
	fv.fields["idAgencia"].initial=m.idAgencia
	fv.fields["idGarage"].initial=m.idGarage
	if fv.is_valid():
			datos=fv.cleaned_data
			m.matricula=datos.get("matricula")
			m.marca=datos.get("marca")
			m.tipo=datos.get("tipo")
			m.modelo=datos.get("modelo")
			m.anio=datos.get("anio")
			m.color=datos.get("color")
			m.imagen=datos.get("imagen")
			m.precio=datos.get("precio")
			m.estado=datos.get("estado")
			m.idAgencia=datos.get("idAgencia")
			m.idGarage=datos.get("idGarage")

			if m.save() != True:
				return redirect(listarvehiculos)
	context={
		'fv':fv,
	}
	return render(request,"modificar.html",context)

def eliminar(request):
	v=Vehiculo.objects.get(id=request.GET['id'])
	v.delete()
	return redirect(listarvehiculos)

def listVehiculos(request):
	queryset=Vehiculo.objects.all()
	queryset=serializers.serialize('json',queryset)
	return HttpResponse(queryset, content_type='application/json')

def reservacionDetalle(request):
	fr=FormularioReservacionDetalle(request.POST or None)
	if request.method == 'POST':
		if fr.is_valid():
			datos=fr.cleaned_data
			r=Reservacion()
			r.fecha_inicio=datos.get("fecha_inicio")
			r.fecha_final=datos.get("fecha_final")
			if r.save() != True:
				return redirect(listarvehiculos)
	context={
		'fr':fr,
	}
	return render(request,"listarvehiculos.html",context)