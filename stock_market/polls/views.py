from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def Home(request):
    return render(request, 'base.html')


def GotoInsertOperation(request):
    return render(request, 'operation_form_screen.html')


def GotoListOperation(request):
    return render(request, 'operation_form_screen.html')


def InsertOperations(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            qtd = request.POST['qtd']
            price = request.POST['price']
            type_operation = request.POST['type']
            tax = request.POST['taxa']
            date = request.POST['date']
            usuario = request.user
            user = User.objects.get(user=usuario)
            operacao = Operacao(
                price=price, qtd=qtd, type_operation=type_operation, tax=tax, date=date, user=user)
            operacao.save()
    return redirect('home')


def checkOperations(request):
    users_list = []
    for o in Operacao.objects.raw('SELECT * FROM polls_operacao where id= ${request.user_id}'):
        operations = Operacao(o.type, o.qtd, o.price, o.date)
        users_list.append(user)
    contexto = {'operations': users_list}
    return render(request, 'operation_list.html', context=contexto)
