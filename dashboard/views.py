from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request)

    context = {}
    return render(request, 'dashboard/auth/login.html', context)

@login_required(login_url='user-login')
def home(request):
    context = {}
    return render(request, 'dashboard/admin-dash.html', context)
