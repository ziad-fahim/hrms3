from django.shortcuts import render , HttpResponseRedirect
from .models import Taxes


# Create your views here.
"""
def compare(request):
    month_salary = request.POST.get('net_salary')
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
    print(final_tax,gross_salary)
    return render(request,"taxes/calculate.html",context)