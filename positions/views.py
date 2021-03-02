from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Position 
from .form import positionForm
# Create your views here.
def positions(request):
    all_positions = Position.objects.all()
    context = {
        'all_positions' : all_positions ,

    }
    return render(request,'all_positions.html',context)


def create_position(request):
    if request.method =="POST":
        form = positionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/position')
    else:
        form= positionForm()
    

    context = {
        'form' : form ,
    }
    return render(request, 'create_position.html', context)


