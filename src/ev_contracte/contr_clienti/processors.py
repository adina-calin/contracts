from .models import Contract
from django import template


register = template.Library()
@register.tag()
def data_incheiere_contract(request):
    contract = Contract.objects.all().first()
    if contract.actaditional_set.all():
        ac=contract.actaditional_set.all().order_by('data_sfarsit_actaditional')
        al=ac.last()
        a_data_sfarsit_contract=al.data_sfarsit_actaditional
        context = {'a_data_sfarsit_contract': a_data_sfarsit_contract}
        return context
