from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms improt SignUpForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Account Created successfully!")
            return redirect('dashboard')
    else:
        form = SignUpForm()

    return render(request, 'authentication/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Username or Password")
    return render(request, "authentication/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('login')