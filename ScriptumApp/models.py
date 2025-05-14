from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid


class CustomUserManager(BaseUserManager):
    """Define un administrador de modelo para Usuario con email como identificador único."""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Email es obligatorio'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser debe tener is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser debe tener is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Modelo de usuario personalizado con email como identificador principal."""
    
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('STUDENT', 'Estudiante'),
    )
    
    username = None
    email = models.EmailField(_('Correo electrónico'), unique=True)
    first_name = models.CharField(_('Nombre'), max_length=150)
    last_name = models.CharField(_('Apellidos'), max_length=150)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):
    """Modelo para los grupos de estudiantes."""
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='administered_groups')
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class Profile(models.Model):
    """Modelo para el perfil de estudiante."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    description = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Perfil de {self.user}"


class AdminInvitation(models.Model):
    """Modelo para invitaciones de administradores."""
    
    email = models.EmailField()
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_invitations')
    code = models.CharField(max_length=50, unique=True)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Invitación para {self.email}"


class StudentInvitation(models.Model):
    """Modelo para invitaciones de estudiantes a grupos."""
    
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='invitations')
    code = models.CharField(max_length=50, unique=True)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Invitación a {self.email} para {self.group.name}"


class StudentRegistration(models.Model):
    """Modelo para solicitudes de registro de estudiantes pendientes de aprobación."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Registro de {self.user.email}"