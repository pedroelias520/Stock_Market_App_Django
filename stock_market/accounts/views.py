from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from polls.models import Investor

def signup_screen(request):
    return render(request, 'accounts/signup.html')

def login_screen(request):
    return render(request, 'accounts/login_screen.html')

def log_user(request):
    if request.method == "POST":
        username = request.POST['inputName']
        password = request.POST['inputPassword']
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request,"Este usuário não está presente no banco de dados")
        return redirect('login')    

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        risk_person = request.POST['risk_person']
        # TODO: fazer checagens
        if(User.objects.filter(username=username).exists()):
            print("Este usuário já existe")
            return messages.info(request, 'Pera lá, esse usuário já existe.')
        if(password == password_confirm):
            user = User.objects.create_user(username=username, email=email, password=password)            
            user.save()

            Investor.objects.create(
                user =  user,
                username= username,
                email=email,
                risk_person=risk_person
            )
            
            messages.success(request, 'Funfou, você está cadastrado!')
            return render(request, 'base.html')    
        else:
            return messages.error(request, "Calma lá meu patrão! suas senhas não estão iguais.")

def logout_user(request):
    logout(request)
    return redirect('home')