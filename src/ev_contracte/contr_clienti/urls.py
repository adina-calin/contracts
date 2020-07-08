from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acasa'),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/', views.actaditional_detalii, name='actaditional-detail'),
    path('contract/new/', views.creeaza_contract, name='contract-nou'),
    path('contract/<int:pk1>/actaditional/new/', views.creeaza_actaditional, name='actaditional-nou'),
]
