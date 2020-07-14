from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import ActAditionalForm, ContractForm


def home(request):
    contracte = Contract.objects.all()
    total_contracte = contracte.count()
    paginator = Paginator(contracte, 5)
    page = request.GET.get('page')
    contracte = paginator.get_page(page)

    context = {
        'contracte': contracte, 
        'total_contracte': total_contracte
    }

    return render(request, 'contr_clienti/home.html', context)


def contract_detalii(request, pk1):
    contract = Contract.objects.get(id=pk1)
    acteaditionale = contract.actaditional_set.all()
    aplicatii = contract.aplicatii.all()
    produse = contract.produse.all()
    servicii = contract.servicii.all()
    # pdfc = contract.pdfc

    context = {
        'contract': contract, 
        'acteaditionale':acteaditionale, 
        'aplicatii':aplicatii, 
        'produse': produse, 
        'servicii':servicii,
        # 'pdfc': pdfc
        }

    return render(request, 'contr_clienti/contract_detail.html', context)


def contract_pdf(request, pk1):
    contract = Contract.objects.get(id=pk1)
    # pdf = Contract.objects.get(id=pk1)
    # pdfc = pdf.contract_set.all()
    if request.method == 'POST':
        form = ContractUForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = ContractUForm(instance=contract)

    context = {
        'contract': contract, 
        'form':form, 
        # 'pdfc':pdfc
    }

    return render(request, 'contr_clienti/contract_pdf.html', context)


def actaditional_detalii(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)

    context = {
        'contract': contract, 
        'actaditional':actaditional, 
    }

    return render(request, 'contr_clienti/actaditional_detail.html', context)


def creeaza_contract(request):
    form = ContractForm
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('acasa')

    context = {'form': form}

    return render(request, 'contr_clienti/contract_form.html', context)


def creeaza_actaditional(request, pk1):
    contract = Contract.objects.get(id=pk1)
    form = ActAditionalForm(initial={'contract': contract})
    
    context = {
        'contract': contract, 
        'form': form
    }

    if request.method == 'POST':
        form = ActAditionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)

    return render(request, 'contr_clienti/actaditional_form.html', context)


def update_contract(request, pk1):
    contract = Contract.objects.get(id=pk1)
    form = ContractForm(instance=contract)

    context = {
        'form': form, 
        'contract': contract
    }

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    
    return render(request, 'contr_clienti/contract_form_up.html', context)


def update_actaditional(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)
    form = ActAditionalForm(instance=actaditional)
    
    context = {
        'contract': contract, 
        'actaditional': actaditional,
        'form': form
    }

    if request.method == 'POST':
        form = ActAditionalForm(request.POST, instance=actaditional)
        if form.is_valid():
            form.save()
            return redirect('actaditional-detail', contract.id, actaditional.id)

    return render(request, 'contr_clienti/actaditional_form_up.html', context)


def sterge_contract(request, pk1):
    contract = Contract.objects.get(id=pk1)
    if request.method == 'POST':
        contract.delete()
        return redirect('acasa')

    context = {'object': contract}

    return render(request, 'contr_clienti/contract_confirm_delete.html', context)


def sterge_actaditional(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)
    if request.method == 'POST':
        actaditional.delete()
        return redirect('contract-detail', contract.id)

    context = context = {
        'contract': contract, 
        'actaditional': actaditional
    }
    
    return render(request, 'contr_clienti/actaditional_confirm_delete.html', context)