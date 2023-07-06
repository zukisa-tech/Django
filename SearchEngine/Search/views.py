from django.shortcuts import render, redirect
from .chatgpt import search
from .forms import SignupForm

# Create your views here.

def index(request):

    return render(request, 'Search/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/login/')

    else:

        form = SignupForm()

    return render(request, 'Search/signup.html',{'form':form})

def welcome(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        results = search(query)
        return render(request, 'Search/welcome.html', {'results': results, 'query': query})
    
    return render(request, 'Search/welcome.html')