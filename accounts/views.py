from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import UserCreationFormLocal



# Create your views here.
def registerPage(request):
    form = UserCreationFormLocal()

    if request.method == "POST":
        form = UserCreationFormLocal(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account created successfully for " + user + "!")
            return redirect('login')

    return render(request, "accounts/register.html", {
        "form": form
    })

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect.")

    return render(request, "accounts/login.html", {
    })

def logoutPage(request):
    logout(request)
    return redirect("login")