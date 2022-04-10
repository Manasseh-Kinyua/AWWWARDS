from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, 'awards/index.html', context)
