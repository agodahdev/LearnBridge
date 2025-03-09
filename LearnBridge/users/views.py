from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm
from courses.models import Enrollment

# Register a new user
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# User login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

# User logout
def user_logout(request):
    logout(request)
    return redirect('login')

# User dashboard (Shows enrolled courses)
@login_required
def dashboard(request):
    enrolled_courses = Enrollment.objects.filter(user=request.user)  # ✅ Fetch courses correctly
    return render(request, 'users/dashboard.html', {'enrolled_courses': enrolled_courses})

# User profile page
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})