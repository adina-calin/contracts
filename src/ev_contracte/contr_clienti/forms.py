from django.forms import ModelForm
from django import forms
from .models import ActAditional, Contract, ContractScan, CategorieContract


class ActAditionalForm(forms.ModelForm):
    class Meta():
        model = ActAditional
        fields = ('nr_registru', 'contract', 'nr_actaditional', 'data_actaditional', 'data_incepere_actaditional', 'data_sfarsit_actaditional', 'produse', 'servicii', 'aplicatii', 'observatii')

        # widgets = {
        #     'nr_registru': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contract': forms.Select(attrs={'class': 'form-control'}),
        #     'nr_actaditional': forms.TextInput(attrs={'class': 'form-control'}),
        #     'data_actaditional': forms.TextInput(attrs={'class': 'form-control'}),
        #     'data_incepere_actaditional': forms.TextInput(attrs={'class': 'form-control'}),
        #     'data_sfarsit_actaditional': forms.TextInput(attrs={'class': 'form-control'}),
        #     'produse': forms.Select(attrs={'class': 'form-control'}),
        #     'servicii': forms.Select(attrs={'class': 'form-control'}),
        #     'aplicatii': forms.Select(attrs={'class': 'form-control'}),
        #     'observatii': forms.Textarea(attrs={'class': 'form-control'}),
        # }


# class ContractForm(forms.ModelForm):
#     class Meta():
#         model = Contract
#         fields = ('nr_registru', 'tip_contract', 'nr_contract', 'data_contract', 'beneficiar', 'data_incepere_contract', 'data_sfarsit_contract', 'produse', 'servicii', 'aplicatii', 'observatii')

#         widgets = {
#             'nr_registru': forms.TextInput(attrs={'class': 'form-control'}),
#             'tip_contract': forms.Select(attrs={'class': 'form-control'}),
#             'nr_contract': forms.TextInput(attrs={'class': 'form-control'}),
#             'data_contract': forms.TextInput(attrs={'class': 'form-control'}),
#             'beneficiar': forms.Select(attrs={'class': 'form-control'}),
#             'data_incepere_contract': forms.TextInput(attrs={'class': 'form-control'}),
#             'data_sfarsit_contract': forms.TextInput(attrs={'class': 'form-control'}),
#             'produse': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'servicii': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'aplicatii': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'observatii': forms.Textarea(attrs={'class': 'form-control', 'rows': "3"}),
#         }


class ContractUForm(forms.ModelForm):
    class Meta():
        model = ContractScan
        fields = ('documente', 'contract')

class ContractAAUForm(forms.ModelForm):
    class Meta():
        model = ContractScan
        fields = ('documente', 'actaditional', 'contract')


class ContractForm(forms.ModelForm):

    class Meta():
        model = Contract 

        fields = ['nr_registru', 'tip_contract', 'nr_contract', 'data_contract', 'beneficiar', 'data_incepere_contract', 'data_sfarsit_contract', 'produse', 'servicii', 'aplicatii', 'observatii']
   
        labels = {
            'nr_registru': 'Numar registru',
            'nr_contract': 'număr',
            'data_contract': 'data',
            'data_incepere_contract': 'Contractul începe în:',
            'data_sfarsit_contract': 'și se încheie în:'
        }

        help_texts = {
            'data_incepere_contract': '*Format data: aaaa-ll-zz.',
            'data_sfarsit_contract': '*Format data: aaaa-ll-zz.',
            'data_contract': '*Format data: aaaa-ll-zz.',
            'produse': '*Pentru a selecta mai multe produse apăsați CTRL',
            'servicii': '*Pentru a selecta mai multe servicii apăsați CTRL',
            'aplicatii': '*Pentru a selecta mai multe aplicații apăsați CTRL',
            'observatii': '*Introduceti detalii suplimentare despre contract'
        }

        widgets = {
            'nr_registru ': forms.NumberInput(),
            'tip_contract': forms.Select(attrs={'class': 'form-control'}),
            'nr_contract': forms.NumberInput(),
            'data_contract': forms.DateInput(format='d.m.Y'),
            # 'data_contract': forms.SelectDateWidget(attrs=({'style': 'width: 33%; display: inline-block;'})),
            'beneficiar': forms.Select(attrs={'class': 'form-control'}),
            'data_incepere_contract': forms.DateInput(format='d.m.Y'),
            'data_sfarsit_contract': forms.DateInput(format='d.m.Y'),
            'produse': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'servicii': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'aplicatii': forms.SelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'observatii': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }