from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def profile(request):
    return render(request, 'profile.html')


# LOGOUT

def user_logout(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully!"
    )

    return redirect('login')


# HOME

@login_required
def home(request):

    return render(
        request,
        'Portfolio.html'
    )


# =========================================================
# FORGOT PASSWORD


def Forgotpassword(request):

    return render(
        request,
        'forgotpassword.html'
    )


# LOGIN

def user_login(request):

    if request.method == "POST":

        username = request.POST.get(
            'username',
            ''
        ).strip()

        password = request.POST.get(
            'password',
            ''
        )


        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            auth_login(
                request,
                user
            )

            messages.success(
                request,
                f"Welcome {username}!"
            )

            return redirect('home')


        else:

            messages.error(
                request,
                "Invalid username or password."
            )

            return redirect('login')


    return render(
        request,
        'login.html'
    )


# =========================================================
# REGISTER
# =========================================================

def register(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username',
            ''
        ).strip()

        email = request.POST.get(
            'email',
            ''
        ).strip()

        password = request.POST.get(
            'password',
            ''
        )

        confirm_password = request.POST.get(
            'confirm_password',
            ''
        )


        # =================================================
        # CHECK EMPTY FIELDS
        # =================================================

        if not username or not email or not password or not confirm_password:

            messages.error(
                request,
                "Please fill in all fields."
            )

            return redirect('register')


        # =================================================
        # CHECK USERNAME
        # =================================================

        if User.objects.filter(
            username__iexact=username
        ).exists():

            messages.error(
                request,
                "Username already exists. Please choose another username."
            )

            return redirect('register')


        # =================================================
        # CHECK EMAIL
        # =================================================

        if User.objects.filter(
            email__iexact=email
        ).exists():

            messages.error(
                request,
                "This email is already registered."
            )

            return redirect('register')


        # =================================================
        # CHECK PASSWORD
        # =================================================

        if password != confirm_password:

            messages.error(
                request,
                "Passwords do not match."
            )

            return redirect('register')


        # =================================================
        # PASSWORD LENGTH
        # =================================================

        if len(password) < 8:

            messages.error(
                request,
                "Password must be at least 8 characters long."
            )

            return redirect('register')


        # =================================================
        # CREATE USER
        # =================================================

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )


        # =================================================
        # SUCCESS
        # =================================================

        messages.success(
            request,
            "Registration successful! You can now login."
        )

        return redirect('login')


    # =====================================================
    # GET REQUEST
    # =====================================================

    return render(
        request,
        'register.html'
    )