from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')


def Forgotpassword(request):
    return render(request, 'forgotpassword.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   # logs user in
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check passwords
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # Save user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now login.")
        return redirect('login')  # Make a login page later

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Log the user in
            messages.success(request, f"Welcome {username}!")
            return redirect('home')  # Replace with your home page
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

