from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, ('contr_clienti/base.html'))

def contract(request):
    return HttpResponse('contract')

def actaditional(request):
    return HttpResponse('actaditional')

