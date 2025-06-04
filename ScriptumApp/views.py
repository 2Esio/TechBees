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