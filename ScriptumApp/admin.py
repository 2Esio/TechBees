from django.contrib import admin
from .models import (
    User, 
    Group, 
    Profile, 
    AdminInvitation, 
    StudentInvitation, 
    StudentRegistration
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_verified')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('role', 'is_verified')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'admin', 'created_at')
    search_fields = ('name', 'code')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'is_approved')
    list_filter = ('is_approved',)

@admin.register(AdminInvitation)
class AdminInvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'invited_by', 'is_accepted')
    list_filter = ('is_accepted',)

@admin.register(StudentInvitation)
class StudentInvitationAdmin(admin.ModelAdmin):
    list_display = ('email', 'group', 'is_accepted')
    list_filter = ('is_accepted',)

@admin.register(StudentRegistration)
class StudentRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved')
    list_filter = ('is_approved',)