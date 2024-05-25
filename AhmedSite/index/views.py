from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index/home.html")

def resume(request):
    return render(request,"index/resume.html")

def aboutme(request):
    return render(request,"index/about.html")