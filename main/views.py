from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"base.html")

def about(request):
    return render(request,"main/about.html")

def contact(request):
    return render(request,"main/contact.html")

def projects(request):
    return render(request,"main/projects.html")
