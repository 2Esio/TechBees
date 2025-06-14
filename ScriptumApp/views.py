from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

def landing_page(request):
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')
        codigo_grupo = request.POST.get('codigo')
        
        user = authenticate(request, username=nombre, password=password)
        
        if user is not None:
            # Verificar el código de grupo aquí si es necesario
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard después del login
        else:
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Aquí irá la lógica de registro
        pass
    return render(request, 'register.html')

def admin_login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin:index')
        else:
            messages.error(request, 'Credenciales inválidas o usuario no es administrador')
    
    return render(request, 'admin_login.html')

def about_view(request):
    return render(request, 'about.html')

def group_view(request):
    return render(request, 'group.html')

def profile_view(request, id):
    # Diccionario de perfiles (esto podría venir de una base de datos)
    profiles = {
        1: {
            'profile_image': 'images/irvin.jpg',
            'profile_name': 'Irvin Javier Cruz Gonzalez',
            'description': 'Descripción del perfil...',
            'awards': 'Lista de premios...'
        },
        2: {
            'profile_image': 'images/ixchel.png',
            'profile_name': 'Ixchel',
            'description': 'Descripción del perfil...',
            'awards': 'Lista de premios...'
        },
        3: {
            'profile_image': 'images/jimena.png',
            'profile_name': 'Jimena Ugalde Flores',
            'description': 'Descripción del perfil...',
            'awards': 'Lista de premios...'
        },
        4: {
            'profile_image': 'images/marco.png',
            'profile_name': 'Marco Flores Cid',
            'description': 'Descripción del perfil...',
            'awards': 'Lista de premios...'
        }
    }
    
    profile_data = profiles.get(id, {
        'profile_image': 'images/default-profile.png',
        'profile_name': 'Usuario no encontrado',
        'description': 'No hay descripción disponible',
        'awards': 'Sin premios'
    })
    
    # Agregar el id del perfil al contexto
    profile_data['profile_id'] = id

    return render(request, 'profile.html', profile_data)

@require_http_methods(["POST"])
def update_description(request):
    try:
        data = json.loads(request.body)
        profile_id = data.get('profile_id')
        new_description = data.get('description')
        
        # Actualizar la descripción en el diccionario de perfiles
        profiles = {
            1: {
                'profile_image': 'images/irvin.jpg',
                'profile_name': 'Irvin Javier Cruz Gonzalez',
                'description': new_description,  # Actualización aquí
                'awards': 'Lista de premios...'
            },
            2: {
                'profile_image': 'images/ixchel.png',
                'profile_name': 'Ixchel',
                'description': new_description if profile_id == 2 else 'Descripción del perfil...',
                'awards': 'Lista de premios...'
            },
            3: {
                'profile_image': 'images/jimena.png',
                'profile_name': 'Jimena Ugalde Flores',
                'description': new_description if profile_id == 3 else 'Descripción del perfil...',
                'awards': 'Lista de premios...'
            },
            4: {
                'profile_image': 'images/marco.png',
                'profile_name': 'Marco Flores Cid',
                'description': new_description if profile_id == 4 else 'Descripción del perfil...',
                'awards': 'Lista de premios...'
            }
        }

        # En una implementación real, aquí actualizarías la base de datos
        # Por ahora solo devolvemos una respuesta exitosa
        return JsonResponse({
            'status': 'success',
            'description': new_description
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

