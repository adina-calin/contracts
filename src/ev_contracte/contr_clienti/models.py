from django.db import models
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from datetime import datetime, timedelta, date
from itertools import chain
from operator import attrgetter


functii = [
        (1, 'Administrator'),
        (2, 'Director'),
        (3, 'Director General'),
        (4, 'Director Adjunct'),
        (5, 'Contabil Șef'),
        (6, 'Director Economic')
    ]

moneda = [
        (1, 'RON'),
        (2, 'EUR'),
        (3, 'USD')
    ]


class CategorieContract(models.Model):
    '''In functie de catgoria de contract se va alege modelul de contract si daca se ofera sevicii, produse sau aplicatii propri'''
    categorie_contract = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categorii de contracte'

    def __str__(self):
        return self.categorie_contract

 
class Produse(models.Model):
    '''Produsele revandute de catre Info98'''
    produs = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, blank=True)
    furnizor = models.CharField(max_length=255)
    pret_furnizor_fara_tva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    moneda_furnizor = models.IntegerField(choices=moneda)
    pret_vanzare_fara_tva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    moneda_vanzare = models.IntegerField(choices=moneda)
    observatii = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Produse'

    def __str__(self):
        return self.produs


class ServiciiInformatice(models.Model):
    '''Serviciile informatice pe care noi le putem oferi'''
    serviciu = models.CharField(max_length=255)
    contravaloare_serviciu_fara_tva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    moneda_vanzare = models.IntegerField(choices=moneda)
    observatii = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Servicii'

    def __str__(self):
        return self.serviciu


class AplicatiiInfo98(models.Model):
    '''Aplicatiile dezvoltate de catre INFO98'''
    aplicatie = models.CharField(max_length=255)
    contravaloare_aplicatie = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    contravaloare_aplicatie_fara_tva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    moneda_vanzare = models.IntegerField(choices=moneda)
    abonament_aplicatie_fara_tva = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    moneda_abonament = models.IntegerField(choices=moneda)
    observatii = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Aplicații INFO'98"

    def __str__(self):
        return self.aplicatie


class Clienti(models.Model):
    '''Toate datele clientului necesare a fi trecute pe contract'''
    societate = models.CharField(max_length=255)
    cod_fiscal = models.IntegerField()
    platitor_tva = models.BooleanField(default=None)
    nr_registrul_comertului = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255)
    banca_cont = models.CharField(max_length=255)

    def __str__(self):
        return self.societate

    class Meta:
        verbose_name_plural = 'Clienti'


