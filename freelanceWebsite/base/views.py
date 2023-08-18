from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


# Create your views here.


def home(request):
    return render(request, "base/home.html", {})

@login_required(login_url='register')
def vacancies(request):
    vacansy = Vacansy.objects.all()
    context = {'vacansy':vacansy}
    return render(request,'base/allVacancies.html',context)


def registerPage(request):
    form = UserCreationForm()
    context = {"form": form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Введите другой ник или проверьте пароли")
    return render(request, "base/login_register.html", context)


def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("pass")
        try:
            user = User.objects.get(username=username)
        except Exception:
            messages.error(request, "User doesnt exists")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "User doesnt exists")
    context = {"page": page}
    return render(request, "base/login_register.html", context)


def logoutPage(request):
    logout(request)
    return redirect("home")


@login_required(login_url='register')
def createVacansy(request):
    if request.method == "POST":
        vacansy = Vacansy.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
            host=request.user
        )
    context = {}
    return render(request, "base/createVacansy.html", context)


# @login_required(login_url='register')
# def updateVacansy(request):
    

