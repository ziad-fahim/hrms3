from django.shortcuts import render
from django import forms
from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Leave_Master , All_Leaves , Taxes
from employees.models import Employee , Contract 

from .form import LeavesForm , AllLeavesForm , Login , LeavesForm
from django.core.mail import send_mail , EmailMessage
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.




def Leaves(request):
    leaves = Leave_Master.objects.all()
    context = {
        'leaves' : leaves ,

    }
    return render(request,'leave_master.html',context)

def add_leave(request):
    if request.method =="POST":
        form = LeavesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves_master')
    else:
        form= LeavesForm()
    

    context = {
        'form' : form ,
    }
    return render(request, 'add_leave.html', context)


def display_leave_details(request, pk):
    display= All_Leaves.objects.get(id=pk)
    context = {
        'display' : display ,

    }
    return render(request,'display.html',context)
    
def compare(request):
    if(request.method == 'POST'):
        month_salary =request.POST.get('net_salary')
        print(month_salary)
        net_salary = float(month_salary)*12
        values = Taxes.objects.all()
        insurance = 0.11
        taxes=0
        difference=0
        percent=0
        for x in values :
            if float(net_salary)>x.start_range and float(net_salary)<=x.end_range:
                percent = x.percent
                break
            else:
                taxes+=x.tax
                difference+=x.difference
    
        dummy = float(net_salary)+taxes-difference
        dummy2= dummy/(1-percent)
        dummy3= dummy2*percent
        final_tax=round(taxes + dummy3,3)
        monthly_tax = final_tax/12
        gross_salary = round(final_tax +float(net_salary),3)
        monthly_gross = gross_salary/12
        social_insurance=monthly_gross*insurance
        basic_salary = monthly_gross-social_insurance
        context ={
            'gross':round(gross_salary,3) , 'tax':round(final_tax,3) ,
            'month_gross':round(monthly_gross,3) , 'monthly_tax':round(monthly_tax,3) ,
            'insurance':round(social_insurance,3) , 'salary':round(basic_salary,3) ,
        
        }
        return render(request,"calculate.html",context)
    else:
        return render(request,"calculate.html")
    #print(final_tax,gross_salary)
    

@login_required(login_url='')
def emp_leaves(request):
    emp = Employee.objects.get(user=request.user.id)
    print(emp)
    employee_leaves= All_Leaves.objects.filter(employee=emp.id)
    print(emp_leaves)
    context = {
        'all_leaves' : employee_leaves ,
    }
    return render(request, 'all_leaves.html', context)

def create_leave(request):
    if request.method =="POST":
        form = AllLeavesForm(request.POST)
        if form.is_valid():  
            #print(form.cleaned_data)
            balance=int(form.cleaned_data['employee'].leaves_balance)
            value= form.cleaned_data['leave_type'].leave_value
            start =form.cleaned_data['leave_start'].day
            end = form.cleaned_data['leave_end'].day
            days = (int(end) - int(start)) + 1
            result = (days* int(value))
            employee_id= form.cleaned_data['employee'].id
            all_leaves = All_Leaves.objects.filter(employee=employee_id , leave_end__gt = form.cleaned_data['leave_start'])
            if all_leaves.count()==0 :
                if result < balance :
                    form.save()
                    return HttpResponseRedirect('/leaves_master/employee_leaves')
                else:
                    messages.info(request, 'You dont have enough balance ' + str(balance) ) 
            else:
                messages.info(request, '    You already have a leave in this date' ) 
            #send_mail('Email subject' , 'This is message' , settings.EMAIL_HOST_USER , ['ziadmohamed44214@gmail.com'], fail_silently = False)
            
    else:
        form= AllLeavesForm()
    
    context = {
        'form' : form ,
    }
    return render(request, 'create_leave.html', context)    


def All_Leavess(request):
    all_leaves = All_Leaves.objects.all()
    context = {
        'all_leaves' : all_leaves ,

    }
    return render(request,'all_leaves.html',context)


def Display_Dashboard(request):

    all_leaves = All_Leaves.objects.all()
    user=Employee.objects.get(user=request.user)
    emp= Contract.objects.filter(manager=user)
    context = {
        'emp' : emp ,
        'all_leaves' : all_leaves ,

    }
    return render(request,'Dashboard.html',context)

def Accept(request,pk):
    obj = All_Leaves.objects.get(id=pk)
    obj.Status="Accept"
    obj.save()
    balance = obj.employee.leaves_balance
    value= obj.leave_type.leave_value
    start = obj.leave_start.day
    end = obj.leave_end.day
    days = (int(end) - int(start)) + 1
    result = int(balance) - (days* int(value))
    employee = Employee.objects.get(id=obj.employee.id)
    employee.leaves_balance = result
    employee.save()
    return HttpResponseRedirect('/leaves_master/dashboard')


def Reject(request,pk):
    obj = All_Leaves.objects.get(id=pk)
    obj.Status="Reject"
    obj.save()
    return HttpResponseRedirect('/leaves_master/dashboard')









