from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='acasa'),
    path('contract/<int:pk1>/', views.contract_detalii, name='contract-detail'),
    path('contract/<int:pk1>/upload', views.contract_scan, name='contract-upload'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/', views.actaditional_detalii, name='actaditional-detail'),
    path('contract/new/', views.creeaza_contract, name='contract-nou'),
    path('contract/<int:pk1>/actaditional/new/', views.creeaza_actaditional, name='actaditional-nou'),
    path('contract/<int:pk1>/update/', views.update_contract, name='contract-update'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/update/', views.update_actaditional, name='actaditional-update'),
    path('contract/<int:pk1>/delete/', views.sterge_contract, name='contract-delete'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/delete/', views.sterge_actaditional, name='actaditional-delete'),
    path('contract/<int:pk1>/actaditional/<int:pk2>/upload/', views.actaditional_scan, name='actaditional-upload'),
    # path('about/', views.about, name='despre_app'),
]
