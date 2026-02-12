from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm

def register_page(request):
    form = RegisterForm()
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('file_list')
    context = {
        "form": form
    }

    return render(request, template_name="register.html", context=context)

def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('file_list')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, template_name='login.html', context=context)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login-page')