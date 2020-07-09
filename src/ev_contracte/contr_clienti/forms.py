from django.forms import ModelForm
from django import forms
from .models import ActAditional, Contract




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


class ContractForm(forms.ModelForm):
    class Meta():
        model = Contract
        fields = '__all__'

        widgets = {
            'nr_registru': forms.TextInput(attrs={'class': 'form-control'}),
            'tip_contract': forms.Select(attrs={'class': 'form-control'}),
            'nr_contract': forms.TextInput(attrs={'class': 'form-control'}),
            'data_contract': forms.TextInput(attrs={'class': 'form-control'}),
            'beneficiar': forms.Select(attrs={'class': 'form-control'}),
            'data_incepere_contract': forms.TextInput(attrs={'class': 'form-control'}),
            'data_sfarsit_contract': forms.TextInput(attrs={'class': 'form-control'}),
            'produse': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'servicii': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'aplicatii': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'observatii': forms.Textarea(attrs={'class': 'form-control', 'rows': "3"}),
        }

