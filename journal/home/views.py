from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request , 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def policies(request):
    return render(request, 'policies.html')
