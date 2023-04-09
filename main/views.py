from django.shortcuts import render
from api.models import Project

# Create your views here.
def index(request):
    return render(request,"base.html")

def about(request):
    return render(request,"main/about.html")

def contact(request):
    return render(request,"main/contact.html")

def projects(request):
    nomlar = Project.objects.all()
    return render(request,"main/projects.html", {'nomlar': nomlar})
