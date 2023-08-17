from django import forms
#SECCION DE FORM PARA QUE NO SE EXTIENDA EL VIEW Y SEA MAS LEGIBLE
#A TRAVES DE WIDGET Y LOS ATRIBUTOS SE EDITAN LA VISTA DE LOS FORMULARIOS
class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su apellido'}))
    presentacion = forms.CharField(max_length=256, required=True, 
                                   label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su presentacion',"style":"height: 10rem"}))
    experiencia = forms.CharField(max_length=256, required=True, 
                                  label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese sus experiencias',"style":"height: 10rem"}))
    estudios = forms.CharField(max_length=256, required=True,
                               label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese sus estudios',"style":"height: 10rem"}))
    

class TrabajoForm(forms.Form):
    cargo = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el cargo'}))
    detalles = forms.CharField(max_length=256, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese los detalles',"style":"height: 10rem"}))
    ubicacion = forms.CharField(max_length=50, required=True, 
                                   label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese la ubicacion'}))
    sueldo = forms.CharField(max_length=50, required=True, 
                                  label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el sueldo'}))
    
class EmpleadorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, 
                             label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su nombre'}))
    apellido = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su apellido'}))
    edad = forms.IntegerField(required=True, 
                                   label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su edad'}))
    profesion = forms.CharField(max_length=50, required=True, 
                                  label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese su profesion'}))
    nombreEmpresa = forms.CharField(max_length=50, required=True, 
                                label='', widget=forms.TextInput(attrs={ 'class': "form-control", 'placeholder': 'Ingrese el nombre de la empresa'}))

