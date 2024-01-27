from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'auth/signup.html', {'username': username})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'auth/signup.html', {'username': username})

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Signup successful. Welcome!')

        return redirect('/')

    return render(request, 'auth/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return render(request, 'auth/login.html', {'message': 'invalid credential'})

    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'core/index.html', {'massage': 'Logout successful'})