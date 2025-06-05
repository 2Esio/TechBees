from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('admin-login/', views.admin_login_view, name='admin_login'),  # Nueva URL
    path('about/', views.about_view, name='about'),
    path('group/', views.group_view, name='group'),
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('update-description/', views.update_description, name='update_description'),
]