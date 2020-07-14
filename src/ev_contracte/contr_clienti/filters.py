import django_filters
from .models import Contract, Clienti, Produse, ServiciiInformatice, AplicatiiInfo98

class ContractFilter(django_filters.FilterSet):
    class Meta:
        model = Contract
        fields = '__all__'
