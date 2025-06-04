from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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