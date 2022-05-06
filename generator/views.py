from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    return render(request, 'password.html')