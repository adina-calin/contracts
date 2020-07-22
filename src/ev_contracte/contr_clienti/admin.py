from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from dynamic_raw_id.admin import DynamicRawIDMixin
from .models import Reprezentant, PersoanaContact, Adresa, Clienti, CategorieContract, Produse, AplicatiiInfo98, Contract, ServiciiInformatice, ActAditional, ContractScan


@admin.register(Clienti)
class  ClientiAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Date societate', {'fields': ['societate', 'cod_fiscal', 'platitor_tva', 'nr_registrul_comertului', 'sediul_social']}),
        ('Reprezentanți', {'fields': ['reprezentant']}),
        ('Puncte de lucru', {'fields': ['punct_de_lucru']}),
        ('Date bancare', {'fields': ['iban', 'banca_cont']}),
        ('Pesoane de contact', {'fields': ['persoana_contact']})
    ]

    list_display = ('societate', 'cod_fiscal', 'platitor_tva', 'nr_registrul_comertului', 'sediul_social', 'reprezentant_societate')
    list_filter = ('societate', 'cod_fiscal', 'platitor_tva', 'sediul_social')

    def reprezentant_societate(self, object):
        return ', '.join(str(reprezentant) for reprezentant in object.reprezentant.all())


class ContractScanAdmin(admin.StackedInline):
    model = ContractScan


@admin.register(Contract)
class ContractAdmin(DynamicRawIDMixin, admin.ModelAdmin):

    fieldsets = [
        ('Date contract', {'fields': ['nr_registru', 'tip_contract', ('nr_contract', 'data_contract'), 'beneficiar']}),
        ('Valabilitate contract', {'fields': [('data_incepere_contract', 'data_sfarsit_contract')]}),
        ('Produse/servicii', {'fields': ['produse', 'servicii', 'aplicatii']}),
        ('Detalii contract', {'classes': ('collapse',), 'fields': ['observatii']})
    ]

    list_display = ['nr_registru', 'tip_contract', 'nr_contract', 'data_contract', 'beneficiar', 'data_incepere_contract', 'data_sfarsit_contract', 'produse_contract', 'servicii_contract', 'aplicatii_contract', 'observatii']
    list_filter = ('nr_contract', 'data_contract', 'beneficiar', 'data_incepere_contract', 'data_sfarsit_contract', 'produse')
    search_fields = ('nr_contract', 'data_contract', 'beneficiar', 'data_incepere_contract', 'data_sfarsit_contract', 'produse')
    list_per_page = 10
    ordering = ['-nr_registru']
    inlines = [ContractScanAdmin]

    def produse_contract(self, object):
        return ', '.join(str(produs) for produs in object.produse.all())

    def servicii_contract(self, object):
        return ', '.join(str(serviciu) for serviciu in object.servicii.all())

    def aplicatii_contract(self, object):
        return ', '.join(str(aplicatie) for aplicatie in object.aplicatii.all())

    filter_horizontal = ('aplicatii','servicii',)
    dynamic_raw_id_fields = ('produse','aplicatii','servicii')


@admin.register(ActAditional)
class ActAditionalAdmin(DynamicRawIDMixin, admin.ModelAdmin):

    def numar_contract(self, instance):
        if instance.contract:
            return instance.contract.nr_contract

    def datacontract(self, instance):
        if instance.contract:
            return instance.contract.data_contract

    def beneficiarcontract(self, instance):
        if instance.contract:
            return instance.contract.beneficiar
        
    fieldsets = [
        ('Date contract / act aditional', {'fields': ['nr_registru', 'contract', ('nr_actaditional', 'data_actaditional')]}),
        ('Valabilitate act aditional', {'fields': [('data_incepere_actaditional', 'data_sfarsit_actaditional')]}),
        ('Produse/servicii', {'fields': ['produse', 'servicii', 'aplicatii']}),
        ('Detalii act aditiona', {'classes': ('collapse',), 'fields': ['observatii']})
    ]

    list_display = ['nr_registru', 'numar_contract', 'datacontract', 'beneficiarcontract', 'nr_actaditional', 'data_actaditional', 'produse_contract', 'servicii_contract', 'aplicatii_contract', 'observatii', 'data_incepere_actaditional', 'data_sfarsit_actaditional']
    # list_filter = ('nr_contract', 'data_contract', 'beneficiar', 'produse')
    # search_fields = ('nr_contract', 'data_contract', 'beneficiar', 'produse')
    list_per_page = 10
    ordering = ['-nr_actaditional']
    inlines = [ContractScanAdmin]

    def produse_contract(self, object):
        return ', '.join(str(produs) for produs in object.produse.all())

    def servicii_contract(self, object):
        return ', '.join(str(serviciu) for serviciu in object.servicii.all())

    def aplicatii_contract(self, object):
        return ', '.join(str(aplicatie) for aplicatie in object.aplicatii.all())


admin.site.register(Reprezentant)
admin.site.register(PersoanaContact)
admin.site.register(Adresa)
admin.site.register(CategorieContract)
admin.site.register(Produse)
admin.site.register(ServiciiInformatice)
admin.site.register(AplicatiiInfo98)
admin.site.register(ContractScan)



