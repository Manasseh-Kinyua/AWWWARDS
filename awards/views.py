from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'awards/login_register.html', context)

def index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'awards/index.html', context)
