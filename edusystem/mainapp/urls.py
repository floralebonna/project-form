from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/mahasiswa/', views.dashboard_mahasiswa, name='dashboard_mahasiswa'),
    path('dashboard/dosen/', views.dashboard_dosen, name='dashboard_dosen'),
]