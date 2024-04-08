from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django import forms


from .models import CustomUser

# Forms goes here

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 


# Helper functions goes here
def login_if_valid(request, username, password):
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)


# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            login_if_valid(request, username, password)
            return redirect('dashboard:index')
        else:
            return render(request, 'users/register.html', {
                'form' : form
            })
    
    form = RegisterForm()
    return render(request, 'users/register.html', {
        'form' : form
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        login_if_valid(request, username, password)
        if request.user.is_authenticated:
            return redirect('dashboard:index')
        else:  
            return render(request, "users/login.html", {
                "message" : "Invalid Credentials!",
            })

    return render(request, "users/login.html")

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard:index')

    logout(request)
    return render(request, "users/login.html", {
        "message" : "Logged out!",
    })

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard:index')
    
    return render(request, "users/profile.html", {
        "form" : RegisterForm()
    })