from django.shortcuts import render
from .models import Curriculum, Empleos, Empleador
from django.http import HttpResponse
from .forms import EmpleadoForm, TrabajoForm, EmpleadorForm
from django import template


register = template.Library()

def estilizar_campo(campo, clase_css):
    return campo.as_widget(attrs={'class': clase_css})

def inicio(request):
    return render(request, "aplicacion/inicio.html")
#LOS TRES MODELOS TRABAJAN DE LA MISMA MANERA
#################################  EMPLEADO ############################################### 
#LLAMO LA CLASE PARA IMPORTAR TODOS LOS OBJETOS EN LA VARIABLE
#ADEMAS DE HACER EL FILTRADO POR 'NOMBRE' O POR LO QUE SE QUIERA BUSCAR, EN EL CASO DE EMPLEOS ES POR 'CARGO'
#ASI CON UNA FUNCION OBTENGO LOS DATOS DE LA CLASE Y RENDERIZAR TAMBIEN LA VARIABLE PARA FILTRAR LA BUSQUEDA
def lista_empleados(request):
    curriculums = Curriculum.objects.all()                          

    nombre_buscado = request.GET.get('nombre')
    if nombre_buscado:
        curriculums = curriculums.filter(nombre__icontains=nombre_buscado)

    return render(request, 'aplicacion/lista_empleados.html', {'curriculums': curriculums})
#PARA OBTENER LA ID DEL OBJETO Y RENDERIZARLO EN LA URL DEL DETALLE
def detalle_empleado(request, curriculum_id):
    curriculum = Curriculum.objects.get(pk=curriculum_id)
    return render(request, 'aplicacion/detalle_empleado.html', {'curriculum': curriculum})
# SE LLAMA A LA CLASE DEL FORM PARA RENDERIZARLA EN EL HTML DE IDA Y VUELTA, 
# COMPRUEVA SI LOS DATOS SON VALIDOS Y LOS GUARDA EN LA BASE DE DATOS AL IGUALARLO CON EL OBJETO DESEADO
def empleadoForm(request):
    if request.method == 'POST':
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado_nombre = miForm.cleaned_data.get('nombre')
            empleado_apellido = miForm.cleaned_data.get('apellido')
            empleado_presentacion = miForm.cleaned_data.get('presentacion')
            empleado_experiencia = miForm.cleaned_data.get('experiencia')
            empleado_estudios = miForm.cleaned_data.get('estudios')
            empleado = Curriculum(nombre=empleado_nombre,
                                  apellido=empleado_apellido,
                                  presentacion=empleado_presentacion,
                                  experiencia=empleado_experiencia,
                                  estudios=empleado_estudios,
                                  )
            empleado.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = EmpleadoForm()

    return render(request, "aplicacion/empleadoForm.html", {"form": miForm})



#################################  TRABAJOS ############################################### 

def lista_empleos(request):
    trabajos = Empleos.objects.all()

    trabajo_buscado = request.GET.get('cargo')
    if trabajo_buscado:
        trabajos = trabajos.filter(cargo__icontains=trabajo_buscado)
    return render(request, "aplicacion/lista_empleos.html", {'trabajos': trabajos})

def detalle_empleo(request, trabajo_id):
    trabajo = Empleos.objects.get(pk=trabajo_id)
    return render(request, 'aplicacion/detalle_empleo.html', {'trabajo': trabajo})


def trabajoForm(request):
    if request.method == 'POST':
        miForm = TrabajoForm(request.POST)
        if miForm.is_valid():
            trabajo_cargo = miForm.cleaned_data.get('cargo')
            trabajo_detalles = miForm.cleaned_data.get('detalles')
            trabajo_ubicacion = miForm.cleaned_data.get('ubicacion')
            trabajo_sueldo = miForm.cleaned_data.get('sueldo')
            trabajo = Empleos(cargo=trabajo_cargo,
                                  detalles=trabajo_detalles,
                                  ubicacion=trabajo_ubicacion,
                                  sueldo=trabajo_sueldo,
                                  )
            trabajo.save()
            return render(request, "aplicacion/base.html")

    else:
        miForm = TrabajoForm()

    return render(request, "aplicacion/trabajoForm.html", {"form": miForm})

################################# EMPLEADOR ############################################### 

def lista_empleadores(request):
    empleadores = Empleador.objects.all()

    empleador_buscado = request.GET.get('nombre')
    if empleador_buscado:
        empleadores = empleadores.filter(nombre__icontains=empleador_buscado)
    return render(request, "aplicacion/lista_empleadores.html", {'empleadores': empleadores})

def detalle_empleador(request, empleador_id):
    empleador = Empleador.objects.get(pk=empleador_id)
    return render(request, 'aplicacion/detalle_empleador.html', {'empleador': empleador})

def empleadorForm(request):
    if request.method == 'POST':
        miForm = EmpleadorForm(request.POST)
        if miForm.is_valid():
            empleador_nombre = miForm.cleaned_data.get('nombre')
            empleador_apellido = miForm.cleaned_data.get('apellido')
            empleador_edad = miForm.cleaned_data.get('edad')
            empleador_profesion = miForm.cleaned_data.get('profesion')
            empleador_nombreEmpresa = miForm.cleaned_data.get('nombreEmpresa')
            empleador = Empleador(nombre=empleador_nombre,
                                  apellido=empleador_apellido,
                                  edad=empleador_edad,
                                  profesion=empleador_profesion,
                                  nombreEmpresa=empleador_nombreEmpresa
                                  )
            empleador.save()
            return render(request, "aplicacion/inicio.html")

    else:
        miForm = EmpleadorForm()

    return render(request, "aplicacion/empleadorForm.html", {"form": miForm})

