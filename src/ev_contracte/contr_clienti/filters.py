import django_filters
from django_filters import DateFilter, CharFilter
from .models import Contract, Clienti


class ContractFilter(django_filters.FilterSet):
    data_inceput = DateFilter(field_name="data_incepere_contract", lookup_expr='gte', label='Data de început')
    data_sfarsit = DateFilter(field_name="data_sfarsit_contract", lookup_expr='lte', label='Data de încheiere')
 
    class Meta:
        model = Contract
        fields = ['beneficiar']


class ClientiFilter(django_filters.FilterSet):
    societate = CharFilter(lookup_expr='icontains', label='')

    class Meta:
        model = Clienti
        fields = ['societate', ]




# , 'data_incepere_contract', 'data_sfarsit_contract', 'produse', 'servicii', 'aplicatii'