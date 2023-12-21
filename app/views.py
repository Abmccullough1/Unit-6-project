from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def register(request):
    form = CreateUserForm()
    print(request.method)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'register.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect')
    return render(request, 'login.html')


def homepage(request):
    return render(request, 'home.html')