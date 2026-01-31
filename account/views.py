from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm_password') 
        register_error = False

        if User.objects.filter(username=username).exists():
            register_error = True
            messages.error(request, "Username already exists")

        if User.objects.filter(email=email).exists():
            register_error = True
            messages.error(request, "Email already exists")

        if len(password) < 5:
            register_error = True
            messages.error(request, "Password must be at least 5 characters")
        if password != cpassword:
            register_error = True
            messages.error(request, "Passwords do not match")

        if register_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                email=email, 
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')

        

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        # email=request.POST.get('email')
        username=request.POST.get('username')

        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def shorten_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        # Here you would add the logic to shorten the URL
        messages.success(request, f"URL shortened: {url}")
        return redirect('home')
    return render(request, 'shorten_url.html')