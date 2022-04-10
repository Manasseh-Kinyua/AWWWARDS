from django.shortcuts import render
from .models import Project

# Create your views here.
def loginPage(request):
    context = {}
    return render(request, 'awards/login_register.html', context)

def index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'awards/index.html', context)
