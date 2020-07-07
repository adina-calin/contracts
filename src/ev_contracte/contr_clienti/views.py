from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, ('contr_clienti/home.html'))

def contract_detalii(request):
    return render(request, ('contr_clienti/contract_detail.html'))

def actaditional_detalii(request):
    return render(request, ('contr_clienti/actaditional_detail.html'))

