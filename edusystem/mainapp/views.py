from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # nanti kita buat view ini
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def dashboard_mahasiswa(request):
    return render(request, 'mainapp/mahasiswa_home.html')

def dashboard_dosen(request):
    return render(request, 'mainapp/dosen_home.html')

def home(request):
    return render(request, 'mainapp/home.html')

@login_required
def dashboard(request):
    if request.user.role == 'mahasiswa':
        return redirect('dashboard_mahasiswa')
    elif request.user.role == 'dosen':
        return redirect('dashboard_dosen')
    else:
        return redirect('home')  # fallback
