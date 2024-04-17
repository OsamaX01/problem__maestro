from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import RegisterForm, EditProfileForm

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
                "messages" : ["Invalid Credentials!"],
            })

    return render(request, "users/login.html")

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard:index')

    logout(request)
    messages.success(request, "Logged out!")
    return redirect('dashboard:index')

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('dashboard:index')
    
    return render(request, "users/profile.html", {
        "form" : RegisterForm()
    })

def edit_profile(request):
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('users:profile')
        else:
            return render(request, 'users/edit_profile.html', {
                'form': user_form
            })        
        
    user_form = EditProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {
        'form': user_form
    })