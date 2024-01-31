from django.http import HttpResponse
from django.shortcuts import render

from.form import EmpForm

# Create your views here.
def index(request):
    s=EmpForm()
    if request.method== "POST":
        s=EmpForm(request.POST)
        if s.is_valid():
            s.save()
            return HttpResponse("success")

    return render(request,'index.html',{'form':s})