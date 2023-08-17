from django.urls import path, include
from .views import *
#SEPARE DE 3 CADA URL PARA TENER MAS ORGANIZADO CADA MODELO. EMPLEADO EMPLEADOR EMPLEO
urlpatterns = [
    path('inicio/', inicio, name="home"),
    
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('empleado/<int:curriculum_id>/', detalle_empleado, name='detalle_empleado'),
    path('empleadoForm/', empleadoForm, name='empleadoForm'),

    path('lista_empleos/', lista_empleos, name='lista_empleos'),
    path('trabajo/<int:trabajo_id>/', detalle_empleo, name='detalle_empleo'),
    path('trabajoForm/', trabajoForm, name='trabajoForm'),

    path('lista_empleadores/', lista_empleadores, name='lista_empleadores'),
    path('empleador/<int:empleador_id>/', detalle_empleador, name='detalle_empleador'),
    path('empleadorForm/', empleadorForm, name='empleadorForm'),

]