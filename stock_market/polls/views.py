from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import datetime as datetime
from django.contrib.auth.models import User
from .models import Operacao,Investor
from django.contrib.auth.decorators import login_required
import json


@login_required
def Home(request):
    more_bouthed = ''
    less_bouthed = ''
    total_bouthed = 0.0
    names_c  = []
    prices_c = []
    names_v  = []    
    prices_v = []
    amount_c = []
    amount_v = []
    queryset = Operacao.objects.all()
    for obj in queryset:
        if(obj.type_operation == "C"):
            names_c.append(obj.shareName)
            prices_c.append(float(obj.unit_price))
            amount_c.append(obj.amount)
    for obj in queryset:
        if(obj.type_operation == "V"):
            names_v.append(obj.shareName)
            prices_v.append(float(obj.unit_price))            
            amount_v.append(obj.amount)
    names =  [obj.shareName for obj in queryset]
    prices = [float(obj.unit_price) for obj in queryset]        
    
    for operation in queryset:
        if(operation.amount == max(amount_c)):
            more_bouthed = operation.shareName  
        if(operation.amount == max(amount_v)):
            less_bouthed = operation.shareName            
        total_bouthed += float(operation.totalOperationValue)

    contexto = {
        'prices':  json.dumps(prices),
        'shareNames': json.dumps(names),
        'shareName_C': json.dumps(names_c),
        'unit_price_C': json.dumps(prices_c),
        'shareName_V': json.dumps(names_v),
        'unit_price_V': json.dumps(prices_v),
        'more_bouthed':more_bouthed,
        'less_bouthed':less_bouthed,
        'total_bouthed': ('%.2f' % total_bouthed)
    }        
    return render(request, 'views/minha_carteira.html' ,context=contexto)

@login_required
def GotoInsertOperation(request):
    return render(request, 'views/operation_form_screen.html')

@login_required
def GotoListOperation(request):
    usuario = request.user
    investor = Investor.objects.get(user=usuario)    
    operations = investor.operacao_set.all()
    contexto = {'operations': operations}    
    return render(request, 'views/operationList_screen.html', context=contexto)

@login_required
def SearchOperations(request):
    type_op = request.POST['type_operation']
    search_camp = request.POST['search_camp'] 
    print("|"+search_camp+"|")      
    usuario = request.user
    investor = Investor.objects.get(user=usuario)    
    if search_camp and type_op:
        operations = investor.operacao_set.all().filter(type_operation=type_op,shareName=search_camp)
        
    if  type_op:      
        operations = investor.operacao_set.all().filter(type_operation=type_op)
        
    if  search_camp:      
        operations = investor.operacao_set.all().filter(shareName=search_camp)
              
    contexto = {'operations': operations}    
    return render(request, 'views/operationList_screen.html', context=contexto)


@login_required
def InsertOperations(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            shareName = request.POST['shareName']
            amount = int(request.POST['amount'])
            unit_price = float(request.POST['unit_price'])
            trading_value = float(request.POST['trading_value'])
            purchase_value = unit_price * amount
            tax = (purchase_value * 0.003125) + (purchase_value * 0.0275) + trading_value            
            if (request.POST['type_operation'] == "C"):
                totalOperationValue = purchase_value + tax
            else:
                totalOperationValue = purchase_value - tax                                            
            type_operation = request.POST['type_operation']                                                     
            investor = Investor.objects.get(user=request.user)
            date = datetime.datetime.now()            
            operacao = Operacao(
                amount=amount, 
                unit_price=unit_price, 
                trading_value=trading_value, 
                purchase_value=purchase_value, 
                tax=tax,
                totalOperationValue=totalOperationValue,
                shareName=shareName, 
                type_operation=type_operation,
                date = date.strftime("%Y/%m/%d"),
                user=investor)

            operacao.save()
    return redirect('home')

@login_required
def checkOperations(request):
    users_list = []
    for o in Operacao.objects.raw('SELECT * FROM polls_operacao where id= ${request.user_id}'):
        operations = Operacao(o.type, o.qtd, o.price, o.date)
        users_list.append(user)
    contexto = {'operations': users_list}
    return render(request, 'operation_list.html', context=contexto)
