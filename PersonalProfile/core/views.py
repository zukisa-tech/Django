from django.shortcuts import render

def index(request):

    return render(request, 'core/index.html')

def education(request):
    return render(request, 'core/education.html')

def experience(request):
    return render(request, 'core/experience.html')

def projects(request):
    return render(request, 'core/projects.html')