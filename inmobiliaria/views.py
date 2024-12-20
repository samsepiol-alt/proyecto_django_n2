from django.shortcuts import render, redirect
from .forms import UserRegisterForm, PerfilModelForm, DireccionModelForm
from django.contrib import messages

#vista principal
def index(request):
    context = {}
    return render(request,'inmobiliaria/index.html',context)


#Vistas de usuario y autenticacion
def sign_in(request):
    pass

def sign_out(request):
    pass

def register(request):
    context = {'user_form':UserRegisterForm,'perfil_form':PerfilModelForm, 'addr_form':DireccionModelForm}
    if request.method == 'GET':
        return render(request, 'profile/register.html',context)
    elif request.method =='POST':
        user_form = UserRegisterForm(request.POST)
        perfil_form = PerfilModelForm(request.POST)
        addr_form = DireccionModelForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid() and addr_form.is_valid():
            # Guardar el formulario de usuario
            user = user_form.save()
            direccion =addr_form.save()
            # Asignar el usuario al perfil
            perfil = perfil_form.save(commit=False)
            perfil.direccion = direccion
            perfil.usuario = user
            perfil.save()
            
            # Mensaje de éxito
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login') 
    else:
        return render(request,'404.html',status=404)

#vistas de perfil
def profile(request):
    pass
def edit_profile(request):
    pass
def delete_profile(request):
    pass

#vistas inmueble

def inmueble(request):
    pass

def editar_inmueble(request,id):
    pass

def crear_inmueble(request):
    pass

def eliminar_inmueble(request):
    pass
