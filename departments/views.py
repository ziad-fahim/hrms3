from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Department 
from .form import departmentForm
# Create your views here.
def departments(request):
    all_departments = Department.objects.all()
    context = {
        'all_departments' : all_departments ,

    }
    return render(request,'all_departments.html',context)


def create_department(request):
    if request.method =="POST":
        form = departmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/department')
    else:
        form= departmentForm()
    

    context = {
        'form' : form ,
    }
    return render(request, 'create_department.html', context)