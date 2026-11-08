from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from pedidos.models import Cliente
from catalogo.models import Plato
from .forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.admin.views.decorators import staff_member_required
from catalogo.forms import PlatoForm

def registro(request):
    if request.method == 'POST':
        # Bound form (con datos enviados por el usuario)
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Procesamos y extraemos los datos limpios
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            telefono = form.cleaned_data['telefono']
            direccion = form.cleaned_data['direccion']
            
            # Guardamos en la base de datos (Usuario de Django + Perfil Cliente)
            user = User.objects.create_user(username=username, email=email, password=password)
            Cliente.objects.create(usuario=user, telefono=telefono, direccion=direccion)
            
            return redirect('menus_disponibles')
    else:
        # Unbound form (formulario vacío para peticiones GET)
        form = RegistroForm()
        
    return render(request, 'gestion/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verificamos si las credenciales son correctas con el sistema de Django
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Si el usuario existe y la contraseña es correcta, iniciamos sesión
                login(request, user)
                return redirect('catalogo:menus_disponibles')
            else:
                # Si falla, podemos añadir un error general al formulario
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        form = LoginForm()
        
    return render(request, 'gestion/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('gestion:login')

@staff_member_required
def panel_cocina(request):
    platos = Plato.objects.all()
    return render(request, 'gestion/panel_cocina.html', {'platos': platos})

@staff_member_required
def crear_plato(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:panel_cocina')
    else:
        form = PlatoForm()
    return render(request, 'gestion/form_plato.html', {'form': form, 'titulo': 'Añadir Nuevo Plato'})

@staff_member_required
def editar_plato(request, plato_id):
    plato = get_object_or_404(Plato, pk=plato_id)
    if request.method == 'POST':
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect('gestion:panel_cocina')
    else:
        form = PlatoForm(instance=plato)
    return render(request, 'gestion/form_plato.html', {'form': form, 'titulo': f'Editar Plato: {plato.nombre}'})

@staff_member_required
def borrar_plato(request, plato_id):
    plato = get_object_or_404(Plato, pk=plato_id)
    if request.method == 'POST':
        plato.delete()
        return redirect('gestion:panel_cocina')
    return render(request, 'gestion/confirmar_borrado.html', {'plato': plato})