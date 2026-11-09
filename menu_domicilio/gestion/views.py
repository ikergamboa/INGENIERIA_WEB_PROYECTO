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
        # 1. Recogemos los campos del formulario HTML
        username_val = request.POST.get('username', '').strip()
        email_val = request.POST.get('email', '').strip()
        password_val = request.POST.get('password', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        direccion = request.POST.get('direccion', '').strip()

        # 2. Comprobamos si el nombre de usuario ya existe
        if User.objects.filter(username=username_val).exists():
            return render(request, 'gestion/registro.html', {
                'error': 'El nombre de usuario ya está registrado.'
            })

        # 3. Creamos el User de Django y lo guardamos en la variable 'nuevo_user'
        nuevo_user = User.objects.create_user(
            username=username_val, 
            email=email_val, 
            password=password_val
        )

        cliente = Cliente.objects.get(usuario=nuevo_user)
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.save()

        # 5. Redirigimos a la confirmación de éxito
        return redirect('gestion:registro_exito')

    return render(request, 'gestion/registro.html')

def registro_exito(request):
    return render(request, 'gestion/registro_exito.html')

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