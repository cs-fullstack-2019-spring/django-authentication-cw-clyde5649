from django.shortcuts import render
from django.http import HttpResponse
from .forms import fitnessform,fitnessmodel
from django.contrib.auth.models import User



# Create your views here.




def index(request):
    return HttpResponse('we are working on a server for you')



def newuser(request):
    form = fitnessmodel(request.POST or None)
    context = {
        "form": form
    }

    if request.method == "POST":
        print(request.method)

        #return render(request,'fitnessapp/newuser.html')

    return render(request, 'fitnessapp/newuser.html', context)




def hellonewuser(request):
    return render(request, "fitnessapp/hellonewuser.html")