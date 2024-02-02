from django.http import HttpResponse
from django.shortcuts import render

from .form import form2
from .models import employee


# Create your views here.

def imag2(request):
    b = form2()
    if request.method =="POST":
        b =form2(request.POST,request.FILES)
        if b.is_valid():
            b.save()
            return HttpResponse("success")

    return render(request,"form1.html",{'form':b})
def display(request):
    a=employee.objects.all()
    return render(request,"img2.html",{'a':a})

