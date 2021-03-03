from django.contrib.auth import authenticate, login
from django.shortcuts import render



def Home(request):
    return render(request, base)
def InsertOperations(request):    
    qtd = request.POST['password']              
    price = request.POST['email']    
    tipo = request.POST.get('type', "Comum");  
    taxa = request.POST['taxa']    
    date = request.POST['date'] 
    id_user =  request.user_id  

    operacao = Operacao(price = price, qtd = qtd, tipo = tipo, taxa = taxa, date = date)    
    operacao.save()
    return render(request,'minha_carteira.html')

def InsertUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password_verification = request.POST['password_verification']

    if password == password_verification:
        if User. 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(username=username, password=password)
        if user in not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

def ListOperations(request):
    users_list = []
    for o in Operacao.objects.raw('SELECT * FROM polls_operacao where id= ${request.user_id}'):        
        operations = Operacao(o.type,o.qtd,o.price,o.date)               
        users_list.append(user)        
    contexto = {'operations': users_list}            
    return render(request,'operation_list.html', context=contexto) 