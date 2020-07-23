from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from .forms import ActAditionalForm, ContractForm, ContractUForm, ContractAAUForm
from .filters import ContractFilter


def home(request):
    contracte = Contract.objects.all().order_by('nr_registru')

    myFilter = ContractFilter(request.GET, queryset=contracte)
    contracte = myFilter.qs

    paginator = Paginator(contracte, 6)
    page = request.GET.get('page')
    contracte = paginator.get_page(page)
         
    context = {
        'contracte': contracte, 
        'myFilter': myFilter,
    }

    return render(request, 'contr_clienti/home.html', context)


def contracte_context_processor(request):
    contracte_ex = Contract.objects.all()
    ultimul_contract = Contract.objects.latest('nr_registru')
    ultimul_actaditional = ActAditional.objects.latest('nr_registru')

    return {
        'contracte_ex': contracte_ex,
        'ultimul_contract': ultimul_contract,
        'ultimul_actaditional': ultimul_actaditional,
        }


def contract_detalii(request, pk1):
    contract = Contract.objects.get(id=pk1)
    acteaditionale = contract.actaditional_set.all()
    aplicatii = contract.aplicatii.all()
    produse = contract.produse.all()
    servicii = contract.servicii.all()
    documente = contract.contractscan_set.all()

    context = {
        'contract': contract, 
        'acteaditionale':acteaditionale, 
        'aplicatii':aplicatii, 
        'produse': produse, 
        'servicii':servicii,
        'documente': documente,
        }

    return render(request, 'contr_clienti/contract_detail.html', context)


def contract_scan(request, pk1):
    contract = Contract.objects.get(id=pk1)
    form = ContractUForm(initial={'contract': contract})
    context = {
        'contract': contract, 
        'form': form,
    }
    if request.method == 'POST':
        form = ContractUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contract-detail', contract.id)
    else:
        form = ContractUForm()
    return render(request, 'contr_clienti/contract_scan.html', context)


def sterge_documentc(request, pk1, pk3):
    contract = Contract.objects.get(id=pk1)
    document = ContractScan.objects.get(id=pk3)
    if request.method == 'POST':
        document = ContractScan.objects.get(id=pk3)
        document.delete()
        return redirect('contract-detail', contract.id)

    context = {'contract': contract, 'document': document}

    return render(request, 'contr_clienti/document_confirm_delete.html', context)


def actaditional_scan(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)
    form = ContractAAUForm(initial={'actaditional': actaditional, 'contract': contract})
    context = {
        'contract': contract, 
        'actaditional': actaditional,
        'form': form,
    }
    if request.method == 'POST':
        form = ContractAAUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('actaditional-detail', contract.id, actaditional.id)
    else:
        form = ContractAAUForm()
    return render(request, 'contr_clienti/actaditional_scan.html', context)


def actaditional_detalii(request, pk1, pk2):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)
    documente = actaditional.contractscan_set.all()

    context = {
        'contract': contract, 
        'actaditional':actaditional,
        'documente': documente 
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
        'form': form,
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
        'contract': contract,
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
        'form': form,
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
        'actaditional': actaditional,
    }
    
    return render(request, 'contr_clienti/actaditional_confirm_delete.html', context)



