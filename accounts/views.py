from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.

#User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form':form})

#user regisration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:dashboard')
    else:
        form = UserCreationForm()
    return render(request, "accounts/user_registration.html", {'form':form})


def user_logout(request):
    auth_logout(request)
    return redirect('/')




def dashboard(request):
    return render(request, "accounts/dashboard.html")