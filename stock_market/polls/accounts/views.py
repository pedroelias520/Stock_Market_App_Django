from django.shortcuts import render

def signup(request):
    return render(request, 'accounts/signup.html')

def register(request):
    return render(request, 'accounts/register.html')    