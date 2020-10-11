from django.shortcuts import render, redirect
from .forms import SignUpForm, LogInForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'begin/home.html')


def detail(request):
    return render(request, 'begin/detail.html')


def advice(request):
    return render(request, 'begin/advice.html')


def login(response):
    if response.method == "POST":
        form = LogInForm(response.POST)

        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = LogInForm()

    return render(response, "begin/login.html", {"form": form})


def logout(request):
    return render(request, 'begin/logout.html')


def sign_up(response):
    if response.method == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = SignUpForm()

    return render(response, "begin/sign_up.html", {"form": form})
