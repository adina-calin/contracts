from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Contract, ActAditional, ContractScan, AdresaPL, AdresaSS, registru, Clienti, Reprezentant, PersoanaContact
from .forms import ActAditionalForm, ContractForm, ContractUForm, AdresaPLForm, AdresaSSForm, ContractAAUForm, ClientiForm, ReprezentantForm, PersoanaContactForm
from .filters import ContractFilter, ClientiFilter
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import StringIO, BytesIO
from django.contrib import messages
# from xhtml2pdf.utils import generate_pdf



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


def sterge_documenta(request, pk1, pk2, pk3):
    contract = Contract.objects.get(id=pk1)
    actaditional = ActAditional.objects.get(id=pk2)
    document = ContractScan.objects.get(id=pk3)
    if request.method == 'POST':
        document = ContractScan.objects.get(id=pk3)
        document.delete()
        return redirect('actaditional-detail', contract.id, actaditional.id)

    context = {'contract': contract, 'document': document, 'actaditional': actaditional}

    return render(request, 'contr_clienti/document_confirm_delete_aa.html', context)


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
            # form.save()
            new_contract = form.save()
            contract = Contract.objects.get(id=new_contract.id)
            messages.success(request, f'Contractul s-a creat cu succes!')
            return redirect('contract-detail', contract.id)

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


def client_detalii(request, pk4):
    client = Clienti.objects.get(id=pk4)
    reprezentanti = client.reprezentant_set.all()
    form = ReprezentantForm(initial={'client': client})
    persoanecontact = client.persoanacontact_set.all()
    formpc = PersoanaContactForm(initial={'client': client})
    punctelucru = client.adresapl_set.all()
    formpl = AdresaPLForm(initial={'client': client})
    adresass = client.adresass_set.last()
    formss = AdresaSSForm(initial={'client': client})

    context = {
        'client': client, 
        'reprezentanti':reprezentanti, 
        'form':form, 
        'persoanecontact': persoanecontact, 
        'formpc': formpc,
        'punctelucru': punctelucru, 
        'formpl': formpl,
        'adresass': adresass, 
        'formss': formss,
        }

    return render(request, 'contr_clienti/client_detail.html', context)


def update_client_detalii(request, pk4):
    client = Clienti.objects.get(id=pk4)
    reprezentanti = client.reprezentant_set.all()
    form = ReprezentantForm(initial={'client': client})
    persoanecontact = client.persoanacontact_set.all()
    formpc = PersoanaContactForm(initial={'client': client})
    punctelucru = client.adresapl_set.all()
    formpl = AdresaPLForm(initial={'client': client})
    adresassoc = client.adresass_set.last()
    formss = AdresaSSForm(initial={'client': client})

    context = {
        'client': client, 
        'reprezentanti':reprezentanti, 
        'form':form, 
        'persoanecontact': persoanecontact, 
        'formpc': formpc,
        'punctelucru': punctelucru, 
        'formpl': formpl,
        'adresass': adresassoc, 
        'formss': formss,
        }

    return render(request, 'contr_clienti/client_detail_update.html', context)


def creeaza_client(request):
    form = ClientiForm
    if request.method == 'POST':
        form = ClientiForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            client = Clienti.objects.get(id=new_client.id)
            return redirect('client-detail', client.id)

    context = {'form': form}

    return render(request, 'contr_clienti/client_form.html', context)


def creeaza_reprezentant(request, pk4):
    client = Clienti.objects.get(id=pk4)
    form = ReprezentantForm(initial={'client': client})

    context = {
        'client': client, 
        'form': form,
    }

    if request.method == 'POST':
        form = ReprezentantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', client.id)

    return render(request, 'contr_clienti/reprezentant_form.html', context)


def creeaza_persoanacontact(request, pk4):
    client = Clienti.objects.get(id=pk4)
    formpc = PersoanaContactForm(initial={'client': client})

    context = {
        'client': client, 
        'form': formpc,
    }

    if request.method == 'POST':
        form = PersoanaContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', client.id)

    return render(request, 'contr_clienti/persoanacontact_form.html', context)


def creeaza_adresapl(request, pk4):
    client = Clienti.objects.get(id=pk4)
    formpl = AdresaPLForm(initial={'client': client})

    context = {
        'client': client, 
        'form': formpl,
    }

    if request.method == 'POST':
        form = AdresaPLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', client.id)

    return render(request, 'contr_clienti/adresapl_form.html', context)


def creeaza_adresass(request, pk4):
    client = Clienti.objects.get(id=pk4)
    formss = AdresaSSForm(initial={'client': client})

    context = {
        'client': client, 
        'form': formss,
    }

    if request.method == 'POST':
        form = AdresaSSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client-detail', client.id)

    return render(request, 'contr_clienti/adresass_form.html', context)


def update_client_date(request, pk4):
    client = Clienti.objects.get(id=pk4)
    form = ClientiForm(instance=client)
    
    context = {
        'client': client, 
        'form': form,
    }

    if request.method == 'POST':
        form = ClientiForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client-detail-update', client.id)

    return render(request, 'contr_clienti/client_form_up.html', context)


