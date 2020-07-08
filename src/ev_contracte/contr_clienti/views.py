from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def home(request):
    contracte = Contract.objects.all()
    total_contracte = contracte.count()
    paginator = Paginator(contracte, 5)
    page = request.GET.get('page')
    contracte = paginator.get_page(page)
    context = {'contracte': contracte, 'total_contracte': total_contracte}
    return render(request, 'contr_clienti/home.html', context)

def contract_detalii(request, pk1):
    contract = Contract.objects.get(id=pk1)
    acteaditionale = contract.actaditional_set.all()
    aplicatii = contract.aplicatii.all()
    produse = contract.produse.all()
    servicii = contract.servicii.all()

    context = {
        'contract': contract, 
        'acteaditionale':acteaditionale, 
        'aplicatii':aplicatii, 
        'produse': produse, 
        'servicii':servicii,
        }
    return render(request, ('contr_clienti/contract_detail.html'), context)

def actaditional_detalii(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)

    context = {
        'contract': contract, 
        'actaditional':actaditional, 
    }
    return render(request, ('contr_clienti/actaditional_detail.html'), context)

