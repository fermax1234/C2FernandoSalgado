from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Propuesta
from .forms import PropuestaForm
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from .models import Proyecto
from .models import Propuesta

# Create your views here.
def paginita(request):
    return render(request, 'core/pagina.html')

def logout(request):
    auth_logout(request)
    return redirect('home')
######

@login_required
def ingreso_propuesta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        # Aquí obtenemos el usuario actualmente autenticado
        usuario = request.user
        # Creamos una nueva instancia de Propuesta con los datos del formulario
        propuesta = Propuesta(titulo=titulo, descripcion=descripcion, usuario=usuario)
        # Guardamos la propuesta en la base de datos
        propuesta.save()
        # Redireccionamos a alguna página después de guardar la propuesta
        return redirect('pagina_de_confirmacion')  # Cambia 'pagina_de_confirmacion' por la URL a la que quieras redireccionar después de guardar la propuesta
    else:
        return render(request, 'pagina.html')


def redireccion(request):
    return render(request, 'redirecciom.html')
#####
def projects(request):
    # Recupera todos los proyectos desde la base de datos
    proyectos = Proyecto.objects.all()
    # Imprime los proyectos recuperados para verificar
    print(proyectos)
    # Pasa los proyectos al contexto de la plantilla
    return render(request, 'core/pagina.html', {'proyectos': proyectos})

##


def my_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ingreso_propuesta')  # Redirecciona a la página principal
        else:
            # Handle invalid login
            pass
    return render(request, 'redireccion')


