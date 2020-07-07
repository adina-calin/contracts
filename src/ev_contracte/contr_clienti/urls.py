from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('actaditional/', views.actaditional_detalii, name='actaditional-detail'),
]
