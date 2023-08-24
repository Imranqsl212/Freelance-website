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
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *



def home(request):
    return render(request, "base/home.html", {})


@login_required(login_url="register")
def vacancies(request):
    vacansy = Vacansy.objects.all()
    participants_count = 0
    for j in vacansy:
        participants_count = j.participants.all().count()
    context = {"vacansy": vacansy, "participants_count": participants_count}
    return render(request, "base/allVacancies.html", context)


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


@login_required(login_url="register")
def logoutPage(request):
    logout(request)
    return redirect("home")


@login_required(login_url="register")
def createVacansy(request):
    if request.method == "POST":
        vacansy = Vacansy.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            price=request.POST.get("price"),
            host=request.user,
        )
    context = {}
    return render(request, "base/createVacansy.html", context)


@login_required(login_url="register")
def updateVacansy(request, pk):
    vacansy = Vacansy.objects.get(id=pk)
    if request.user != vacansy.host:
        return HttpResponse("You arent owner of a room")
    if request.method == "POST":
        vacansy.title = request.POST.get("title")
        vacansy.description = request.POST.get("description")
        vacansy.price = request.POST.get("price")
        vacansy.host = request.user
        vacansy.save()
        return redirect("home")
    context = {}
    return render(request, "base/createVacansy.html", context)


@login_required(login_url="register")
def deleteVacansy(request, pk):
    vacansy = Vacansy.objects.get(id=pk)
    if request.user != vacansy.host:
        return HttpResponse("You arent owner of a room")
    if request.method == "POST":
        vacansy.delete()
        return redirect("home")
    return HttpResponse(
        '<h1>You deleted vacansy</h1> <a href="{% url "home" %}">Go back</a>'
    )


# @login_required(login_url='register')
# def doneVacansy(request):


@login_required(login_url="register")
def vacansyDetail(request, pk):
    vacansy = Vacansy.objects.get(id=pk)
    return render(request, "base/vacansyDetail.html", {"vacansy": vacansy})


@login_required(login_url="register")
def applyVacansy(request, pk):
    vacansy = Vacansy.objects.get(id=pk)
    form = ApplyForm(instance=vacansy)
    if request.method == "POST":
        form = ApplyForm(request.POST, instance=vacansy)
        if form.is_valid():
            form.save()
            vacansy.participants.add(request.user)
            return redirect("vacancyDetail", pk)
    return render(request, "base/apply_form.html", {"form": form})
