from django.http import HttpResponse
from django.shortcuts import render

from.models import product


# Create your views here.

def index(request):
    return HttpResponse('hello')
def ind(request):
    produ ={
        'pro':product.objects.all()
    }
    return render(request,'index.html',produ)
