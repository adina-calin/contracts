from django.forms import ModelForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.core import validators
from django.core.exceptions import ValidationError
from .models import ActAditional, Contract, ContractScan, CategorieContract, Produse, Clienti


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
            'data_incepere_contract': '*Format data: ll/zz/aaaa.',
            'data_sfarsit_contract': '*Format data: ll/zz/aaaa.',
            'data_contract': '*Format data: ll/zz/aaaa.',
            'produse': '*Selectați produsele aferente contractului',
            'servicii': '*Selectați produsele aferente contractului',
            'aplicatii': '*Selectați produsele aferente contractului',
            'observatii': '*Introduceti detalii suplimentare despre contract'
        }

        widgets = {
            'nr_registru ': forms.NumberInput(),
            'tip_contract': forms.Select(attrs={'class': 'form-control'}),
            'nr_contract': forms.NumberInput(),
            'data_contract': DatePickerInput(),
            'beneficiar': forms.Select(attrs={'class': 'form-control'}),
            'data_incepere_contract': DatePickerInput(),
            'data_sfarsit_contract': DatePickerInput(),
            'produse': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'servicii': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'aplicatii': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'observatii': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def clean_data_sfarsit_contract(self):
        data_incepere_contract = self.cleaned_data.get('data_incepere_contract')
        data_sfarsit_contract = self.cleaned_data.get('data_sfarsit_contract')

        if data_incepere_contract and data_sfarsit_contract:
            if data_incepere_contract > data_sfarsit_contract:
                raise forms.ValidationError("Data este anterioara datei de inceput!")
            return data_sfarsit_contract


class ClientiForm(forms.ModelForm):

    class Meta():
        model = Clienti
        
        fields = ['societate', 'sediul_social', 'punct_de_lucru', 'cod_fiscal', 'platitor_tva', 'nr_registrul_comertului', 'iban', 'banca_cont', 'reprezentant', 'persoana_contact']
        
        labels = {
            'nr_registrul_comertului': 'Numarul de inreg. la Reg. Comertului',
            'persoana_contact': 'Persoane de contact',
        #     'data_contract': 'data',
        #     'data_incepere_contract': 'Contractul începe în:',
        #     'data_sfarsit_contract': 'și se încheie în:'
        }

        # help_texts = {
        #     'data_incepere_contract': '*Format data: ll/zz/aaaa.',
        #     'data_sfarsit_contract': '*Format data: ll/zz/aaaa.',
        #     'data_contract': '*Format data: ll/zz/aaaa.',
        #     'produse': '*Selectați produsele aferente contractului',
        #     'servicii': '*Selectați produsele aferente contractului',
        #     'aplicatii': '*Selectați produsele aferente contractului',
        #     'observatii': '*Introduceti detalii suplimentare despre contract'
        # }

        widgets = {
            'societate': forms.TextInput(),
            'sediul_social': forms.Select(attrs={'class': 'form-control'}),
            'punct_de_lucru': forms.Select(attrs={'class': 'form-control'}),
            'cod_fiscal': forms.TextInput(),
            'platitor_tva': forms.CheckboxInput(attrs={'class' : 'bootstrap-select'}),
            'nr_registrul_comertului': forms.TextInput(),
            'iban': forms.TextInput(),
            'banca_cont': forms.TextInput(),
            'reprezentant': forms.CheckboxSelectMultiple(attrs={'class': 'form-control', 'size': 3}),
            'persoana_contact': forms.Select(attrs={'class': 'form-control'}),
        }