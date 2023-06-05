from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']


        if not username or not password or not password1:
            messages.error(request, "Your registration is not completed")
            return redirect('register')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    return render(request, "register.html")


def newpage(request):
    return render(request, 'new_page.html')


def logout_view(request):
    logout(request)
    return redirect('login')