class AbstractReprezentant(models.Model):
    '''Modelul pe care il mosteneste clasa de reprezentanti si clasa de persoane de contact.'''
    nume = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    telefon = models.IntegerField(null=True, blank=True)
    functie = models.CharField(max_length=255)
    client = models.ForeignKey(Clienti, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(str(self.functie), self.nume)

    class Meta:
        abstract = True


class Reprezentant(AbstractReprezentant):
    '''Datele reprezentantilor societatii pe care ii vom trece pe contract. Campuri obligatorii: nume, prenume, functie.'''
    pass

    class Meta:
        verbose_name_plural = 'Reprezentanti'


class PersoanaContact(AbstractReprezentant):
    '''Persoanele de contact pentru un anumit contract. Pot fi dintre reprezentantii sociatatii.'''

    class Meta:
        verbose_name_plural = 'Persoane de contact'


class AdresaPL(models.Model):
    nume_pl = models.CharField(max_length=255, null=True, blank=True)
    localitate = models.CharField(max_length=255)
    strada = models.CharField(max_length=255)
    numar = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    client = models.ForeignKey(Clienti, on_delete=models.SET_NULL, null=True, blank=True)
    alte_detalii = models.CharField(max_length=255)

    def __str__(self):
        return '{}, str. {}, nr. {}, judet {}'.format(self.localitate, self.strada, self.numar, self.judet)

    class Meta:
        verbose_name_plural = 'Adrese'


class AdresaSS(models.Model):
    localitate = models.CharField(max_length=255)
    strada = models.CharField(max_length=255)
    numar = models.CharField(max_length=255)
    judet = models.CharField(max_length=255)
    client = models.ForeignKey(Clienti, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return '{}, str. {}, nr. {}, judet {}'.format(self.localitate, self.strada, self.numar, self.judet)

    class Meta:
        verbose_name_plural = 'Adrese'


def increment_nr_reg():
    '''Afiseaza automat numarul de registru tinant cont de contracte, acte aditionale'''
    lst=[]
    ultimul_nr_reg_c = Contract.objects.all().order_by('nr_registru').last()
    ultimul_nr_reg_a = ActAditional.objects.all().order_by('nr_registru').last()
    reg1 = ultimul_nr_reg_c.nr_registru
    reg2 = ultimul_nr_reg_a.nr_registru
    lst.append(reg1)
    lst.append(reg2)
    nr_reg = max(lst)
    nou_nr_reg = nr_reg + 1
    return nou_nr_reg


def increment_nr_contr():
    '''Afiseaza automat numarul urmator de contract'''
    ultimul_nr_contr = Contract.objects.all().order_by('nr_contract').last()
    ultimul_nr = ultimul_nr_contr.nr_contract
    nou_nr_contr = ultimul_nr + 1
    return nou_nr_contr


class Contract(models.Model):
    '''Datele sumare de pe contract'''
    nr_registru = models.IntegerField(default=increment_nr_reg, unique=True)
    tip_contract = models.ForeignKey(CategorieContract, verbose_name='Categorie contract', on_delete=models.SET_NULL, null=True)
    nr_contract = models.IntegerField(default=increment_nr_contr)
    data_contract = models.DateField(null=True, blank=True)
    beneficiar = models.ForeignKey(Clienti, on_delete=models.CASCADE)
    data_incepere_contract = models.DateField(null=True, blank=True)
    data_sfarsit_contract = models.DateField(null=True, blank=True)
    produse = models.ManyToManyField(Produse, blank=True)
    servicii = models.ManyToManyField(ServiciiInformatice, blank=True)
    aplicatii = models.ManyToManyField(AplicatiiInfo98, blank=True)
    observatii = models.TextField(max_length=255, blank=True)
    
    class Meta:
        verbose_name_plural = 'Contracte'
        unique_together = ('nr_contract', 'data_contract')

    def __str__(self):
        return '{}/{} - {}'.format(self.nr_contract, self.data_contract, self.beneficiar)

    def data_incheiere(self):
        '''Calculeaza data de expirare a contractului in functie de actele aditionale aferente contractului'''
        if self.actaditional_set.all():
            lst=[]
            actad = self.actaditional_set.all().order_by('data_sfarsit_actaditional').last()
            data_actad = actad.data_sfarsit_actaditional
            lst.append(self.data_sfarsit_contract)
            lst.append(data_actad)
            data_incheiere_pc = max(lst)
            return data_incheiere_pc
        else:
            return self.data_sfarsit_contract

    def zile_pana_la_expirare(self):
        '''Calculeaza zilele pana la expirare pentru contractele care expira in urmatoarele 30 de zile'''
        data_incheierec = self.data_incheiere()
        azi = date.today()
        nr_zile_expirare = data_incheierec - azi
        if nr_zile_expirare < timedelta(days=30) and nr_zile_expirare > timedelta(days=0):
            return nr_zile_expirare.days

    def zile_de_la_expirare(self):
        '''Calculeaza zilele de la expirare pentru contractele care au expirat in ultimele 30 de zile'''
        data_incheierec = self.data_incheiere()
        azi = date.today()
        nr_zile_expirare = data_incheierec - azi
        if nr_zile_expirare > timedelta(days=-30) and nr_zile_expirare < timedelta(days=0):
            return nr_zile_expirare.days


class ActAditional(models.Model):
    '''Datele sumare de pe actul aditional aferent unui conrtact'''
    nr_registru = models.IntegerField(default=increment_nr_reg, unique=True)
    nr_actaditional = models.IntegerField()
    data_actaditional = models.DateField(null=True, blank=True)
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True)
    data_incepere_actaditional = models.DateField(null=True, blank=True)
    data_sfarsit_actaditional = models.DateField(null=True, blank=True)
    produse = models.ManyToManyField(Produse, blank=True)
    servicii = models.ManyToManyField(ServiciiInformatice, blank=True)
    aplicatii = models.ManyToManyField(AplicatiiInfo98, blank=True)
    observatii = models.TextField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Acte Aditionale'

    def __str__(self):
        return '{}/{}'.format(self.nr_actaditional, self.data_actaditional)

    # @property
    # def total(self):
    #     '''cand adaug cantitatea (cant_s, cant_a, cant_p) in tabel ar fi util sa folosesc ceva de genul:'''
    #     return self.price * self.quantity


class ContractScan(models.Model):
    '''Salvarea documentelor aferente contractului/actului aditional'''
    contract = models.ForeignKey(Contract, default=None, null=True, on_delete=models.CASCADE)
    actaditional = models.ForeignKey(ActAditional, default=None, null=True, blank=True, on_delete=models.CASCADE)
    documente = models.FileField(upload_to='media/')
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.uploaded_at, str(self.documente))

    def delete(self, *args, **kwargs):
        '''Stergerea documentelor aferente contractului/actului aditional'''
        self.documente.delete()
        # self.uploaded_at.delete()
        super().delete(*args, **kwargs)


def registru():
    '''Ordoneaza contractele si acteleaditonale in functie de numarul de registru'''
    contracte = Contract.objects.all()
    acteaditionale = ActAditional.objects.all()
    lst_contr_aa = sorted(chain(contracte, acteaditionale), key=attrgetter('nr_registru'))
    return lst_contr_aa
    