def update_reprezentant(request, pk4, pk5):
    client = Clienti.objects.get(id=pk4)
    reprezentant = Reprezentant.objects.get(id=pk5)
    form = ReprezentantForm(instance=reprezentant)
    
    context = {
        'client': client, 
        'reprezentant': reprezentant,
        'form': form,
    }

    if request.method == 'POST':
        form = ReprezentantForm(request.POST, instance=reprezentant)
        if form.is_valid():
            form.save()
            return redirect('client-detail-update', client.id)

    return render(request, 'contr_clienti/reprezentant_form_up.html', context)


def update_persoanacontact(request, pk4, pk6):
    client = Clienti.objects.get(id=pk4)
    persoanacontact = PersoanaContact.objects.get(id=pk6)
    form = PersoanaContactForm(instance=persoanacontact)
    
    context = {
        'client': client, 
        'persoanacontact': persoanacontact,
        'form': form,
    }

    if request.method == 'POST':
        form = PersoanaContactForm(request.POST, instance=persoanacontact)
        if form.is_valid():
            form.save()
            return redirect('client-detail-update', client.id)

    return render(request, 'contr_clienti/persoanacontact_form_up.html', context)


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


def update_adresapl(request, pk4, pk7):
    client = Clienti.objects.get(id=pk4)
    adresapl = AdresaPL.objects.get(id=pk7)
    form = AdresaPLForm(instance=adresapl)
    
    context = {
        'client': client, 
        'adresapl': adresapl,
        'form': form,
    }

    if request.method == 'POST':
        form = AdresaPLForm(request.POST, instance=adresapl)
        if form.is_valid():
            form.save()
            return redirect('client-detail-update', client.id)

    return render(request, 'contr_clienti/adresapl_form_up.html', context)


def update_adresass(request, pk4, pk8):
    client = Clienti.objects.get(id=pk4)
    adresass = AdresaSS.objects.get(id=pk8)
    form = AdresaSSForm(instance=adresass)
    
    context = {
        'client': client, 
        'adresass': adresass,
        'form': form,
    }

    if request.method == 'POST':
        form = AdresaSSForm(request.POST, instance=adresass)
        if form.is_valid():
            form.save()
            return redirect('client-detail-update', client.id)

    return render(request, 'contr_clienti/adresass_form_up.html', context)


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


def sterge_reprezentant(request, pk4, pk5):
    client = Clienti.objects.get(id=pk4)
    reprezentant = Reprezentant.objects.get(id=pk5)
    if request.method == 'POST':
        reprezentant.delete()
        return redirect('client-detail-update', client.id)

    context = context = {
        'client': client, 
        'reprezentant': reprezentant,
    }
    
    return render(request, 'contr_clienti/reprezentant_confirm_delete.html', context)


def sterge_persoanacontact(request, pk4, pk6):
    client = Clienti.objects.get(id=pk4)
    persoanacontact = PersoanaContact.objects.get(id=pk6)
    if request.method == 'POST':
        persoanacontact.delete()
        return redirect('client-detail-update', client.id)

    context = context = {
        'client': client, 
        'persoanacontact': persoanacontact,
    }
    
    return render(request, 'contr_clienti/persoanacontact_confirm_delete.html', context)


def sterge_adresapl(request, pk4, pk7):
    client = Clienti.objects.get(id=pk4)
    adresapl = AdresaPL.objects.get(id=pk7)
    if request.method == 'POST':
        adresapl.delete()
        return redirect('client-detail-update', client.id)

    context = context = {
        'client': client, 
        'adresapl': adresapl,
    }
    
    return render(request, 'contr_clienti/adresapl_confirm_delete.html', context)


def sterge_adresass(request, pk4, pk8):
    client = Clienti.objects.get(id=pk4)
    adresass = AdresaSS.objects.get(id=pk8)
    if request.method == 'POST':
        adresass.delete()
        return redirect('client-detail-update', client.id)

    context = context = {
        'client': client, 
        'adresass': adresass,
    }
    
    return render(request, 'contr_clienti/adresassS_confirm_delete.html', context)


def rapoarte(request):
    reg = registru()

    paginator = Paginator(reg, 10)
    page = request.GET.get('page')
    reg = paginator.get_page(page)

    context = context = {
        'reg': reg,
    }

    return render(request, 'contr_clienti/registru.html', context)


# def listare_registru(request):
#     reg = registru()

#     context = context = {
#         'reg': reg,
#     }

#     template=get_template('registru_print.html')
#     context_p=template.render(context)
#     response=BytesIO()

#     pdfPage=pisa.pisaDocument(BytesIO(context_p.encode('UTF-8')), response)
#     if not pdfPage.err:
#         return HttpResponse(response.getvalue(), content_type='application/pdf')
#     else:
#         return HttpResponse('Eroare la generarea pdf-ului.')

def listare_registru(response):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('registru_print.html', file_object=resp)
    return result   


def lista_clienti(request):
    clienti = Clienti.objects.order_by('societate') 

    myFilter = ClientiFilter(request.GET, queryset=clienti)
    clienti = myFilter.qs

    paginator = Paginator(clienti, 10)
    page = request.GET.get('page')
    clienti = paginator.get_page(page)

    context = context = {
        'clienti': clienti,
        'myFilter': myFilter,
    }

    return render(request, 'contr_clienti/clienti.html', context)