from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import NewUserForm

def newuser(response):
    if response.method == 'POST':
        form = NewUserForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('users/')
            
    else:
        form = NewUserForm()
    return render(response, 'register/newuser.html', {'form': form})

def loggedout(response):
    return render(response, 'register/loggedout.html', {})