from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Employee , Contract
from .form import employeeForm , contractForm , balanceForm
from django.forms import modelformset_factory 
# Create your views here.

def contracts(request):
    contracts = Contract.objects.all()
    context = {
        'contracts' : contracts ,

    }
    return render(request,'contracts.html',context)

def create_contract(request):
    contract_formset = modelformset_factory(Contract,form = contractForm)
    form = contract_formset(queryset=Contract.objects.none())

    if request.method =="POST":
        form = contract_formset(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/contracts')
    else:
        form= contract_formset(queryset=Contract.objects.none())
    

    context = {
        'form' : form ,
    }
    return render(request, 'create_contract.html', context)


def employees(request):
    employees = Employee.objects.all()
    context = {
        'employees' : employees ,

    }
    return render(request,'employees.html',context)

def create_employee(request):
    if request.method =="POST":
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
    else:
        form= employeeForm()
    

    context = {
        'form' : form ,
    }
    return render(request, 'create_employee.html', context)

def update_employee(request, pk):
    update= Employee.objects.get(id=pk)
    form= employeeForm(instance=update)
    if request.method =="POST":
        form = employeeForm(request.POST,instance=update)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees')
        else:
            form= employeeForm(instance=update)

    context = {
        'form' : form ,
    }
    return render(request,'create_employee.html',context)

def add_balance(request,pk):
    add= Employee.objects.get(id=pk)
    form= balanceForm(instance=add)
    if request.method =="POST":
        form = balanceForm(request.POST,instance=add)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/balance')
        else:
            form= balanceForm(instance=add)
    context = {
        'form' : form ,
    }
    return render(request,'add_balance.html',context)

def delete_employee(request, pk):
    deletee= Employee.objects.get(id=pk)
    #form= employeeForm(instance=update)
    deletee.delete()
    return HttpResponseRedirect('/employees')
        
    #return render(request,'employees.html',context)  

def employee_balance(request):
    balance = Employee.objects.all()
    context = {
        'balance' : balance ,
    }
    return render(request,'employee_balance.html',context)


    

    