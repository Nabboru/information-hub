from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def help(request):
    return render(request, 'help_and_support.html', {'title': 'Help and Support'})
